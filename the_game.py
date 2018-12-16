import random


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
            num = num ** num
        return num

    def _fill_random_with_random(self):
        empty_cell_list = list()
        for y in range(self.dimension):
            for x in range(self.dimension):
                if self.cell_row_list[x][y].value == 0:
                    empty_cell_list.append(self.cell_row_list[y][x])
        # for x in empty_cell_list:
        #     print(x.coordinates)
        cell_to_fill_index = random.randint(0, len(empty_cell_list) - 1)
        empty_cell_coordinate = [empty_cell_list[cell_to_fill_index].coordinates[x] for x in range(2)]
        print(empty_cell_coordinate[0], empty_cell_coordinate[1])
        value = self._get_random_number()
        print(value)
        self.cell_row_list[empty_cell_coordinate[0]][empty_cell_coordinate[1]].value = value

    def shift_cells(self, direction):
        if direction == 1:
            shifting = self.cell_row_list
            cells_addit = shifting[self.dimension - 1]
            print(cells_addit)
            cells_base = shifting[self.dimension - 2]
            for num in range(len(cells_addit)):
                print(cells_addit[num], cells_base[num])
                # cells_base[num].merge_with(cells_addit[num])
                if cells_base[num].compare(cells_addit[num]):
                    if cells_base[num].value != 0:
                        cells_base[num].value = cells_base[num].value**self.number_of_the_game
                    cells_addit[num].value = 0       # replace with *prev*
                else:
                    if cells_base[num].value == 0:
                        if cells_addit[num].value != 0:
                            cells_base[num].value = cells_addit[num].value
                            cells_addit[num].value = 0
            for row in shifting:
                row = cells_base


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
            self.value = cell.value


def game_session(board_dimension=2):
    board = GameBoard(board_dimension)
    for x in range(2):
        board._fill_random_with_random()
    print(board)
    board.shift_cells(1)
    print(board)


def main():
    game_session(2)


if __name__ == '__main__':
    main()
