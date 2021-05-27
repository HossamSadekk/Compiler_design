from importlib._common import _

from sly import Lexer

class lex(Lexer):

    tokens = {NUMBER,ID,WHILE,IF,FOR,ELSE,PLUS,MINUS,DIVIDE,TIMES,PRINT,ASSIGN,EQ,GE,GT,LE,NE,LT}
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

if __name__ == '__main__':
    source_code = '''
    # comment
    i=0
    while(i<10)
    {
    print
    ?
    i=i+1
    }
    '''
    output = lex()
    for token in output.tokenize(source_code):
        print(token)
