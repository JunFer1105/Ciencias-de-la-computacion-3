import ply.lex as lex

tokens = [ 'NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE', 'EQUALS','CICLO','CONDICIONAL','MENOR','MAYOR','IGUAL','DIFERENTE','MENOR_IGUAL','MAYOR_IGUAL', 'CONSECUENCIA']

t_ignore = ' \t\n'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r':='
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
#AGREGADO
t_MENOR=r'<'
t_MENOR_IGUAL=r'<='
t_MAYOR=r'>'
t_MAYOR_IGUAL=r'>='
t_IGUAL=r'=='
t_DIFERENTE=r'!='



def t_FOR(t):
	r'\PARA+'	
	if t.value=="PARA":
		t.type="CICLO"
	return t
	
def t_ENTONCES(t):
	r'\ENTONCES+'	
	if t.value=="ENTONCES":
		t.type="CONSECUENCIA"
	return t	
	
def t_SI(t):
	r'\SI+'	
	if t.value=="SI":
		t.type="CONDICIONAL"
	return t	

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer


cadena=open("algo.txt","r").readlines()
for i in cadena:
	lex.input(i)
	
	while True:
		tok = lex.token()
		if not tok: break
		print str(tok.value) + " - " + str(tok.type)



