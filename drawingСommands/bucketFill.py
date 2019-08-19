from drawingСommands.constant import Constant


class BucketFill:
    def __init__(self, file, field, character):
        self.file = file
        self.field = field
        self.character = character

    @staticmethod
    def valid(value):
        if value == Constant.LINE_CHARACTER or value == Constant.RECTANGLE_CHARACTER or\
                value == Constant.HORIZONTAL_BORDER or value == Constant.VERTICAL_BORDER:
            return False
        return True

    def empty_place(self, x, y):
        empty_place_index = []
        for index, value in enumerate(self.field[y][1:-1]):
            if self.valid(value):
                empty_place_index.append(index+1)
            elif index+1 < x:
                empty_place_index.clear()
            elif index+1 > x:
                break

        for index in empty_place_index:
            self.field[y] = ''.join((self.field[y][:index], self.character, self.field[y][index + 1:]))

        for i in empty_place_index:
            if self.valid(self.field[y+1][i]) and\
                    self.field[y+1][i] != self.character:
                self.empty_place(i, y+1)
            if self.valid(self.field[y-1][i]) and\
                    self.field[y-1][i] != self.character:
                self.empty_place(i, y-1)

    def create(self, x, y):
        if type(x) == str or type(y) == str:
            raise Exception('Bad argument')
        if not self.valid(self.field[y][x]):
            raise Exception('Bad argument')
        self.empty_place(x, y)
        self.file.write('\n'.join(self.field) + '\n')
        return self.field
