

class ConstantCommands:
    CANVAS_COMMAND = 'C'
    LINE_COMMAND = 'L'
    RECTANGLE_COMMAND = 'R'
    BUCKET_FILL_COMMAND = 'B'

    COMMANDS = [CANVAS_COMMAND, LINE_COMMAND, RECTANGLE_COMMAND, BUCKET_FILL_COMMAND]


class ConstantCanvas:
    HORIZONTAL_BORDER = '-'
    VERTICAL_BORDER = '|'
    BACKGROUND = ' '


class ConstantCharacter:
    LINE_CHARACTER = 'x'
    RECTANGLE_CHARACTER = 'x'


class Constant(ConstantCommands, ConstantCanvas, ConstantCharacter):
    pass
