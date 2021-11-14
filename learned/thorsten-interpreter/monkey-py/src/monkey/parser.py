from typing import List
from dataclasses import dataclass
from monkey.lexer import *


class Parser:
    def __init__(self, lexer:Lexer) -> None:
        self.lexer = lexer
        self.current_token = None
        self.peek_token = None

        def next_token(self,):
            self.current_token = self.peek_token
            self.peek_token = self.lexer.next_token()

        next_token()
        next_token()

        def parse_program(self,) -> Program:
            return None


class Node:
    def TokenLiteral(self) -> str:
        ...

class Statement(Node):
    def statementNode(self):
        ...

class Expression(Node):
    def expressionNode(self):
        ...


class Program(Node): # root node of ast
    def __init__(self):
        self.statements: List[Statement]

    def TokenLiteral(self):
        if self.statements:
            return self.statements[0].TokenLiteral()
        return ""


class Identifier(Expression):
    def __init__(self, token:Token, value:str):
        self.token = token
        self.value = value

    def expressionNode():
        pass

    def TokenLiteral(self) -> str:
        return self.token.literal


class LetStatement(Statement):
    def __init__(self, token:Token, name: Identifier, value: Expression):
        self.token = token
        self.name = name
        self.value = value

    def statementNode():
        pass

    def TokenLiteral(self) -> str:
        return self.token.literal






