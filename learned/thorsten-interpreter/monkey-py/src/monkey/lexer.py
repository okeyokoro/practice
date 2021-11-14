from dataclasses import dataclass
import string


class Lexer:
    def __init__(self, input):
        def read_next_char():
            if self.peek >= len(self.input):
                self.ch = EOF
            else:
                self.ch = self.input[self.peek]

            self.position = self.peek
            self.peek += 1


        def peek_char() -> str:
            if self.peek >= len(self.input):
                return 0
            else:
                return self.input[self.peek]


        def read_identifier() -> str:
            position = self.position

            while self.ch in LETTERS:
                read_next_char()
            
            return self.input[position:self.position]


        def lookup_identifier(literal) -> TokenType:
            m = {
                "fn": TokenType.FUNCTION,
                "let": TokenType.LET,
                "true": TokenType.TRUE,
                "false": TokenType.FALSE,
                "if": TokenType.IF,
                "else": TokenType.ELSE,
                "return": TokenType.RETURN,
            }
            if literal in m:
                return m[literal]
            return TokenType.IDENTIFIER

        
        def skip_whitespace() -> None:
            while isinstance(self.ch, str) and self.ch in string.whitespace:
                read_next_char()


        def read_number() -> str:
            position = self.position
            while self.ch in string.digits:
                read_next_char()
            return self.input[position:self.position]


        def next_token() -> Token:
            skip_whitespace()

            token_for_char = {
                ";": TokenType.SEMICOLON,
                "(": TokenType.LPAREN,
                ")": TokenType.RPAREN,
                ",": TokenType.COMMA,
                "+": TokenType.PLUS,
                "{": TokenType.LBRACE,
                "}": TokenType.RBRACE,
                "<": TokenType.LT,
                ">": TokenType.GT,
                "+": TokenType.PLUS,
                "*": TokenType.ASTERIK,
                "/": TokenType.SLASH,
                "-": TokenType.MINUS,
                EOF: TokenType.EOF,
            }

            if self.ch in token_for_char:
                tok = Token(
                    type=token_for_char[self.ch],
                    literal=self.ch or "")

            elif self.ch == "=":
                if peek_char() == "=":
                    read_next_char()
                    tok = Token(
                        type=TokenType.EQ,
                        literal="==")
                else:
                    tok = Token(
                        type=TokenType.ASSIGN,
                        literal="=")

            elif self.ch == "!":
                if peek_char() == "=":
                    read_next_char()
                    tok = Token(
                        type=TokenType.NOT_EQ,
                        literal="!=")
                else:
                    tok = Token(
                        type=TokenType.BANG,
                        literal="!")

            elif self.ch in LETTERS:
                literal = read_identifier()
                token_type = lookup_identifier(literal)
                tok = Token(
                    literal=literal,
                    type=token_type)
                return tok

            elif self.ch in string.digits:
                literal = read_number()
                tok = Token(
                    type=TokenType.INT,
                    literal=literal)
                return tok

            else:
                tok = Token(
                    literal=self.ch,
                    type=TokenType.ILLEGAL)

            read_next_char()
            return tok


        EOF = 0
        LETTERS = string.ascii_letters + "_"
        
        self.input = input
        self.position = 0
        self.ch = None
        self.peek = 0

        self.next_token = next_token
        read_next_char()


class TokenType:
    ASSIGN = "="
    PLUS = "+"
    MINUS = "-"
    BANG = "!"
    ASTERIK = "*"
    SLASH = "/"
    LT = "<"
    GT = ">"
    COMMA = ","
    SEMICOLON = ";"
    LPAREN = "("
    RPAREN = ")"
    LBRACE = "{"
    RBRACE = "}"

    EQ = "=="
    NOT_EQ = "!="

    IDENTIFIER = "IDENTIFIER"
    INT = "INT"

    FUNCTION = "FUNCTION"
    LET = "LET"
    TRUE = "TRUE"
    FALSE = "FALSE"
    IF = "IF"
    ELSE = "ELSE"
    RETURN = "RETURN"

    ILLEGAL = "ILLEGAL"
    EOF = "EOF"


@dataclass
class Token:
    literal: str
    type: str

