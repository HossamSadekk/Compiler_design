from importlib._common import _

from sly import Lexer
from sly import Parser

class lex(Lexer):

    tokens = {NUMBER,ID,WHILE,IF,FOR,ELSE,PLUS,MINUS,DIVIDE,TIMES,PRINT,ASSIGN,EQ,GE,GT,LE,NE,LT,LPAREN,RPAREN}
    literals = {')','(','{','}',';'}

    ignore = ' \t'  # ignore any space
    ignore_Comments = '\#.*'
    MINUS = r'-'
    TIMES = r'\*'
    PLUS = r'\+'
    ASSIGN = r'='
    DIVIDE = r'/'
    LE = r'<='
    LT = r'<'
    GT = r'>'
    GE = r'>='
    NE = r'!='
    EQ = r'=='
    LPAREN = r'\('
    RPAREN = r'\)'

    @_(r'\d+')
    def NUMBER(self,t):
        t.value = int(t.value)
        return t

    # Identifier and keywords
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['for']=FOR
    ID['if']=IF
    ID['while']=WHILE
    ID['else']=ELSE
    ID['print'] = PRINT

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print('line %d: bad character %r' %(self.lineno, t.value[0]))
        self.index+=1

class Myparser(Parser):
    # Get the token list
    tokens = lex.tokens

    @_('expr PLUS term')
    def expr(self,P):
        return P.expr+P.term

    @_('expr MINUS term')
    def expr(self, P):
        return P.expr - P.term

    @_('expr TIMES term')
    def expr(self, P):
        return P.expr * P.term

    @_('term')
    def expr(self, P):
        return P.term

    @_('term TIMES factor')
    def term(self, P):
        return P.term * P.factor

    @_('term DIVIDE factor')
    def term(self, P):
        return P.term / P.factor

    @_('factor')
    def term(self, P):
        return P.factor

    @_('NUMBER')
    def factor(self, P):
        return P.NUMBER

    @_('LPAREN expr RPAREN')
    def factor(self, P):
        return P.expr


if __name__ == '__main__':
    output_lexer = lex()
    parser = Myparser()

    while True:
        try:
            text = input('source code:')
            result = parser.parse(output_lexer.tokenize(text))
            print(result)
        except EOFError:
            break



