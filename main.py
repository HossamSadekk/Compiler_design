from sly import Lexer

class lex(Lexer):

    tokens = { ID, NUMBER, PLUS, MINUS, TIMES, DIVIDE, ASSIGN, LPAREN, RPAREN }
    ignore = ' \t'
    # regular express rules
    # Dictionary describe the token
    ID     = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER = r'\d+'
    PLUS   = r'\+'
    MINUS  = r'-'
    TIMES  = r'\*'
    DIVIDE = r'/'
    ASSIGN = r'='
    LPAREN = r'\('
    RPAREN = r'\)'

if __name__ == '__main__':
    source_code = 'z = 5 + 6 * ( A - B )'
    output_lexer = lex()
    for T in output_lexer.tokenize(source_code):
      print('type=%r, value=%r' % (T.type, T.value))
