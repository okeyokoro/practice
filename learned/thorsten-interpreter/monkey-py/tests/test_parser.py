from monkey.lexer import Lexer
from monkey.lexer import Parser


def test_parsing_let_statements():
    input = """
        let x = 5;
        let y = 10;
        let foobar = 838383;
    """
    lexer = Lexer(input)
    parser = Parser(lexer)

