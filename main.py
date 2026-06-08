from compiler.lexer import Lexer
from compiler.parser import Parser
from compiler.interpreter import Interpreter

# برنامج بسيط بلغة FaisalLang
code = "دع س = 10"

# 1. التقطيع إلى رموز
lexer = Lexer(code)
tokens = lexer.tokenize()

# 2. بناء الهيكل (AST)
parser = Parser(tokens)
ast = parser.parse()

# 3. التنفيذ
interpreter = Interpreter(ast)
interpreter.run()
