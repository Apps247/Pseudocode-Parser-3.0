
# - ॐ गणेशाय नमः

import os
import sys

# * Read


def read():
    filename = sys.argv[1]
    with open(filename, 'r') as pseudocode_file:
        pseudocode_lines = [line.strip()
                            for line in pseudocode_file.readlines()]
    pseudocode_file.close()
    return pseudocode_lines


# * Translate

class VALUE():

    syntax_mapping_exempt = {
        '<=',
        '>=',
    }

    syntax_map = {
        '!=': 'raise SyntaxError("!=")',
        '%': '/100',
        '//': '#',
        '=': '==',
        '←' : '=',
        '<>': '!=',
        '&' : '+ "" +',
        # 'not' : 'raise SyntaxError("not")',
        'AND': 'and',
        'OR': 'or',
        'NOT': 'not',
        'TRUE': 'True',
        'FALSE': 'False',
    }

    def __init__(self, value):

        # concatenation_breakers = ['+', '/', '=', '-', '*', '(', ')']
        # comparison_operators = []

        def map_syntax(command):

            split_command = []
            quoted = False
            quote_type = None
            run = ''

            for character in command:
                if character == '\'' or character == '"':
                    if not quoted:
                        split_command.append(run)
                        quoted = True
                        quote_type = character
                        run = ''
                        run += character
                    elif quoted and quote_type == character:
                        run += character
                        split_command.append(run)
                        quoted = False
                        run = ''
                    else:
                        run += character
                else:
                    run += character
            split_command.append(run)

            split_command = [
                commandlet for commandlet in split_command if commandlet != '']

            def syntax_mapped(command):
                command = command.split(' ')
                for c in range(len(command)):
                    for syntax in VALUE.syntax_map:
                        if (command[c] not in VALUE.syntax_mapping_exempt):
                            command[c] = command[c].replace(
                                syntax, VALUE.syntax_map[syntax])
                command = ' '.join(command)
                return command

            for index, commandlet in enumerate(split_command):
                if not ((commandlet.startswith('\'') and commandlet.endswith('\'')) or (commandlet.startswith('"') and commandlet.endswith('"'))):
                    split_command[index] = syntax_mapped(commandlet)

            command = ''.join(split_command)

            # if self.concatenation_required :
            #     command = f'"".join([{command}])'
            #     command = command.replace('$SEPARATE$' , '," ",')
            #     command = command.replace('$CONCATENATE$' , ',')

            # if ('&') in command:
            #     print("Yes", command)
            #     for
            #     command = command.split('&')

            return command

        #     print(' '.join(split_command))
        #     return ' '.join(split_command)
        # print('VALUE:',value)
        self.translated_line = map_syntax(value)


TYPE_DICT = {
    'STRING': 'String',
    'CHAR': 'char',
    'INTEGER': 'int',
    'REAL': 'float',
    'BOOLEAN': 'bool',

}
INPUT_TYPE_DICT = {
    'String': 'nextLine',
    'int': 'nextInt',
}

symbol_table = {}

class DECLARE:
    def __init__(self, pseudocode_line):
        identifier = pseudocode_line.split(':')[0].split(' ')[1].strip()
        data_type = TYPE_DICT[pseudocode_line.split(':')[1].strip()]

        symbol_table[identifier] = data_type

        self.translated_line = f'{data_type} {identifier};'

class CONSTANT:
    def __init__(self, pseudocode_line):
        identifier = pseudocode_line.split('=')[0].split(' ')[1].strip()
        value = VALUE(pseudocode_line.split('=')[1:]).translated_line

        self.translated_line = f'final var {identifier} = {value};'

class INPUT:
    def __init__(self, pseudocode_line):
        prompt = VALUE(' '.join(pseudocode_line.split(' ')[1:-1])).translated_line
        identifier = (pseudocode_line.split(' ')[-1])

        self.translated_line = f'System.out.print({prompt}); {identifier} = inputScanner.{INPUT_TYPE_DICT[symbol_table[identifier]]}();'


class OUTPUT:
    def __init__(self, pseudocode_line):
        args = VALUE(' '.join(pseudocode_line.split(' ')[1:])).translated_line

        self.translated_line = f'System.out.println({args});'


class PROCESS:
    def __init__(self, pseudocode_line):
        self.translated_line = VALUE(pseudocode_line).translated_line + ';'

class BLOCK_OPENER:
    def __init__(self, pseudocode_line):
            self.translated_line = '{'
class BLOCK_CLOSER:
    def __init__(self, pseudocode_line):
            self.translated_line = '}'


KEYWORD_DICT = {
    'INPUT' : INPUT,
    'OUTPUT': OUTPUT,
    'DECLARE' : DECLARE,
    'CONSTANT' : CONSTANT,
}


def translate(pseudocode_lines):
    translated_lines = [KEYWORD_DICT.get(line.strip().split(' ')[0], PROCESS)(
        line.strip()).translated_line for line in pseudocode_lines if line != '']
    translated_lines = [
        '''import java.util.Scanner;public class Main {
        public static void main(String[] args) {
        Scanner inputScanner = new Scanner(System.in);'''
    ] \
    + translated_lines + \
    [
        'inputScanner.close();\n}\n}'
    ]
    return translated_lines


#  * Write

def write(translated_lines):
    with open('Main.java', 'w') as translated_file:
        translated_file.write("\n".join(translated_lines))
    translated_file.close()


if __name__ == "__main__":
    write(translate(read()))
    os.system('javac Main.java')
    os.system('java Main')
