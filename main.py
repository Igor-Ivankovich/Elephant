import sys

from drawingСommands.bucketFill import BucketFill
from drawingСommands.canvas import Canvas
from drawingСommands.file import File
from drawingСommands.line import Line
from drawingСommands.rectangle import Rectangle

from drawingСommands.constant import Constant


class Main:
    def __init__(self, output_path, commands):
        self.output_path = output_path
        self.commands = commands

    def valid_data(self):
        for command in self.commands:
            if command == '':
                raise Exception('Empty line')
            command = command[0]
            if command not in Constant.COMMANDS:
                raise Exception('Unknown command')

        if not self.commands:
            raise Exception('Not found  commands')

        if self.commands[0][0] != Constant.CANVAS_COMMAND:
            raise Exception('The first command does not create a canvas')

    def write_in_output_file(self):
        self.valid_data()
        with open(self.output_path, 'a') as file:
            output_field = []
            for line in self.commands:
                line = line.split()
                command = line[0]
                parameter = [int(param) if param.isdigit() else param for param in line[1:]]

                if command == Constant.CANVAS_COMMAND:
                    if len(parameter) > 2:
                        raise Exception('Too many parameters')
                    output_field = Canvas(file).create(*parameter)
                elif command == Constant.LINE_COMMAND:
                    if len(parameter) > 4:
                        raise Exception('Too many parameters')
                    output_field = Line(file, output_field).create(*parameter)
                elif command == Constant.RECTANGLE_COMMAND:
                    if len(parameter) > 4:
                        raise Exception('Too many parameters')
                    output_field = Rectangle(file, output_field).create(*parameter)
                elif command == Constant.BUCKET_FILL_COMMAND:
                    if len(parameter) > 3:
                        raise Exception('Too many parameters')
                    output_field = BucketFill(file, output_field, parameter[-1]).create(*parameter[:-1])
        return output_field


def main(argv):
    argv = argv[1:3]
    if len(argv) < 2:
        raise Exception('Bad arguments')
    input_file, output_file = (argv[0], argv[1])

    commands = File(File(input_file).file_path()).read_file()
    Main(File(output_file).file_path(), commands).write_in_output_file()


if __name__ == '__main__':
    main(sys.argv)
