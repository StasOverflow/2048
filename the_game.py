import random
import getch


class GameBoard:
    cell_row_list = []
    dimension = 0
    number_of_the_game = 3

    def __init__(self, dimension):
        self.dimension = dimension
        self.cell_row_list = ([[self.Cell([x, y]) for x in range(dimension)] for y in range(dimension)])

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
        # for x in empty_cell_list:
        #     print(x.coordinates)
        if empty_cell_list:
            print("not yet out")
            cell_to_fill_index = random.randint(0, len(empty_cell_list) - 1)
            empty_cell_coordinate = [empty_cell_list[cell_to_fill_index].coordinates[x] for x in range(2)]
            # print(empty_cell_coordinate[0], empty_cell_coordinate[1])
            value = self._get_random_number()
            # print(value)
            self.cell_row_list[empty_cell_coordinate[0]][empty_cell_coordinate[1]].value = value
        else:
            print("vse, net vsobodnih")
        return empty_cell_list      # going to be false in case the list will be empty


    def func(self, array):
        for index in range(len(array)-1):
            # print("--------------------------------\nb4 all")
            # print("curr ", shifting[index])
            # print("next ", shifting[index + 1])
            # print(self.__repr__())
            for ind_cell in range(len(array[index])):
                if array[index][ind_cell].merge_with(array[index + 1][ind_cell]):
                    array[index + 1][ind_cell].value = 0
            # print("--------------------------------\nafter all")


    def shift_cells(self, direction):
        if direction == 1:
            shifting = self.cell_row_list
        elif direction == 0:
            shifting = list(reversed(self.cell_row_list))
        # print("shifting b4 ", shifting)
        print("len shifting ravno ", len(shifting))
        for _ in range(2):
            self.func(shifting)
        return self._fill_random_with_random()
        # for _ in range(len(shifting)-1):        # workaround additional loop
            # print("curr ", shifting[index])
            # print("next ", shifting[index + 1])

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


def game_session(board_dimension=2):
    board = GameBoard(board_dimension)
    # board._fill_random_with_random()
    # print(board)
    while(board.shift_cells(1)):
        print("--------------------------------\nadded random")
        # board._fill_random_with_random()
        print(board)
        char = getch.getche() # also displayed on the screen
        # x = board.shift_cells(1)
        # print(x)
        print("--------------------------------\nafter all")
        print(board)
    print("ENDGAME")


def main():
    game_session(3)


if __name__ == '__main__':
    main()
