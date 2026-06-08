# faisallang/parser.py

from faisallang.ast import (
    Program,
    Number,
    String,
    Variable,
    VariableDeclaration,
    PrintStatement,
)


class Parser:
    """
    Parser أولي لـ FSL.
    يدعم حالياً:
      - دع x = 10
      - اطبع x
      - اطبع 123
    """

    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def current(self):
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return None

    def advance(self):
        self.position += 1

    def parse(self):
        statements = []

        while self.current() is not None:
            stmt = self.parse_statement()

            if stmt:
                statements.append(stmt)
            else:
                self.advance()

        return Program(statements)

    def parse_statement(self):

        token = self.current()

        if token is None:
            return None

        token_type = token["type"]

        if token_type == "VAR_DECL":
            return self.parse_variable_declaration()

        if token_type == "PRINT":
            return self.parse_print()

        return None

    def parse_variable_declaration(self):

        self.advance()  # دع

        name_token = self.current()

        if not name_token or name_token["type"] != "IDENTIFIER":
            raise SyntaxError("Expected variable name")

        var_name = name_token["value"]

        self.advance()

        assign_token = self.current()

        if not assign_token or assign_token["type"] != "ASSIGN":
            raise SyntaxError("Expected '='")

        self.advance()

        value = self.parse_expression()

        return VariableDeclaration(var_name, value)

    def parse_print(self):

        self.advance()  # اطبع

        expr = self.parse_expression()

        return PrintStatement(expr)

    def parse_expression(self):

        token = self.current()

        if token is None:
            raise SyntaxError("Unexpected end of input")

        if token["type"] == "NUMBER":
            self.advance()
            return Number(token["value"])

        if token["type"] == "STRING":
            self.advance()
            return String(token["value"])

        if token["type"] == "IDENTIFIER":
            self.advance()
            return Variable(token["value"])

        raise SyntaxError(f"Unexpected token: {token}")
