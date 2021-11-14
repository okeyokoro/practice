import getpass
from monkey.lexer import Lexer
from monkey.lexer import TokenType


def greeting():
    print(f"Hello {getpass.getuser()}! This is the Monkey programming language!\n"
        "Feel free to type in commands")

def repl():
    line = input(">> ")
    lexer = Lexer(line)

    while (tok := lexer.next_token()).type not in {TokenType.ILLEGAL, TokenType.EOF}:
        print(tok)

    repl()


if __name__ == "__main__":
    greeting()
    repl()

