import random
import getch


def receive_character():
    try:
        ch = getch.getch()
    except OverflowError:
        print("Please use EN Layout")
        ch = None
    return ch


class Game:
    cell_row_list = []
    dimension = 0
    number_of_the_game = 3
    points = 0
    arrow = False
    game_ongoing = False
    game_finished = False
    permission_to_add_random = False
    lines_moved = 0

    moves = {
        'w': 'Up',
        'W': 'Up',
        'd': 'Right',
        'D': 'Right',
        's': 'Down',
        'S': 'Down',
        'a': 'Left',
        'A': 'Left',
        '\n': 'Enter',
        'q': 'Quit',
        'Q': 'Quit',
        # '\r': "Enter",
    }

    def __init__(self, dimension):
        self.dimension = dimension
        self.cell_row_list = [[self.Cell() for x in range(dimension)] for y in range(dimension)]

    def __repr__(self):
        row_list = []
        for x in self.cell_row_list:
            row = '\t' + '\t\t'.join(str(e) for e in x) + '\t'
            row_list.append(row)
        row_list = '\n'.join(row_list) + '\n' + 'Your Game Score is: ' + str(self.points)
        return row_list

    def game_session_end(self):
        print('Your score is: ', self.points, 'Game Over\n')
        exit()

    def game_session_start(self):
        self.fill_random_cell()
        self.fill_random_cell()
        print('Use `W`, `A`, `S`, `D` (EN layout) to move\nPress `Enter`, press `Q` to quit')
        playing = True
        while playing:
            cmd = receive_character()
            if self.receive_move(cmd):
                if not self.game_ongoing:
                    print('To start a game press Enter')
                else:
                    if self.permission_to_add_random:
                        self.fill_random_cell()
                        print(self.__repr__())
                if self.game_finished:
                    self.game_session_end()

    def _proceed_move(self, move):
        if move in self.moves.values():
            if move == 'Quit':
                self.game_session_end()
            if self.game_ongoing:
                self.shift_to_direction(move)
            else:
                if move == 'Enter':
                    self.game_ongoing = True
                    print('Starting game')
                    print(self.__repr__())

    def receive_move(self, ch):
        if ch is not None:
            if ch.encode() == b'[':
                self.arrow = True
            if ch in self.moves:
                if not self.arrow:
                    self._proceed_move(self.moves[ch])
                    self.arrow = False
                    return True
                else:
                    self.arrow = False
        return False

    def _get_random_number(self):
        num = self.number_of_the_game
        seed_1 = random.randint(0, 5)
        seed_2 = random.randint(0, 5)
        if seed_2 == seed_1:
            num = num * num
        return num

    def fill_random_cell(self):
        index_list = list()
        for x in range(self.dimension):
            for y in range(self.dimension):
                if self.cell_row_list[x][y].value == 0:
                    index_list.append([x, y])
        if index_list:
            rand_cell_index = random.randint(0, len(index_list) - 1)
            value = self._get_random_number()
            x_coord = index_list[rand_cell_index][0]
            y_coord = index_list[rand_cell_index][1]
            self.cell_row_list[x_coord][y_coord].value = value
        else:
            self.game_finished = True
        return index_list

    def shift_lines(self, array):
        # first, delete all empty elements to shift cells to a border
        new_array = [x for x in array if x.value != 0]
        new_array.extend([self.Cell(0) for x in range(self.dimension - len(new_array))])

        shift_performed = False
        points = 0

        # then check for similar cells to multiply
        for x in range(self.dimension-1):
            if new_array[x].value:
                # print("in cell ", x)
                if new_array[x].value == new_array[x+1].value:
                    new_array[x+1].value = new_array[x].value * Game.number_of_the_game
                    points = points + new_array[x+1].value
                    new_array.pop(x)
                    new_array.append(self.Cell(0))
            if array[x].value != new_array[x].value:
                shift_performed = True
        if shift_performed:
            self.lines_moved = self.lines_moved + 1
        self.points = self.points + points
        return new_array

    def shift_to_direction(self, move):
        """Reshuffle a current set of cells to according to the move received
           because shifting always goes from left to right

           After performing a shifting itself reshuffle cells back to were they
           were
        """
        shift_list = [list() for _ in range(self.dimension)]
        if move == 'Up':
            for y in range(self.dimension):
                for x in range(self.dimension):
                    shift_list[y].append(self.cell_row_list[x][y])
        elif move == 'Down':
            for y in range(self.dimension):
                for x in reversed(range(self.dimension)):
                    shift_list[y].append(self.cell_row_list[x][y])
        elif move == 'Right':
            for y in range(self.dimension):
                for x in range(self.dimension):
                    shift_list[y].append(self.cell_row_list[y][self.dimension - 1 - x])
        elif move == 'Left':
            for y in range(self.dimension):
                for x in range(self.dimension):
                    shift_list[y].append(self.cell_row_list[y][x])
        elif move == 'Enter':
            self.permission_to_add_random = False
            return None

        shift_row = list()
        for x in range(self.dimension):
            shift_row.append(self.shift_lines(shift_list[x]))

        if self.lines_moved:
            self.permission_to_add_random = True
        else:
            self.permission_to_add_random = False
        self.lines_moved = 0

        if move == 'Up':
            for y in range(self.dimension):
                for x in range(self.dimension):
                    self.cell_row_list[x][y] = shift_row[y][x]
        elif move == 'Down':
            for y in range(self.dimension):
                for x in reversed(range(self.dimension)):
                    self.cell_row_list[(self.dimension-1)-x][y] = shift_row[y][x]
        elif move == 'Right':
            for y in range(self.dimension):
                for x in range(self.dimension):
                    self.cell_row_list[y][x] = shift_row[y][(self.dimension-1)-x]
        elif move == 'Left':
            for y in range(self.dimension):
                for x in range(self.dimension):
                    self.cell_row_list[y][x] = shift_row[y][x]

    class Cell:
        """A separate class, containing cell attributes

           since there is only command line interface available
           The only attribute of the class is value
        """
        value = 0

        def __init__(self, value=0):
            self.value = value

        def __repr__(self):
            return str(self.value)


def main():
    new_game = Game(4)
    new_game.game_session_start()


if __name__ == '__main__':
    main()
