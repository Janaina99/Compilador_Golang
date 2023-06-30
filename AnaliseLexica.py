import ply.lex as lex

def space_counter(token):
  spaces = 0
  for c in token.value:
    if c == ' ':
      spaces += 1
    elif c == '\t':
      spaces += 8 - (spaces % 8)
  return spaces


reservadas = {
  'float': 'FLOAT',
  'int': 'INT',
  'bool': 'BOOL',
  'string': 'STRING',
  'break': 'BREAK',
  'func': 'FUNC',
  'interface': 'INTERFACE',
  'case': 'CASE',
  'go': 'GO',
  'goto': 'GOTO',
  'defer': 'DEFER',
  'map': 'MAP',
  'struct': 'STRUCT',
  'chan': 'CHAN',
  'else': 'ELSE',
  'package': 'PACKAGE',
  'switch': 'SWITCH',
  'const': 'CONST',
  'fallthrough': 'FALLTHROUGH',
  'if': 'IF',
  'range': 'RANGE',
  'type': 'TYPE',
  'continue': 'CONTINUE',
  'for': 'FOR',
  'import': 'IMPORT',
  'return': 'RETURN',
  'var': 'VAR',
  'default': 'DEFAULT',
  'nil': 'NULL',
  'true': 'TRUE',
  'false': 'FALSE'
}

tokens = [
  'SOMA', 'SUBTRACAO', 'ASTERISCO', 'DIVISAO', 'ID', 'INTEIRO', 'FLUTUANTE', 
  'IGUAL', 'DIFERENTE', 'MAIORQUE', 'MENORQUE', 'MAIORIGUAL',
  'MENORIGUAL', 'CONJUNCAO', 'MODULO', 'DISJUNCAO', 'ATRIBUICAO',
  'ATRIBUICAOSOMA', 'ATRIBUICAOMULT', 'ATRIBUICAOSUB', 'ATRIBUICAODIV',
  'ATRIBUICAOMOD', 'ATRIBUICAOPONTO', 'LPAREN', 'RPAREN', 'LCHAVE', 'RCHAVE',
  'LCOLCHETE', 'RCOLCHETE', 'VIRGULA', 'PVIRGULA', 'PONTO', 'DOISPONTOS',
  'PALAVRA', 'COMENTARIO', 'ENDERECO', 'LINHA', 'IDENT', 'DEDENT'
] + list(reservadas.values())

t_SOMA = r'\+'
t_SUBTRACAO = r'-'
t_ASTERISCO = r'\*'
t_DIVISAO = r'/'
t_MODULO = r'%'
t_IGUAL = r'=='
t_DIFERENTE = r'!='
t_MAIORQUE = r'>'
t_MENORQUE = r'<'
t_MAIORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_ENDERECO = r'&'
t_CONJUNCAO = r'&&'
t_DISJUNCAO = r'\|\|'
t_ATRIBUICAO = r'='
t_ATRIBUICAOSOMA = r'\+='
t_ATRIBUICAOSUB = r'-='
t_ATRIBUICAOMULT = r'\*='
t_ATRIBUICAODIV = r'/='
t_ATRIBUICAOMOD = r'%='
t_ATRIBUICAOPONTO = r':='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCHAVE = r'{'
t_RCHAVE = r'}'
t_LCOLCHETE = r'\['
t_RCOLCHETE = r'\]'
t_VIRGULA = r','
t_PVIRGULA = r';'
t_PONTO = r'\.'
t_DOISPONTOS = r':'
t_PALAVRA = r'"(.*?)"'
t_ignore = ' '

stack = [0]
states = (
  ('idstate', 'exclusive'),
  ('dedstate', 'exclusive'),
)
t_LINHA = '[a-zA-Z][a-zA-Z \t]+'


def t_breakline(t):
  r'\n+'  #Reconhece uma ou mais quebras de linha
  t.lexer.lineno += len(t.value)
  t.lexer.begin('idstate')


def t_idstate_blankline(t):
  r'([ \t]+)\n'  #Reconhece uma linha em branco
  pass


def t_idstate_linewithcode(t):
  '([ \t]+) | ([a-zA-Z{}])'  #Reconhece espaços em brancos e tabulações ou uma palavra
  # print('t_idstate_linewithcode')
  n_spaces = space_counter(t)
  t.lexer.begin('INITIAL')
  if n_spaces < stack[-1]:
    t.lexer.skip(-len(t.value))
    stack.pop()
    t.type = 'DEDENT'
    t.lexer.begin('dedstate')
  elif n_spaces > stack[-1]:
    stack.append(n_spaces)
    t.type = 'IDENT'
  elif n_spaces == 0:
    t.lexer.skip(-1)


def t_dedstate_linewithdedent(t):
  '([ \t]+) | ([a-zA-Z{}])'  #Reconhece espaços em brancos e tabulações ou uma palavra
  n_spaces = space_counter(t)
  if n_spaces < stack[-1]:
    t.lexer.skip(-len(t.value))
    stack.pop()
    t.type = 'DEDENT'
  elif n_spaces >= stack[-1]:
    t.lexer.begin('INITIAL')
    if n_spaces > stack[-1]:
      print('Erro de dedentação --->', n_spaces)
    elif n_spaces == 0:  # Se o elemento começar com uma palavra
      t.lexer.skip(-1)

def t_error(t):
  print("ERROR in INITIAL state")
  print(t.value)
  t.lexer.skip(1)

def t_idstate_error(t):
  print("ERROR in idstate state")
  t.lexer.skip(1)

def t_dedstate_error(t):
  print("ERROR in dedstate state")
  t.lexer.skip(1)

def t_FLUTUANTE(t):
  r'[-]?[0-9]+[.][0-9]+'
  t.value = float(t.value)
  return t

def t_INTEIRO(t):
  r'[-]?[0-9]+'
  t.value = int(t.value)
  return t

def t_ID(t):
  r'[_]{0,}[a-zA-Z][a-zA-Z0-9_]*'
  t.type = reservadas.get(t.value, 'ID')
  return t

def t_COMENTARIO(t):
  r'(//.*)|(/\*(.|\n)*?\*/)'
  pass

lexer = lex.lex()
lexer.input(
  'func mais(a int, b int) int {\n a += 5;  return a + b;\n}\nfunc main() {\n if 5 > 6{ shift := 9;}  res += mais(1, 2);\n   Println("1+2=", res);\nfor j := 7; j <= 9; j=j+1 {\nPrintln(j);\n}}'
)
