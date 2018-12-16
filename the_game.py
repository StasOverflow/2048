import random


class GameBoard:
    cell = []
    dimension = 0

    def __init__(self, dimension):
        self.dimension = dimension
        self.cell = ([[self.Cell([x, y]) for x in range(dimension)] for y in range(dimension)])

    def __repr__(self):
        row_list = []
        for x in self.cell:
            row = '|\t' + '\t|\t'.join(str(e) for e in x) + '\t|'
            row_list.append(row)
        row_list = ('\n'.join(row_list))
        return row_list

    def _fill_random_with_random(self):
        empty_cell_list = list()
        for y in range(self.dimension):
            for x in range(self.dimension):
                if self.cell[x][y].value == 0:
                    empty_cell_list.append(self.cell[x][y])
        cell_to_fill_index = random.randint(0, len(empty_cell_list) - 1)
        empty_cell_coordinate = [empty_cell_list[cell_to_fill_index].coordinates[x] for x in range(2)]
        self.cell[empty_cell_coordinate[0]][empty_cell_coordinate[1]].value = 255
        # cell_raw[self.cell[x, y] for x in self.cell if ]
        for x in self.cell:
            print("one instance", x, '\n')
        row_num = random.randint(0, self.dimension-1)
        col_num = random.randint(0, self.dimension-1)
        print(row_num, col_num)

    class Cell:
        value = 0
        x_coord = 0
        y_coord = 0
        coordinates = 0

        def __init__(self, coordinates):
            self.coordinates = coordinates

        def __repr__(self):
            return str(self.value)


def game_session(board_dimension=2):
    board = GameBoard(board_dimension)
    for x in range(12):
        board._fill_random_with_random()
    print(board)


def main():
    game_session(5)


if __name__ == '__main__':
    main()
