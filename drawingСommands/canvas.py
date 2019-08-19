from drawingСommands.constant import Constant


class Canvas:
    def __init__(self, file):
        self.file = file

    def create(self, w, h):
        if type(h) == str or type(w) == str:
            raise Exception('Bad argument')
        if w < 0 or h < 0:
            raise Exception('w or h - negative')

        output_field = [Constant.HORIZONTAL_BORDER * (w + 2)]
        for _ in range(h):
            output_field.append(Constant.VERTICAL_BORDER + Constant.BACKGROUND * w +
                                Constant.VERTICAL_BORDER)
        output_field.append(Constant.HORIZONTAL_BORDER * (w + 2))

        self.file.write('\n'.join(output_field) + '\n')
        return output_field
