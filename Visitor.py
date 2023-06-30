from abstractVisitor import AbstractVisitor
#from AnaliseSintatica import *

class Visitor(AbstractVisitor):
  def  visitProgramaConcreto1(self, programa):
    programa.declaration.accept(self)

  def visitProgramaConcreto2(self, prog):
    prog.programa.accept(self)
    prog.declaration.accept(self)
    
  def visitDeclarationConcreto1(self, DeclarationConcreto1):
    DeclarationConcreto1.declarationvar.accept(self)
    print(';', end='', sep='')

  def visitDeclarationConcreto2(self, DeclarationConcreto2):
    DeclarationConcreto2.declarationfunc.accept(self)

  #Como diferenciar o CONST e o VAR? Precisa fazer um abs pra cada?
  def visitDeclaraVar(self, DeclaraVar):
    print('var', end='', sep='')
    DeclaraVar.declarationvar.accept(self)

  def visitDeclaraVar2(self, DeclaraVar):
    print('const', end='', sep='')
    DeclaraVar.declarationvar.accept(self)

  def visitDeclaraExpBinaria(self, DeclaraExpBinaria):
    print(DeclaraExpBinaria.id, end='', sep='')
    print('=', end='', sep='')
    DeclaraExpBinaria.expbinaria.accept(self)

  def visitDeclaraIdTipo(self, DeclaraIdTipo):
    print(DeclaraIdTipo.id, end='', sep='')
    DeclaraIdTipo.tipo.accept(self)

  def visitDeclaraIdTipoExp(self, DeclaraIdTipoExp):
    print(DeclaraIdTipoExp.id, end='', sep='')
    DeclaraIdTipoExp.tipo.accept(self)
    print('=', end='', sep='')
    DeclaraIdTipoExp.expbinaria.accept(self)

  def visitDeclarationFuncConcreta(self, DeclarationFunc):
    print('FUNC', end='', sep='')
    print(DeclarationFunc.id, end='', sep='')
    DeclarationFunc.assinatura.accept(self)
    DeclarationFunc.corpo.accept(self)

  def visitAssinaturaListParam(self, AssinaturaListParam):
    print('(', end='', sep='')
    if(AssinaturaListParam.listaParam is not None):
      AssinaturaListParam.listaParam.accept(self)
    print(')', end='', sep='')
    if(AssinaturaListParam.listaParam is not None):
      AssinaturaListParam.tipo.accept(self)

  def visitListaParamIdTipo(self, ListaParamIdTipo):
    print(ListaParamIdTipo.id, end='', sep='')
    ListaParamIdTipo.tipo.accept(self)

  def visitListaParamPvId(self, ListaParamPvId):
    ListaParamPvId.listaParam.accept(self)
    print(',', end='', sep='')
    
    print(ListaParamPvId.id, end='', sep='')
    ListaParamPvId.tipo.accept(self)    

  def visitCorpoConcreto(self, CorpoConcreto):
    print('{', end='', sep='')
    CorpoConcreto.stms.accept(self)
    print('}', end='', sep='')

  def visitStmsConcreto(self, StmsConcreto):
    StmsConcreto.stm.accept(self)
    if(StmsConcreto.stms is not None):
      StmsConcreto.stms.accept(self)

  def visitStmListaExp(self, StmListaExp):
    StmListaExp.listaExp.accept(self)
    print(';', end='', sep='')

  def visitStmDeclarationVar(self, StmDeclarationVar):
    StmDeclarationVar.declarationVar.accept(self)
    print(';', end='', sep='')

  def visitStmDeclarationShort(self, StmDeclarationShort):
    StmDeclarationShort.declarationVarShort.accept(self)
    print(';', end='', sep='')

  def visitStmIfstm(self, StmIf):
    StmIf.ifStm.accept(self)

  def visitStmForstm(self, StmFor):
    StmFor.forStm.accept(self)

  def visitStmReturnstm(self, StmReturn):
    StmReturn.returnStm.accept(self)

  def visitReturn(self, returnStm):
    print('return', end='', sep='')
    if(returnStm.expBinaria is not None):
      returnStm.expBinaria.accept(self)
    print(';', end='', sep='')

  def visitDeclaraShort(self, declaraShort):
    print(declaraShort.id, end='', sep='')
    print(':=', end='', sep='')
    declaraShort.expBinaria.accept(self)

  def visitIfListaExp(self, ifLista):
    print('if', end='', sep='')
    ifLista.listaExp.accept(self)
    ifLista.corpo.accept(self)
    ifLista.ifStm2.accept(self)

  def visitIfListaExp2(self, ifLista2):
    print('else', end='', sep='')
    if(ifLista2.corpo is not None):
      ifLista2.corpo.accept(self)

  def visitForCorpo(self, forCorpo):
    print('for', end='', sep='')
    if(forCorpo.listaExp is not None):
      forCorpo.listaExp.accept(self)
    forCorpo.corpo.accept(self)

  def visitForListaExp(self, forListaExp):
    print('for', end='', sep='')
    forListaExp.listaExp1.accept(self)
    print(';', end='', sep='')
    forListaExp.listaExp2.accept(self)
    print(';', end='', sep='')
    forListaExp.listaExp3.accept(self)
    forListaExp.corpo.accept(self)

  def visitTipoArray(self, tipoArray):
    tipoArray.array.accept(self)

  #Não usa o argumento, preciso receber mesmo assim??
  def visitTipoInt(self, tipo):
    print('int', end='', sep='')

  def visitTipoFloat(self, tipo):
    print('float', end='', sep='')

  def visitTipoBool(self, tipo):
    print('bool', end='', sep='')

  def visitTipoString(self, tipo):
    print('string', end='', sep='')

  def visitArraySimples(self, array):
    print('[', end='', sep='')
    array.listaExp.accept(self)
    print(']', end='', sep='')
    if (array.tipo is not None):
      array.tipo.accept(self)
    print(';', end='', sep='')

  def visitArrayComposto(self, array):
    print('[', end='', sep='')
    array.listaExp.accept(self)
    print(']', end='', sep='')
    array.tipo.accept(self)
    print('{', end='', sep='')
    array.params.accept(self)
    print('}', end='', sep='')
    print(';', end='', sep='')

  def visitListaExpBinaria(self, listaExp):
    listaExp.expBinaria.accept(self)

  def visitListaExpAtribui(self, listaExp):
    listaExp.expAtribui.accept(self)

  def visitAbreExpBinariaTerminalFecha(self, args):
    print('(', end='', sep='')
    args.terminal.accept(self)
    args.operadorBinario.accept(self)
    args.expBinaria.accept(self)
    print(')', end='', sep='')

  def visitExpBinariaTerminal(self, args):
    args.terminal.accept(self)
    args.operadorBinario.accept(self)
    args.expBinaria.accept(self)

  def visitExpBinariaApenasTerminal(self, arg):
    arg.terminal.accept(self)

  def visitExpBinariaCall(self, ExpBinariaCall):
    ExpBinariaCall.call.accept(self)

  #Coloquei até aqui

  def visitExpAtribuiConcreta(self, expAtribuiConcreta):
    print(expAtribuiConcreta.id, end='', sep='')
    expAtribuiConcreta.operadorAtribui.accept(self)
    expAtribuiConcreta.expBinaria.accept(self)

  def visitAtribuicao(self, atr):
    print('=', end='', sep='')

  def visitAtribuicaoSoma(self, atr):
    print('+=', end='', sep='')

  def visitAtribuicaoSub(self, atr):
    print('-=', end='', sep='')

  def visitAtribuicaoMul(self, atr):
    print('*=', end='', sep='')

  def visitAtribuicaoDiv(self, atr):
    print('/=', end='', sep='')

  def visitAtribuicaoMod(self, atr):
    print('%=', end='', sep='')

  def visitAtribuicaoPonto(self, atr):
    print(':=', end='', sep='')

  def visitOperadorSoma(self, soma):
    print('+', end='', sep='')

  def visitOperadorAsterisco(self, ast):
    print('*', end='', sep='')

  def visitOperadorModulo(self, mod):
    print('%', end='', sep='')

  def visitOperadorDiv(self, div):
    print('/', end='', sep='')

  def visitOperadorSub(self, sub):
    print('-', end='', sep='')

  def visitOperadorMaior(self, maior):
    print('>', end='', sep='')

  def visitOperadorMenor(self, menor):
    print('<', end='', sep='')

  def visitOperadorMaiorIgual(self, maiorI):
    print('>=', end='', sep='')

  def visitOperadorMenorIgual(self, menorI):
    print('<=', end='', sep='')

  def visitOperadorIgual(self, igual):
    print('==', end='', sep='')

  def visitOperadorDif(self, dif):
    print('!=', end='', sep='')

  def visitOperadorConj(self, conj):
    print('&&', end='', sep='')

  def visitOperadorDis(self, dis):
    print('||', end='', sep='')

  def visitTerminalInt(self, term):
    print(term.intValue, end='', sep='')

  def visitTerminalFloat(self, term):
    print(term.floatValue, end='', sep='')

  def visitTerminalID(self, term):
    print(term.id, end='', sep='')

  def visitTerminalString(self, term):
    print(term.stringValue, end='', sep='')

  def visitTerminalBool(self, term):
    print(term.boolValue, end='', sep='')

  def visitCallId(self, callID):
    print(callID.id, end='', sep='')
    print('(', end='', sep='')
    if(callID.params is not None):
      callID.params.accept(self)
    print(')', end='', sep='')

  def visitParamsLista(self, paramsLista):
    paramsLista.listaexp.accept(self)

  def visitParamsListaParams(self, paramsLista):
    paramsLista.listaexp.accept(self)
    print(';', end='', sep='')
    paramsLista.params.accept(self)
  