
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
        '/': '/(double)',
        '=': '==',
        '←': '=',
        '<>': '!=',
        '&': '+ "" +',
        # 'not' : 'raise SyntaxError("not")',
        'AND': '&&',
        'OR': '||',
        'NOT': '!',
        'TRUE': 'True',
        'FALSE': 'False',

        'STRING_COMPARE' : 'Utility.stringCompare'
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
    'INTEGER': 'long',
    'REAL': 'double ',
    'BOOLEAN': 'boolean',

}
INPUT_TYPE_DICT = {
    'String': 'nextLine()',
    'char' : 'next().charAt(0)',
    'long' : 'nextLong()',
    'double' : 'nextDouble()',
    'boolean': 'nextBoolean()',
}

symbol_table = {}

status = [] # * To keep track of blocks being translated that need special actions


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
        prompt = VALUE(
            ' '.join(pseudocode_line.split(' ')[1:-1])).translated_line
        identifier = (pseudocode_line.split(' ')[-1])

        self.translated_line = f'System.out.print({prompt}); {identifier} = inputScanner.{INPUT_TYPE_DICT[symbol_table[identifier]]};'


class OUTPUT:
    def __init__(self, pseudocode_line):
        args = VALUE(' '.join(pseudocode_line.split(' ')[1:])).translated_line

        self.translated_line = f'System.out.println({args});'

class OUTPUT_CONT:
    def __init__(self, pseudocode_line):
        args = VALUE(' '.join(pseudocode_line.split(' ')[1:])).translated_line

        self.translated_line = f'System.out.print({args});'


class IF:
    def __init__(self, pseudocode_line):
        condition = VALUE(' '.join(pseudocode_line.split(' ')[1:])).translated_line
        
        self.translated_line = f'if ({condition})'

class ELSE:
    def __init__(self, pseudocode_line):
       self.translated_line = '} else {'


class CASE:
    def __init__(self, pseudocode_line):
        status.append('CASE')
        
        identifier = ' '.join(pseudocode_line.split(' ')[2:])

        self.translated_line = f'switch ({identifier}) {{'


class FOR:
    def __init__(self, pseudocode_line):
        identifier = (pseudocode_line.split('←')[0][3:]).strip()
        start = ('←'.join(pseudocode_line.split('←')[1:])).split('TO')[0].strip()
        end = ('←'.join(pseudocode_line.split('←')[1:])).split('TO')[1].strip()
        # todo: handle keywords such as 'TO' appearing in literals
        
        self.translated_line = f'for (int {identifier} = {start}; {identifier} <= {end}; {identifier}++) {{'


class WHILE:
    def __init__(self, pseudocode_line):
        condition = VALUE(' '.join(pseudocode_line.split(' ')[1:])).translated_line
        
        self.translated_line = f'while ({condition}) {{'


class PROCESS:
    def __init__(self, pseudocode_line):

        if ('CASE' in status):
            split_pseudocode_line = pseudocode_line.split(':')
            self.translated_line = 'case ' + split_pseudocode_line[0] + ' : ' + KEYWORD_DICT.get(':'.join(split_pseudocode_line[1:]).strip().split(' ')[0], PROCESS)(':'.join(split_pseudocode_line[1:]).strip()).translated_line + ' break;'
            # todo: handle cases such as ':' (string literal)
        else:
            self.translated_line = VALUE(pseudocode_line).translated_line + ';'


class BLOCK_OPENER:
    def __init__(self, pseudocode_line):
        self.translated_line = '{'


class BLOCK_CLOSER:
    def __init__(self, pseudocode_line):
        self.translated_line = '}'


KEYWORD_DICT = {
    'INPUT': INPUT,
    'OUTPUT': OUTPUT,
    'OUTPUT_CONT': OUTPUT_CONT,
    'DECLARE': DECLARE,
    'CONSTANT': CONSTANT,
    'IF' : IF,
    'THEN' : BLOCK_OPENER,
    'ELSE' : ELSE,
    'ENDIF' : BLOCK_CLOSER,
    'CASE' : CASE,
    'ENDCASE' : BLOCK_CLOSER,
    'FOR' : FOR,
    'ENDFOR' : BLOCK_CLOSER,
    'WHILE' : WHILE,
    'ENDWHILE' : BLOCK_CLOSER,
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
