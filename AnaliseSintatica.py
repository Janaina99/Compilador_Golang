import ply.yacc as yacc
from AnaliseLexica import *
import AnaliseAbstrata as sa

precedence = (
  ('left', 'CONJUNCAO', 'DISJUNCAO', 'DIFERENTE'),
  ('nonassoc', 'MAIORQUE', 'MENORQUE', 'IGUAL', 'MAIORIGUAL', 'MENORIGUAL', 'MODULO'),
  ('left', 'ATRIBUICAO', 'ATRIBUICAOSOMA', 'ATRIBUICAOSUB', 'ATRIBUICAOMULT', 'ATRIBUICAODIV', 'ATRIBUICAOMOD', 'ATRIBUICAOPONTO'),
  ('left', 'SOMA', 'SUBTRACAO'),
  ('left', 'ASTERISCO', 'DIVISAO'),
  ('left', 'LPAREN', 'RPAREN')
)

def p_programa(p):
  '''programa : declaration 
              | programa declaration'''
  if (len(p) == 2):
    p[0] = sa.ProgramaConcreto1(p[1])
  else:
    p[0] = sa.ProgramaConcreto2(p[1], p[2])
  
def p_declaration(p):
  '''declaration : declarationvar PVIRGULA 
                 | declarationfunc'''
  if len(p) == 3:
    p[0] = sa.DeclarationConcreto1(p[1])
  else:
    p[0] = sa.DeclarationConcreto2(p[1])
  
def p_declarationvar(p):
  '''declarationvar : VAR declara 
                    | CONST declara 
                    | ID ATRIBUICAO expbinaria'''
  if (len(p) == 4):
    p[0] = sa.DeclaraExpBinaria(p[1], p[3])
  elif (p[1] == 'var'):
    p[0] = sa.DeclaraVar(p[2])
  else:
    p[0] = sa.DeclaraVar2(p[2])

def p_declara(p):
  '''declara : ID tipo 
             | ID tipo ATRIBUICAO expbinaria'''
  if (len(p) == 3):
    p[0] = sa.DeclaraIdTipo(p[1], p[2])
  else:
    p[0] = sa.DeclaraIdTipoExpBinaria(p[1], p[2], p[4])
  
def p_declarationfunc(p):
  '''declarationfunc : FUNC ID assinatura corpo'''
  p[0] = sa.DeclarationFuncConcreta(p[2], p[3], p[4])
  
def p_assinatura(p):
  '''assinatura : LPAREN listaparam RPAREN tipo
                | LPAREN listaparam RPAREN
                | LPAREN RPAREN tipo
                | LPAREN RPAREN'''
  if (len(p) == 3):
    p[0] = sa.AssinaturaListparam(None, None)
  elif (len(p) == 5):
    p[0] = sa.AssinaturaListparam(p[2], p[4])
  elif p[2]==')':
    p[0] = sa.AssinaturaListparam(None, p[3])
  else:
    p[0] = sa.AssinaturaListparam(p[2], None)
    
def p_listaparam(p):
  '''listaparam : ID tipo 
                | listaparam VIRGULA ID tipo'''
  if (len(p)==3):
    p[0] = sa.ListaParamIdTipo(p[1], p[2])
  else:
    p[0] = sa.ListaParamPvId(p[1], p[3], p[4])
  
def p_corpo(p):
  '''corpo : LCHAVE stms RCHAVE'''
  p[0] = sa.CorpoConcreto(p[2])
  
def p_stms(p):
  '''stms : stm 
          | stm stms'''
  if (len(p) == 2):
    p[0] = sa.StmsConcreto(p[1], None)
  else:
    p[0] = sa.StmsConcreto(p[1], p[2])
  
def p_stm(p):
  '''stm : listaexp PVIRGULA'''
  p[0] = sa.StmListaExp(p[1])
def p_stm2(p):
  '''stm : declarationvar PVIRGULA'''
  p[0] = sa.StmDeclarationVar(p[1])
def p_stm3(p):
  '''stm : declarationvarshort PVIRGULA'''
  p[0] = sa.StmDeclarationShort(p[1])
def p_stm4(p):
  '''stm : ifstm'''
  p[0] = sa.StmIfstm(p[1])
def p_stm5(p):
  '''stm : forstm'''
  p[0] = sa.StmForstm(p[1])
def p_stm6(p):
  '''stm : returnstm'''
  p[0] = sa.StmReturnstm(p[1])

def p_returnstm(p):
  '''returnstm : RETURN PVIRGULA 
               | RETURN expbinaria PVIRGULA'''
  if (len(p) == 3):
    p[0] = sa.Return(None)
  else:
    p[0] = sa.Return(p[2])
  
def p_declarationvarshort(p):
  '''declarationvarshort : ID ATRIBUICAOPONTO expbinaria'''
  p[0] = sa.DeclaraShort(p[3])
  
def p_ifstm(p):
  '''ifstm : IF listaexp corpo ifstm2'''
  p[0] = sa.IfListaExp(p[2], p[3], p[4])

def p_ifstm2(p):
  '''ifstm2 : ELSE corpo 
            |'''
  if (len(p) == 3):
    p[0] = sa.IfListaExp2(p[2])
  else:
    p[0] = sa.IfListaExp2(None)

def p_forstm(p):
  '''forstm : FOR corpo 
            | FOR listaexp corpo 
            | FOR listaexp PVIRGULA listaexp PVIRGULA listaexp corpo'''
  if(len(p) == 3):
    p[0] = sa.ForCorpo(None, p[2])
  elif(len(p) == 4):
    p[0] = sa.ForCorpo(p[2], p[3])
  else:
    p[0] = sa.ForListaExp(p[2], p[4], p[6], p[7])
  
def p_tipo(p):
  '''tipo : array 
          | INT 
          | FLOAT 
          | BOOL 
          | STRING'''
  if(p[1] == 'array'):
    p[0] = sa.tipoArray(p[1])
  elif(p[1] == 'int'):
    p[0] = sa.tipoInt(p[1])
  elif(p[1] == 'float'):
    p[0] = sa.tipoFloat(p[1])
  elif(p[1] == 'bool'):
    p[0] = sa.tipoBool(p[1])
  else:
    p[0] = sa.tipoString(p[1])

def p_array(p):
  '''array : LCOLCHETE listaexp RCOLCHETE tipo LCHAVE params RCHAVE PVIRGULA
           | LCOLCHETE listaexp RCOLCHETE tipo PVIRGULA
           | LCOLCHETE listaexp RCOLCHETE PVIRGULA'''
  if(len(p) == 5):
    p[0] = sa.ArraySimples(p[2], None)
  elif(len(p) == 6):
    p[0] = sa.ArraySimples(p[2], p[4])
  else:
    p[0] = sa.ArrayComposto(p[2], p[4], p[6])
  
def p_listaexp(p):
  '''listaexp : expbinaria 
              | expatribui'''
  if (isinstance(p[1], sa.ExpBinaria)):
    p[0] = sa.ListaExpBinaria(p[1])
  else:
    p[0] = sa.ListaExpAtribui(p[1])

def p_expbinaria(p):
  '''expbinaria : LPAREN terminal operadorbinario expbinaria RPAREN
                | terminal operadorbinario expbinaria 
                | call
                | terminal'''
  if(len(p) == 6):
    p[0] = sa.AbreExpBinariaTerminalFecha(p[2], p[3], p[4])
  elif(len(p) == 4):
    p[0] = sa.ExpBinariaTerminal(p[1], p[2], p[3])
  elif(isinstance(p[1], sa.Call)):
    p[0] = sa.ExpBinariaCall(p[1])
  else:
    p[0] = sa.ExpBinariaApenasTerminal(p[1])
  
def p_expatribui(p):
  '''expatribui :  ID operadoratribuicao expbinaria'''
  p[0] = sa.ExpAtribuiConcreta(p[1], p[2], p[3])

def p_operadoratribuicao(p):
  '''operadoratribuicao : ATRIBUICAO 
                        | ATRIBUICAOSOMA 
                        | ATRIBUICAOSUB 
                        | ATRIBUICAOMULT 
                        | ATRIBUICAODIV 
                        | ATRIBUICAOMOD 
                        | ATRIBUICAOPONTO'''
  if(p[1] == '='):
    p[0] = sa.atribuicao(p[1])
  elif(p[1] == '+='):
    p[0] = sa.atribuicaoSoma(p[1])
  elif(p[1] == '-='):
    p[0] = sa.atribuicaoSub(p[1])
  elif(p[1] == '*='):
    p[0] = sa.atribuicaoMul(p[1])
  elif(p[1] == '/='):
    p[0] = sa.atribuicaoDiv(p[1])
  elif(p[1] == '%='):
    p[0] = sa.atribuicaoMod(p[1])
  else:
    p[0] = sa.atribuicaoPonto(p[1])

def p_operadorbinario(p): 
  '''operadorbinario : SOMA
                     | ASTERISCO 
                     | MODULO 
                     | DIVISAO 
                     | SUBTRACAO 
                     | MAIORQUE 
                     | MENORQUE 
                     | MAIORIGUAL 
                     | MENORIGUAL 
                     | IGUAL 
                     | DIFERENTE 
                     | CONJUNCAO 
                     | DISJUNCAO'''
  if(p[1] == '+'):
    p[0] = sa.operadorSoma(p[1])
  elif(p[1] == '*'):
    p[0] = sa.operadorAsterisco(p[1])
  elif(p[1] == '%'):
    p[0] = sa.operadorModulo(p[1])
  elif(p[1] == '/'):
    p[0] = sa.operadorDivisao(p[1])
  elif(p[1] == '-'):
    p[0] = sa.operadorSubtracao(p[1])
  elif(p[1] == '>'):
    p[0] = sa.operadorMaiorQue(p[1])
  elif(p[1] == '<'):
    p[0] = sa.operadorMenorQue(p[1])
  elif(p[1] == '>='):
    p[0] = sa.operadorMaiorIgual(p[1])
  elif(p[1] == '<='):
    p[0] = sa.operadorMenorIgual(p[1])
  elif(p[1] == '=='):
    p[0] = sa.operadorIgual(p[1])
  elif(p[1] == '!='):
    p[0] = sa.operadorDiferente(p[1])
  elif(p[1] == '&&'):
    p[0] = sa.operadorConjuncao(p[1])
  else:
    p[0] = sa.operadorDisjuncao(p[1])

def p_terminal(p):
  '''terminal : INTEIRO 
              | FLUTUANTE 
              | ID 
              | PALAVRA 
              | TRUE 
              | FALSE'''
  
  if(isinstance(p[1], int)):
    p[0] = sa.terminalInt(p[1])
  elif(isinstance(p[1], float)):
    p[0] = sa.terminalFloat(p[1])
  elif(isinstance(p[1], str) and p[1][0] == '"'):
    p[0] = sa.terminalString(p[1])
  elif(p[1] == 'true' or p[1] == 'false'):
    p[0] = sa.terminalBool(p[1])
  else:
    p[0] = sa.terminalID(p[1])
       
def p_call(p):
  '''call : ID LPAREN params RPAREN 
          | ID LPAREN RPAREN'''
  if(len(p) == 5):
    p[0] = sa.CallId(p[1], p[3])
  else:
    p[0] = sa.CallId(p[1], None)

def p_params(p):
  '''params : listaexp VIRGULA params 
            | listaexp''' 
  if(len(p) == 4):
    p[0] = sa.ParamsListaParams(p[1], p[3])
  else:
    p[0] = sa.ParamsLista(p[1])

def p_error(p):
    print("Syntax error in input!", p.value)