from drawingСommands.line import Line
from drawingСommands.constant import Constant


class Rectangle(Line):
    def __init__(self, file, field):
        super().__init__(file, field, write_to_file=False, character=Constant.RECTANGLE_CHARACTER)
        self.file = file
        self.field = field

    def create(self, x1, y1, x2, y2):
        super().create(x1, y1, x2, y1)
        super().create(x2, y1, x2, y2)
        super().create(x1, y2, x2, y2)
        super().create(x1, y1, x1, y2)
        self.file.write('\n'.join(self.field) + '\n')
        return self.field
