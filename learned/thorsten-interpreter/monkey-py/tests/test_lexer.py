from monkey.lexer import Token
from monkey.lexer import TokenType
from monkey.lexer import Lexer


def test_next_token():
    input = "=+(){},;"

    expected = [
        (TokenType.ASSIGN, "="),
        (TokenType.PLUS, "+"),
        (TokenType.LPAREN, "("),
        (TokenType.RPAREN, ")"),
        (TokenType.LBRACE, "{"),
        (TokenType.RBRACE, "}"),
        (TokenType.COMMA, ","),
        (TokenType.SEMICOLON, ";"),
        (TokenType.EOF,""),
    ]

    lexer = Lexer(input)

    for expected_token, expected_literal in expected:
        token = lexer.next_token()

        assert token.type == expected_token
        assert token.literal == expected_literal


def test_next_token_on_source_code():
    input = """
        let five = 5;
        let ten = 10;

        let add = fn(x, y){
            x + y;
        };

        let result = add(five, ten);
    """

    expected = [
        (TokenType.LET, "let"),
        (TokenType.IDENTIFIER, "five"),
        (TokenType.ASSIGN, "="),
        (TokenType.INT, "5"),
        (TokenType.SEMICOLON, ";"),

        (TokenType.LET, "let"),
        (TokenType.IDENTIFIER, "ten"),
        (TokenType.ASSIGN, "="),
        (TokenType.INT, "10"),
        (TokenType.SEMICOLON, ";"),

        (TokenType.LET, "let"),
        (TokenType.IDENTIFIER, "add"),
        (TokenType.ASSIGN, "="),
        (TokenType.FUNCTION, "fn"),
        (TokenType.LPAREN, "("),
        (TokenType.IDENTIFIER, "x"),
        (TokenType.COMMA, ","),
        (TokenType.IDENTIFIER, "y"),
        (TokenType.RPAREN, ")"),
        (TokenType.LBRACE, "{"),
        (TokenType.IDENTIFIER, "x"),
        (TokenType.PLUS, "+"),
        (TokenType.IDENTIFIER, "y"),
        (TokenType.SEMICOLON, ";"),
        (TokenType.RBRACE, "}"),
        (TokenType.SEMICOLON, ";"),

        (TokenType.LET, "let"),
        (TokenType.IDENTIFIER, "result"),
        (TokenType.ASSIGN, "="),
        (TokenType.IDENTIFIER, "add"),
        (TokenType.LPAREN, "("),
        (TokenType.IDENTIFIER, "five"),
        (TokenType.COMMA, ","),
        (TokenType.IDENTIFIER, "ten"),
        (TokenType.RPAREN, ")"),
        (TokenType.SEMICOLON, ";"),
        (TokenType.EOF,""),
    ]

    lexer = Lexer(input)

    for expected_token, expected_literal in expected:
        token = lexer.next_token()

        assert token.type == expected_token
        assert token.literal == expected_literal


def test_next_token_on_source_code_2():
    input = """
        !-/*5;
        5 < 10 > 5;

        if (5 < 10) {
            return true;
        } else {
            return false;
        }

        10 == 10;
        10 != 9;
    """

    expected = [
        (TokenType.BANG, "!"),
        (TokenType.MINUS, "-"),
        (TokenType.SLASH, "/"),
        (TokenType.ASTERIK, "*"),
        (TokenType.INT, "5"),
        (TokenType.SEMICOLON, ";"),

        (TokenType.INT, "5"),
        (TokenType.LT, "<"),
        (TokenType.INT, "10"),
        (TokenType.GT, ">"),
        (TokenType.INT, "5"),
        (TokenType.SEMICOLON, ";"),

        (TokenType.IF, "if"),
        (TokenType.LPAREN, "("),
        (TokenType.INT, "5"),
        (TokenType.LT, "<"),
        (TokenType.INT, "10"),
        (TokenType.RPAREN, ")"),
        (TokenType.LBRACE, "{"),
        (TokenType.RETURN, "return"),
        (TokenType.TRUE, "true"),
        (TokenType.SEMICOLON, ";"),
        (TokenType.RBRACE, "}"),
        (TokenType.ELSE, "else"),
        (TokenType.LBRACE, "{"),
        (TokenType.RETURN, "return"),
        (TokenType.FALSE, "false"),
        (TokenType.SEMICOLON, ";"),
        (TokenType.RBRACE, "}"),

        (TokenType.INT, "10"),
        (TokenType.EQ, "=="),
        (TokenType.INT, "10"),
        (TokenType.SEMICOLON, ";"),

        (TokenType.INT, "10"),
        (TokenType.NOT_EQ, "!="),
        (TokenType.INT, "9"),
        (TokenType.SEMICOLON, ";"),

        (TokenType.EOF,""),
    ]

    lexer = Lexer(input)

    for expected_token, expected_literal in expected:
        token = lexer.next_token()

        assert token.type == expected_token
        assert token.literal == expected_literal





