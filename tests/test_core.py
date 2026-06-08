from compiler.lexer import Lexer


def test_lexer():

    code = "اطبع 10"

    lexer = Lexer(code)

    tokens = lexer.tokenize()

    assert len(tokens) > 0
