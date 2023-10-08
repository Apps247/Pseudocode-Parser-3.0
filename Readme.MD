# Pseudocode-Parser-3.0

This is a project that aims to parse pseudocode into executable code in different languages. It supports Python, Java, and C++ as target languages. It also provides a graphical user interface for users to input pseudocode and see the output code.

## Features

- Parse pseudocode into Python, Java, or C++ code
- Support basic data types, variables, operators, expressions, assignments, and control structures
- Support user-defined functions and parameters
- Support string comparison and concatenation
- Support while loops and nested loops
- Provide a GUI for user interaction

## Usage

Note: this is an experimental project, and it is very difficult to comprehend 

To run the project, you need to have Java installed on your machine. You can download Java from [here](^1^).

To launch the GUI, run the following command in the terminal:

`java Main`

You will see a window with a text area for inputting pseudocode and three buttons for choosing the target language. You can type or paste your pseudocode in the text area and click on one of the buttons to generate the corresponding code. The output code will be displayed in another window.

You can also run the project without the GUI by using the following command:

`java Main <input_file> <output_file> <language>`

where `<input_file>` is the name of the file containing pseudocode, `<output_file>` is the name of the file where the output code will be written, and `<language>` is one of `python`, `java`, or `cpp`.

For example, to parse pseudocode from `code.cpd` into Python code and write it to `code.py`, you can use:

`java Main code.cpd code.py python`

## Examples

Here are some examples of pseudocode and their corresponding output code in different languages.

### Example 1

Pseudocode:

```
FUNCTION SUM(A,B)
    RETURN A+B
END FUNCTION

X = 10
Y = 20
Z = SUM(X,Y)
PRINT Z
```

Python:

```python
def SUM(A,B):
    return A+B

X = 10
Y = 20
Z = SUM(X,Y)
print(Z)
```

Java:

```java
public class Main {
    public static int SUM(int A, int B) {
        return A+B;
    }

    public static void main(String[] args) {
        int X = 10;
        int Y = 20;
        int Z = SUM(X,Y);
        System.out.println(Z);
    }
}
```

C++:

```cpp
#include <iostream>
using namespace std;

int SUM(int A, int B) {
    return A+B;
}

int main() {
    int X = 10;
    int Y = 20;
    int Z = SUM(X,Y);
    cout << Z << endl;
    return 0;
}
```

### Example 2

Pseudocode:

```
FUNCTION GREET(NAME)
    PRINT "Hello, " + NAME + "!"
END FUNCTION

NAMES = ["Alice", "Bob", "Charlie"]
FOR EACH NAME IN NAMES
    GREET(NAME)
END FOR
```

Python:

```python
def GREET(NAME):
    print("Hello, " + NAME + "!")

NAMES = ["Alice", "Bob", "Charlie"]
for NAME in NAMES:
    GREET(NAME)
```

Java:

```java
import java.util.Arrays;

public class Main {
    public static void GREET(String NAME) {
        System.out.println("Hello, " + NAME + "!");
    }

    public static void main(String[] args) {
        String[] NAMES = {"Alice", "Bob", "Charlie"};
        for (String NAME : NAMES) {
            GREET(NAME);
        }
    }
}
```

C++:

```cpp
#include <iostream>
#include <string>
using namespace std;

void GREET(string NAME) {
    cout << "Hello, " + NAME + "!" << endl;
}

int main() {
    string NAMES[] = {"Alice", "Bob", "Charlie"};
    int size = sizeof(NAMES)/sizeof(NAMES[0]);
    for (int i = 0; i < size; i++) {
        GREET(NAMES[i]);
    }
    return 0;
}
```

## Limitations

This project is not a complete pseudocode parser. It has some limitations and assumptions, such as:

- While attempting to be as lax with pseudocode accepted, the pseudocode style must closely adhere to CAIE's A-Level Computer Science 2021 prescribed standard
- Not all pieces of pseudocode can be parsed into all the available languages

## Future Work

Some possible improvements and extensions for this project are:

- Add more features and functionalities to the GUI, such as syntax highlighting, error handling, and file saving.
- Add more support for different data structures, such as lists, sets, dictionaries, and matrices.
- Add more support for different operators, such as arithmetic, bitwise, and relational operators.
- Add more support for different control structures, such as switch-case, break, continue, and return statements.
- Add more support for different built-in functions, such as math, string, and array functions.
- Add more support for different target languages, such as C#, Ruby, or JavaScript.
