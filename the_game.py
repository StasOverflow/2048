import random
import getch


def receive_character():
    return getch.getch()


class GameBoard:
    cell_row_list = []
    dimension = 0
    number_of_the_game = 3
    arrow = False

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
        self.cell_row_list = [[self.Cell([x, y]) for x in range(dimension)] for y in range(dimension)]

    def __repr__(self):
        row_list = []
        for x in self.cell_row_list:
            row = '|\t' + '\t|\t'.join(str(e) for e in x) + '\t|'
            row_list.append(row)
        row_list = ('\n'.join(row_list))
        return row_list

    def _get_random_number(self):
        num = self.number_of_the_game
        seed_1 = random.randint(0, 5)
        seed_2 = random.randint(0, 5)
        if seed_2 == seed_1:
            num = num * num
        return num

    def _fill_random_with_random(self):
        empty_cell_list = list()
        for y in range(self.dimension):
            for x in range(self.dimension):
                if self.cell_row_list[x][y].value == 0:
                    empty_cell_list.append(self.cell_row_list[y][x])
        if empty_cell_list:
            print("not yet out")
            cell_to_fill_index = random.randint(0, len(empty_cell_list) - 1)
            empty_cell_coordinate = [empty_cell_list[cell_to_fill_index].coordinates[x] for x in range(2)]
            value = self._get_random_number()
            self.cell_row_list[empty_cell_coordinate[0]][empty_cell_coordinate[1]].value = value
        else:
            print("vse, net vsobodnih")
        return empty_cell_list      # going to be false in case the list will be empty

    def shift_lines(self, array):
        print(self.__repr__())

        for num, x in enumerate(array):
            print(x[0], x[1], x[2])
            x[0].merge_with()
        # for index in range(len(array)-1):
        #     # print("--------------------------------\nb4 all")
        #     print("curr ", array[index])
        #     print("next ", array[index + 1])
        #     # print(self.__repr__())
        #     for ind_cell in range(len(array[index])):
        #         if array[index][ind_cell].merge_with(array[index + 1][ind_cell]):
        #             array[index + 1][ind_cell].value = 0
        return array
            # print("--------------------------------\nafter all")

    def shift_to_direction(self, direction):
        shifting = [[self.Cell([x, y]) for x in range(self.dimension)] for y in range(self.dimension)]

        if direction == 1:
            shifting = self.cell_row_list.copy()
        if direction == 2:
            shifting = list(zip(*self.cell_row_list.copy()))
        elif direction == 3:
            shifting = list(reversed(self.cell_row_list))
        # print("len shifting ravno ", len(shifting))
        # for _ in range(2):
        shifting = self.shift_lines(shifting)
        self.cell_row_list = shifting.copy()
        return self._fill_random_with_random()


    def _proceed_move(self, move):
        if move == 'Up':
            print("moving up")
        elif move == 'Down':
            print("moving down")
        elif move == 'Right':
            print("moving right")
        elif move == 'Left':
            print("moving left")
        elif move == 'Enter':
            print("Entering something")
        elif move == 'Quit':
            print("Exiting")
            return 0


    def receive_move(self, ch):
        if ch.encode() == b'[':
            self.arrow = True
        print(ch, ch.encode())
        print(self.arrow)
        if ch in self.moves:
            if not self.arrow:
                print(ch)
                self._proceed_move(self.moves[ch])
                self.arrow = False
                return True
            else:
                self.arrow = False
        return False


    class Cell:
        value = 0
        coordinates = 0

        def __init__(self, coordinates):
            self.coordinates = coordinates

        def __repr__(self):
            return str(self.value)

        def compare(self, cell):
            if self.value == cell.value:
                return True
            else:
                return False

        def merge_with(self, cell):
            # print("comparing ", self.value, "with ", cell.value)
            merged = False
            if self.compare(cell):
                if self.value != 0:
                    self.value = self.value * GameBoard.number_of_the_game
                    merged = True
            elif self.value == 0:
                if cell.value != 0:
                    self.value = cell.value
                    merged = True
            # print("as a result ", self.value)
            return merged


#
# def make_a_move(game_board):
#     game_board.receive_move(receive_character())


def game_session(board_dimension=2):
    board = GameBoard(board_dimension)
    board._fill_random_with_random()
    playing = True
    while 1:
        if board.receive_move(receive_character()):
            board._fill_random_with_random()
            print(board)
    # while board.shift_to_direction(1):
        # print("--------------------------------\nadded random")
        # board._fill_random_with_random()
        # print(board)
        # char = getch.getche() # also displayed on the screen
        # x = board.shift_cells(1)
        # print(x)
        # print("after all")
        # print(board)
        # print("--------------------------------\n")
    # print("ENDGAME")
    # board.receive_character()

def main():
    game_session(4)


if __name__ == '__main__':
    main()
