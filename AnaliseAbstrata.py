from abc import abstractmethod
from abc import ABCMeta

class Programa(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass 

class ProgramaConcreto1(Programa):
  def __init__(self, declaration):
    self.declaration = declaration

  def accept(self, visitor):
    return visitor.visitProgramaConcreto1(self) 

class ProgramaConcreto2(Programa):
  def __init__(self, programa, declaration):
    self.programa = programa
    self.declaration = declaration

  def accept(self, visitor):
    return visitor.visitProgramaConcreto2(self) 
    
class Declaration(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class DeclarationConcreto1(Declaration):
  def __init__(self, declarationvar):
    self.declarationvar = declarationvar

  def accept(self, visitor):
    return visitor.visitDeclarationConcreto1(self)

class DeclarationConcreto2(Declaration):
  def __init__(self, declarationfunc):
    self.declarationfunc = declarationfunc

  def accept(self, visitor):
    return visitor.visitDeclarationConcreto2(self)

class DelarationVar(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class DeclaraVar(Declaration):
  def __init__(self, declara):
    self.declarationvar = declara

  def accept(self, visitor):
    return visitor.visitDeclaraVar(self)

class DeclaraVar2(Declaration):
  def __init__(self, declara):
    self.declarationvar = declara

  def accept(self, visitor):
    return visitor.visitDeclaraVar2(self)
    

class DeclaraExpBinaria(Declaration):
  def __init__(self, id, expbinaria):
    self.id = id
    self.expbinaria = expbinaria
    
  def accept(self, visitor):
    return visitor.visitDeclaraExpBinaria(self)

class Declara(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class DeclaraIdTipo(Declara):
  def __init__(self, tipo):
    self.tipo = tipo
    
  def accept(self, visitor):
    return visitor.visitDeclaraIdTipo(self)

class DeclaraIdTipoExpBinaria(Declara):
  def __init__(self, tipo, expbinaria):
    self.id = id
    self.expbinaria = expbinaria
    
  def accept(self, visitor):
    return visitor.visitDeclaraIdTipoExp(self)

class DeclarationFunc(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class DeclarationFuncConcreta(DeclarationFunc):
  def __init__(self, id, assinatura, corpo):
    self.id = id
    self.assinatura = assinatura
    self.corpo = corpo
    
  def accept(self, visitor):
    return visitor.visitDeclarationFuncConcreta(self)

class Assinatura(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class AssinaturaListparam(Assinatura):
  def __init__(self, listaParam, tipo):
    self.listaParam = listaParam
    self.tipo = tipo
    
  def accept(self, visitor):
    return visitor.visitAssinaturaListParam(self)

class ListaParam(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class ListaParamIdTipo(ListaParam):
  def __init__(self, id, tipo):
    self.id = id
    self.tipo = tipo
    
  def accept(self, visitor):
    return visitor.visitListaParamIdTipo(self)

class ListaParamPvId(ListaParam):
  def __init__(self, listaParam, id, tipo):
    self.listaParam = listaParam
    self.id = id
    self.tipo = tipo
    
  def accept(self, visitor):
    return visitor.visitListaParamPvId(self)

class Corpo(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class CorpoConcreto(Corpo):
  def __init__(self, stms):
    self.stms = stms
    
  def accept(self, visitor):
    return visitor.visitCorpoConcreto(self)

class Stms(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class StmsConcreto(Stms):
  def __init__(self, stm, stms):
    self.stm = stm
    self.stms = stms
    
  def accept(self, visitor):
    return visitor.visitStmsConcreto(self)

class Stm(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass
    
class StmListaExp(Stm):
  def __init__(self, listaExp):
    self.listaExp = listaExp
    
  def accept(self, visitor):
    return visitor.visitStmListaExp(self)

class StmDeclarationVar(Stm):
  def __init__(self, declarationVar):
    self.declarationVar = declarationVar
    
  def accept(self, visitor):
    return visitor.visitStmDeclarationVar(self)


class StmDeclarationShort(Stm):
  def __init__(self, declarationVarShort):
    self.declarationVarShort = declarationVarShort
    
  def accept(self, visitor):
    return visitor.visitStmDeclarationShort(self)

class StmIfstm(Stm):
  def __init__(self, ifStm):
    self.ifStm = ifStm
    
  def accept(self, visitor):
    return visitor.visitStmIfstm(self)

class StmForstm(Stm):
  def __init__(self, forStm):
    self.forStm = forStm
    
  def accept(self, visitor):
    return visitor.visitStmForstm(self)

class StmReturnstm(Stm):
  def __init__(self, returnStm):
    self.returnStm = returnStm
    
  def accept(self, visitor):
    return visitor.visitStmReturnstm(self)

class ReturnStm(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class Return(ReturnStm):
  def __init__(self, expBinaria):
    self.expBinaria = expBinaria
    
  def accept(self, visitor):
    return visitor.visitReturn(self)

class DeclarationVarShort(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class DeclaraShort(DeclarationVarShort):
  def __init__(self, id, expBinaria):
    self.id = id
    self.expBinaria = expBinaria
    
  def accept(self, visitor):
    return visitor.visitDeclaraShort(self)

class IfStm(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class IfListaExp(IfStm):
  def __init__(self, listaExp, corpo, ifStm2):
    self.listaExp = listaExp
    self.corpo = corpo
    self.ifStm2 = ifStm2
    
  def accept(self, visitor):
    return visitor.visitIfListaExp(self)

class IfStm2(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class IfListaExp2(IfStm2):
  def __init__(self, corpo):
    self.corpo = corpo
    
  def accept(self, visitor):
    return visitor.visitIfListaExp2(self)

class ForStm(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class ForCorpo(ForStm):
  def __init__(self, listaExp, corpo):
    self.listaExp = listaExp
    self.corpo = corpo
    
  def accept(self, visitor):
    return visitor.visitForCorpo(self)

class ForListaExp(ForStm):
  def __init__(self, listaExp1, listaExp2, listaExp3, corpo):
    self.listaExp1 = listaExp1
    self.listaExp2 = listaExp2
    self.listaExp3 = listaExp3
    self.corpo = corpo
    
  def accept(self, visitor):
    return visitor.visitForListaExp(self)

class tipo(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class tipoArray(tipo):
  def __init__(self, array):
    self.array = array

  def accept(self, visitor):
    return visitor.visitTipoArray(self)

class tipoInt(tipo):
  def __init__(self, intTipo):
    self.intTipo = intTipo

  def accept(self, visitor):
    return visitor.visitTipoInt(self)

class tipoFloat(tipo):
  def __init__(self, floatTipo):
    self.floatTipo = floatTipo

  def accept(self, visitor):
    return visitor.visitTipoFloat(self)

class tipoBool(tipo):
  def __init__(self, boolTipo):
    self.boolTipo = boolTipo

  def accept(self, visitor):
    return visitor.visitTipoBool(self)

class tipoString(tipo):
  def __init__(self, stringTipo):
    self.stringTipo = stringTipo

  def accept(self, visitor):
    return visitor.visitTipoString(self)

class Array(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class ArraySimples(Array):
  def __init__(self, listaExp, tipo):
    self.listaExp = listaExp
    self.tipo = tipo
    
  def accept(self, visitor):
    return visitor.visitArraySimples(self)

class ArrayComposto(Array):
  def __init__(self, listaExp, tipo, params):
    self.listaExp = listaExp
    self.tipo = tipo
    self.params = params 
    
  def accept(self, visitor):
    return visitor.visitArrayComposto(self)

class ListaExp(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class ListaExpBinaria(ListaExp):
  def __init__(self, expBinaria):
    self.expBinaria = expBinaria
    
  def accept(self, visitor):
    return visitor.visitListaExpBinaria(self)

class ListaExpAtribui(ListaExp):
  def __init__(self, expAtribui):
    self.expAtribui = expAtribui
    
  def accept(self, visitor):
    return visitor.visitListaExpAtribui(self)

class ExpBinaria(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class AbreExpBinariaTerminalFecha(ExpBinaria):
  def __init__(self, terminal, operadorBinario, expBinaria):
    self.terminal = terminal
    self.operadorBinario = operadorBinario
    self.expBinaria = expBinaria
    
  def accept(self, visitor):
    return visitor.visitAbreExpBinariaTerminalFecha(self)

class ExpBinariaTerminal(ExpBinaria):
  def __init__(self, terminal, operadorBinario, expBinaria):
    self.terminal = terminal
    self.operadorBinario = operadorBinario
    self.expBinaria = expBinaria
    
  def accept(self, visitor):
    return visitor.visitExpBinariaTerminal(self)

class ExpBinariaApenasTerminal(ExpBinaria):
  def __init__(self, terminal):
    self.terminal = terminal
    
  def accept(self, visitor):
    return visitor.visitExpBinariaApenasTerminal(self)

class ExpBinariaCall(ExpBinaria):
  def __init__(self, call):
    self.call = call
    
  def accept(self, visitor):
    return visitor.visitExpBinariaCall(self)

class ExpAtribui(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class ExpAtribuiConcreta(ExpAtribui):
  def __init__(self, id, operadorAtribui, expBinaria):
    self.id = id
    self.operadorAtribui = operadorAtribui
    self.expBinaria = expBinaria
    
  def accept(self, visitor):
    return visitor.visitExpAtribuiConcreta(self)

class operadorAtribuicao(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class atribuicao(operadorAtribuicao):
  def __init__(self, atribuicao):
    self.atribuicao = atribuicao

  def accept(self, visitor):
    return visitor.visitAtribuicao(self)

class atribuicaoSoma(operadorAtribuicao):
  def __init__(self, atribuicaoSoma):
    self.atribuicaoSoma = atribuicaoSoma

  def accept(self, visitor):
    return visitor.visitAtribuicaoSoma(self)

class atribuicaoSub(operadorAtribuicao):
  def __init__(self, atribuicaoSub):
    self.atribuicaoSub = atribuicaoSub

  def accept(self, visitor):
    return visitor.visitAtribuicaoSub(self)

class atribuicaoMul(operadorAtribuicao):
  def __init__(self, atribuicaoMul):
    self.atribuicaoMul = atribuicaoMul

  def accept(self, visitor):
    return visitor.visitAtribuicaoMul(self)
    
class atribuicaoDiv(operadorAtribuicao):
  def __init__(self, atribuicaoDiv):
    self.atribuicaoDiv = atribuicaoDiv

  def accept(self, visitor):
    return visitor.visitAtribuicaoDiv(self)

class atribuicaoMod(operadorAtribuicao):
  def __init__(self, atribuicaoMod):
    self.atribuicaoMod = atribuicaoMod

  def accept(self, visitor):
    return visitor.visitAtribuicaoMod(self)

class atribuicaoPonto(operadorAtribuicao):
  def __init__(self, atribuicaoPonto):
    self.atribuicaoPonto = atribuicaoPonto

  def accept(self, visitor):
    return visitor.visitAtribuicaoPonto(self)

class operadorBinario(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class operadorSoma(operadorBinario):
  def __init__(self, soma):
    self.soma = soma

  def accept(self, visitor):
    return visitor.visitOperadorSoma(self)

class operadorAsterisco(operadorBinario):
  def __init__(self, asterisco):
    self.asterisco = asterisco

  def accept(self, visitor):
    return visitor.visitOperadorAsterisco(self)

class operadorModulo(operadorBinario):
  def __init__(self, mod):
    self.mod = mod

  def accept(self, visitor):
    return visitor.visitOperadorModulo(self)

class operadorDivisao(operadorBinario):
  def __init__(self, div):
    self.div = div

  def accept(self, visitor):
    return visitor.visitOperadorDiv(self)

class operadorSubtracao(operadorBinario):
  def __init__(self, sub):
    self.sub = sub

  def accept(self, visitor):
    return visitor.visitOperadorSub(self)

class operadorMaiorQue(operadorBinario):
  def __init__(self, maior):
    self.maior = maior

  def accept(self, visitor):
    return visitor.visitOperadorMaior(self)

class operadorMenorQue(operadorBinario):
  def __init__(self, menor):
    self.menor = menor

  def accept(self, visitor):
    return visitor.visitOperadorMenor(self)

class operadorMaiorIgual(operadorBinario):
  def __init__(self, maiorigual):
    self.maiorigual = maiorigual

  def accept(self, visitor):
    return visitor.visitOperadorMaiorIgual(self)

class operadorMenorIgual(operadorBinario):
  def __init__(self, menorigual):
    self.menorigual = menorigual

  def accept(self, visitor):
    return visitor.visitOperadorMenorIgual(self)

class operadorIgual(operadorBinario):
  def __init__(self, igual):
    self.igual = igual

  def accept(self, visitor):
    return visitor.visitOperadorIgual(self)

class operadorDiferente(operadorBinario):
  def __init__(self, dif):
    self.dif = dif

  def accept(self, visitor):
    return visitor.visitOperadorDif(self)

class operadorConjuncao(operadorBinario):
  def __init__(self, conj):
    self.conj = conj

  def accept(self, visitor):
    return visitor.visitOperadorConj(self)

class operadorDisjuncao(operadorBinario):
  def __init__(self, dis):
    self.dis = dis

  def accept(self, visitor):
    return visitor.visitOperadorDis(self)

class terminal(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class terminalInt(terminal):
  def __init__(self, intValue):
    self.intValue = intValue
  def accept(self, visitor):
    return visitor.visitTerminalInt(self)

class terminalFloat(terminal):
  def __init__(self, floatValue):
    self.floatValue = floatValue
  def accept(self, visitor):
    return visitor.visitTerminalFloat(self)

class terminalID(terminal):
  def __init__(self, id):
    self.id = id
  def accept(self, visitor):
    return visitor.visitTerminalID(self)

class terminalString(terminal):
  def __init__(self, stringValue):
    self.stringValue = stringValue
  def accept(self, visitor):
    return visitor.visitTerminalString(self)

class terminalBool(terminal):
  def __init__(self, boolValue):
    self.boolValue = boolValue
  def accept(self, visitor):
    return visitor.visitTerminalBool(self)

class Call(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class CallId(Call):
  def __init__(self, id, params):
    self.id = id
    self.params = params
    
  def accept(self, visitor):
    return visitor.visitCallId(self)

class Params(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class ParamsLista(Params):
  def __init__(self, listaexp):
    self.listaexp = listaexp
    
  def accept(self, visitor):
    return visitor.visitParamsLista(self)

class ParamsListaParams(Params):
  def __init__(self, listaexp, params):
    self.listaexp = listaexp
    self.params = params
    
  def accept(self, visitor):
    return visitor.visitParamsListaParams(self)