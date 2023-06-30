from abc import abstractmethod, ABCMeta

class AbstractVisitor(metaclass = ABCMeta):
  
  @abstractmethod
  def visitProgramaConcreto1(self, programa):pass
    
  @abstractmethod
  def visitProgramaConcreto2(self, programa):pass

  @abstractmethod
  def visitDeclaraVar(self, DeclaraVar):pass

  @abstractmethod
  def visitDeclaraVar2(self, DeclaraVar):pass 
    
  @abstractmethod
  def visitDeclaraExpBinaria(self, DeclaraExpBinaria):pass

  @abstractmethod
  def visitDeclaraIdTipo(self, DeclaraIdTipo):pass

  @abstractmethod
  def visitDeclaraIdTipoExp(self, DeclaraIdTipoExp):pass

  @abstractmethod
  def visitDeclarationFuncConcreta(self, DeclarationFunc):pass
    
  @abstractmethod
  def visitAssinaturaListParam(self, AssinaturaListParam):pass

  @abstractmethod
  def visitListaParamIdTipo(self, ListaParamIdTipo):pass

  @abstractmethod
  def visitListaParamPvId(self, ListaParamPvId):pass

  @abstractmethod
  def visitCorpoConcreto(self, CorpoConcreto):pass

  @abstractmethod
  def visitStmsConcreto(self, StmsConcreto):pass

  @abstractmethod
  def visitStmListaExp(self, StmListaExp):pass

  @abstractmethod
  def visitStmDeclarationVar(self, StmDeclarationVar):pass

  @abstractmethod
  def visitStmDeclarationShort(self, StmDeclarationShort):pass

  @abstractmethod
  def visitStmIfstm(self, StmIf):pass

  @abstractmethod
  def visitStmForstm(self, StmFor):pass

  @abstractmethod
  def visitStmReturnstm(self, StmReturn):pass

  @abstractmethod
  def visitReturn(self, returnStm):pass

  @abstractmethod
  def visitDeclaraShort(self, declaraShort):pass

  @abstractmethod
  def visitIfListaExp(self, ifLista):pass

  @abstractmethod
  def visitIfListaExp2(self, ifLista2):pass

  @abstractmethod
  def visitForCorpo(self, forCorpo):pass

  @abstractmethod
  def visitForListaExp(self, forListaExp):pass

  @abstractmethod
  def visitTipoArray(self, tipoArray):pass

  @abstractmethod
  def visitTipoInt(self, tipo):pass

  @abstractmethod
  def visitTipoFloat(self, tipo):pass
    
  @abstractmethod
  def visitTipoBool(self, tipo):pass

  @abstractmethod
  def visitTipoString(self, tipo):pass

  @abstractmethod
  def visitArraySimples(self, array):pass

  @abstractmethod
  def visitArrayComposto(self, array):pass

  @abstractmethod
  def visitListaExpBinaria(self, listaExp):pass

  @abstractmethod
  def visitListaExpAtribui(self, listaExp):pass

  @abstractmethod
  def visitAbreExpBinariaTerminalFecha(self, args):pass

  @abstractmethod
  def visitExpBinariaTerminal(self, args):pass

  @abstractmethod
  def visitExpBinariaApenasTerminal(self, arg):pass

  @abstractmethod
  def visitExpBinariaCall(self, ExpBinariaCall):pass

  @abstractmethod
  def visitExpAtribuiConcreta(self, ExpAtribuiConcreta):pass
    
  @abstractmethod
  def visitAtribuicao(self, Atribuicao):pass

  @abstractmethod
  def visitAtribuicaoSoma(self, AtribuicaoSoma):pass

  @abstractmethod
  def visitAtribuicaoSub(self, AtibuicaoSub):pass

  @abstractmethod
  def visitAtribuicaoMul(self, AtribuiMul):pass

  @abstractmethod
  def visitAtribuicaoDiv(self, AtribuicaoDiv):pass

  @abstractmethod
  def visitAtribuicaoMod(self, AtribuicaoMod):pass

  @abstractmethod
  def visitAtribuicaoPonto(self, AtribuicaoPonto):pass

  @abstractmethod
  def visitOperadorSoma(self, OperadorSoma):pass

  @abstractmethod
  def visitOperadorAsterisco(self, OperadorAsterisco):pass

  @abstractmethod
  def visitOperadorModulo(self, OperadorModulo):pass

  @abstractmethod
  def visitOperadorDiv(self, OperadorDiv):pass

  @abstractmethod
  def visitOperadorSub(self, OperadorSub):pass

  @abstractmethod
  def visitOperadorMaior(self, OperadorMaior):pass

  @abstractmethod
  def visitOperadorMenor(self, OperadorMenor):pass

  @abstractmethod
  def visitOperadorMaiorIgual(self, OperadorMenorIgual):pass

  @abstractmethod
  def visitOperadorMenorIgual(self, OperadorMenorIgual):pass

  @abstractmethod
  def visitOperadorIgual(self, OperadorIgual):pass

  @abstractmethod
  def visitOperadorDif(self, OperadorDif):pass

  @abstractmethod
  def visitOperadorConj(self, OperadorConj):pass

  @abstractmethod
  def visitOperadorDis(self, OperadorDis):pass

  @abstractmethod
  def visitTerminalInt(self, TerminalInt):pass

  @abstractmethod
  def visitTerminalFloat(self, TerminalFloat):pass

  @abstractmethod
  def visitTerminalID(self, TerminalID):pass

  @abstractmethod
  def visitTerminalString(self, TerminalString):pass

  @abstractmethod
  def visitTerminalBool(self, TerminalBool):pass

  @abstractmethod
  def visitCallId(self, CallId):pass

  @abstractmethod
  def visitParamsLista(self, ParamsLista):pass

  @abstractmethod
  def visitParamsListaParams(self, ParamsListaParams):pass