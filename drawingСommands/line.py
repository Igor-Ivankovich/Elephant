from drawingСommands.constant import Constant


class Line:
    def __init__(self, file, field, write_to_file=True, character=Constant.LINE_CHARACTER):
        self.file = file
        self.field = field
        self.character = character
        self.write_to_file = write_to_file

    def valid_data(self, x1, y1, x2, y2):
        if type(x1) == str or type(y1) == str or type(x2) == str or type(y2) == str:
            raise Exception('Bad argument')

        if x1 != x2 and y1 != y2:
            raise Exception('No vertical or horizontal line')

        len_x = len(self.field[0]) - 1
        len_y = len(self.field) - 1

        if x1 > len_x or x2 > len_x or x1 < 1 or x2 < 1 \
                or y1 > len_y or y2 > len_y or y1 < 1 or y2 < 1:
            raise Exception('Not correct coordinates')

    def create(self, x1, y1, x2, y2):
        self.valid_data(x1, y1, x2, y2)
        if x1 == x2:
            for index in range(len(self.field)):
                if y1 <= index <= y2:
                    self.field[index] = ''.join((self.field[index][:x1],
                                                 self.character,
                                                 self.field[index][x1 + 1:]))
        if y1 == y2:
            for index in range(len(self.field[y1])):
                if x1 <= index <= x2:
                    self.field[y1] = ''.join((
                        self.field[y1][:index],
                        self.character,
                        self.field[y1][index + 1:]))
        if self.write_to_file:
            self.file.write('\n'.join(self.field) + '\n')
        return self.field
