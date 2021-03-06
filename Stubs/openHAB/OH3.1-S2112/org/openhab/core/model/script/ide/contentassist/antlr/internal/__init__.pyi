import java.lang
import org.antlr.runtime
import org.eclipse.xtext.ide.editor.contentassist.antlr.internal
import typing


class InternalScriptLexer(org.eclipse.xtext.ide.editor.contentassist.antlr.internal.Lexer):
    """
    Java class 'org.openhab.core.model.script.ide.contentassist.antlr.internal.InternalScriptLexer'
    
        Extends:
            org.eclipse.xtext.ide.editor.contentassist.antlr.internal.Lexer
    
      Constructors:
        * InternalScriptLexer(org.antlr.runtime.CharStream)
        * InternalScriptLexer()
        * InternalScriptLexer(org.antlr.runtime.CharStream, org.antlr.runtime.RecognizerSharedState)
    
      Attributes:
        RULE_HEX (int): final static field
        T__50 (int): final static field
        T__59 (int): final static field
        T__55 (int): final static field
        T__56 (int): final static field
        T__57 (int): final static field
        T__58 (int): final static field
        T__51 (int): final static field
        T__52 (int): final static field
        T__53 (int): final static field
        T__54 (int): final static field
        T__60 (int): final static field
        T__61 (int): final static field
        RULE_ID (int): final static field
        RULE_INT (int): final static field
        T__66 (int): final static field
        RULE_ML_COMMENT (int): final static field
        T__67 (int): final static field
        T__68 (int): final static field
        T__69 (int): final static field
        T__62 (int): final static field
        T__63 (int): final static field
        T__64 (int): final static field
        T__65 (int): final static field
        T__37 (int): final static field
        T__38 (int): final static field
        T__39 (int): final static field
        T__33 (int): final static field
        T__34 (int): final static field
        T__35 (int): final static field
        T__36 (int): final static field
        T__30 (int): final static field
        T__31 (int): final static field
        T__32 (int): final static field
        T__48 (int): final static field
        T__49 (int): final static field
        T__44 (int): final static field
        T__45 (int): final static field
        T__46 (int): final static field
        T__47 (int): final static field
        T__40 (int): final static field
        T__41 (int): final static field
        T__42 (int): final static field
        T__43 (int): final static field
        T__91 (int): final static field
        T__92 (int): final static field
        T__93 (int): final static field
        T__90 (int): final static field
        T__19 (int): final static field
        T__15 (int): final static field
        T__16 (int): final static field
        T__17 (int): final static field
        T__18 (int): final static field
        T__13 (int): final static field
        T__14 (int): final static field
        RULE_DECIMAL (int): final static field
        T__26 (int): final static field
        T__27 (int): final static field
        T__28 (int): final static field
        T__29 (int): final static field
        T__22 (int): final static field
        T__23 (int): final static field
        T__24 (int): final static field
        T__25 (int): final static field
        T__20 (int): final static field
        T__21 (int): final static field
        T__70 (int): final static field
        T__71 (int): final static field
        T__72 (int): final static field
        RULE_STRING (int): final static field
        RULE_SL_COMMENT (int): final static field
        T__77 (int): final static field
        T__78 (int): final static field
        T__79 (int): final static field
        T__73 (int): final static field
        EOF (int): final static field
        T__74 (int): final static field
        T__75 (int): final static field
        T__76 (int): final static field
        T__80 (int): final static field
        T__81 (int): final static field
        T__82 (int): final static field
        T__83 (int): final static field
        RULE_WS (int): final static field
        RULE_ANY_OTHER (int): final static field
        T__88 (int): final static field
        T__89 (int): final static field
        T__84 (int): final static field
        T__85 (int): final static field
        T__86 (int): final static field
        T__87 (int): final static field
    
    """
    RULE_HEX: typing.ClassVar[int] = ...
    T__50: typing.ClassVar[int] = ...
    T__59: typing.ClassVar[int] = ...
    T__55: typing.ClassVar[int] = ...
    T__56: typing.ClassVar[int] = ...
    T__57: typing.ClassVar[int] = ...
    T__58: typing.ClassVar[int] = ...
    T__51: typing.ClassVar[int] = ...
    T__52: typing.ClassVar[int] = ...
    T__53: typing.ClassVar[int] = ...
    T__54: typing.ClassVar[int] = ...
    T__60: typing.ClassVar[int] = ...
    T__61: typing.ClassVar[int] = ...
    RULE_ID: typing.ClassVar[int] = ...
    RULE_INT: typing.ClassVar[int] = ...
    T__66: typing.ClassVar[int] = ...
    RULE_ML_COMMENT: typing.ClassVar[int] = ...
    T__67: typing.ClassVar[int] = ...
    T__68: typing.ClassVar[int] = ...
    T__69: typing.ClassVar[int] = ...
    T__62: typing.ClassVar[int] = ...
    T__63: typing.ClassVar[int] = ...
    T__64: typing.ClassVar[int] = ...
    T__65: typing.ClassVar[int] = ...
    T__37: typing.ClassVar[int] = ...
    T__38: typing.ClassVar[int] = ...
    T__39: typing.ClassVar[int] = ...
    T__33: typing.ClassVar[int] = ...
    T__34: typing.ClassVar[int] = ...
    T__35: typing.ClassVar[int] = ...
    T__36: typing.ClassVar[int] = ...
    T__30: typing.ClassVar[int] = ...
    T__31: typing.ClassVar[int] = ...
    T__32: typing.ClassVar[int] = ...
    T__48: typing.ClassVar[int] = ...
    T__49: typing.ClassVar[int] = ...
    T__44: typing.ClassVar[int] = ...
    T__45: typing.ClassVar[int] = ...
    T__46: typing.ClassVar[int] = ...
    T__47: typing.ClassVar[int] = ...
    T__40: typing.ClassVar[int] = ...
    T__41: typing.ClassVar[int] = ...
    T__42: typing.ClassVar[int] = ...
    T__43: typing.ClassVar[int] = ...
    T__91: typing.ClassVar[int] = ...
    T__92: typing.ClassVar[int] = ...
    T__93: typing.ClassVar[int] = ...
    T__90: typing.ClassVar[int] = ...
    T__19: typing.ClassVar[int] = ...
    T__15: typing.ClassVar[int] = ...
    T__16: typing.ClassVar[int] = ...
    T__17: typing.ClassVar[int] = ...
    T__18: typing.ClassVar[int] = ...
    T__13: typing.ClassVar[int] = ...
    T__14: typing.ClassVar[int] = ...
    RULE_DECIMAL: typing.ClassVar[int] = ...
    T__26: typing.ClassVar[int] = ...
    T__27: typing.ClassVar[int] = ...
    T__28: typing.ClassVar[int] = ...
    T__29: typing.ClassVar[int] = ...
    T__22: typing.ClassVar[int] = ...
    T__23: typing.ClassVar[int] = ...
    T__24: typing.ClassVar[int] = ...
    T__25: typing.ClassVar[int] = ...
    T__20: typing.ClassVar[int] = ...
    T__21: typing.ClassVar[int] = ...
    T__70: typing.ClassVar[int] = ...
    T__71: typing.ClassVar[int] = ...
    T__72: typing.ClassVar[int] = ...
    RULE_STRING: typing.ClassVar[int] = ...
    RULE_SL_COMMENT: typing.ClassVar[int] = ...
    T__77: typing.ClassVar[int] = ...
    T__78: typing.ClassVar[int] = ...
    T__79: typing.ClassVar[int] = ...
    T__73: typing.ClassVar[int] = ...
    EOF: typing.ClassVar[int] = ...
    T__74: typing.ClassVar[int] = ...
    T__75: typing.ClassVar[int] = ...
    T__76: typing.ClassVar[int] = ...
    T__80: typing.ClassVar[int] = ...
    T__81: typing.ClassVar[int] = ...
    T__82: typing.ClassVar[int] = ...
    T__83: typing.ClassVar[int] = ...
    RULE_WS: typing.ClassVar[int] = ...
    RULE_ANY_OTHER: typing.ClassVar[int] = ...
    T__88: typing.ClassVar[int] = ...
    T__89: typing.ClassVar[int] = ...
    T__84: typing.ClassVar[int] = ...
    T__85: typing.ClassVar[int] = ...
    T__86: typing.ClassVar[int] = ...
    T__87: typing.ClassVar[int] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, input: org.antlr.runtime.CharStream): ...
    @typing.overload
    def __init__(self, input: org.antlr.runtime.CharStream, state: org.antlr.runtime.RecognizerSharedState): ...
    def getGrammarFileName(self) -> java.lang.String: ...
    def mRULE_ANY_OTHER(self) -> None: ...
    def mRULE_DECIMAL(self) -> None: ...
    def mRULE_HEX(self) -> None: ...
    def mRULE_ID(self) -> None: ...
    def mRULE_INT(self) -> None: ...
    def mRULE_ML_COMMENT(self) -> None: ...
    def mRULE_SL_COMMENT(self) -> None: ...
    def mRULE_STRING(self) -> None: ...
    def mRULE_WS(self) -> None: ...
    def mT__13(self) -> None: ...
    def mT__14(self) -> None: ...
    def mT__15(self) -> None: ...
    def mT__16(self) -> None: ...
    def mT__17(self) -> None: ...
    def mT__18(self) -> None: ...
    def mT__19(self) -> None: ...
    def mT__20(self) -> None: ...
    def mT__21(self) -> None: ...
    def mT__22(self) -> None: ...
    def mT__23(self) -> None: ...
    def mT__24(self) -> None: ...
    def mT__25(self) -> None: ...
    def mT__26(self) -> None: ...
    def mT__27(self) -> None: ...
    def mT__28(self) -> None: ...
    def mT__29(self) -> None: ...
    def mT__30(self) -> None: ...
    def mT__31(self) -> None: ...
    def mT__32(self) -> None: ...
    def mT__33(self) -> None: ...
    def mT__34(self) -> None: ...
    def mT__35(self) -> None: ...
    def mT__36(self) -> None: ...
    def mT__37(self) -> None: ...
    def mT__38(self) -> None: ...
    def mT__39(self) -> None: ...
    def mT__40(self) -> None: ...
    def mT__41(self) -> None: ...
    def mT__42(self) -> None: ...
    def mT__43(self) -> None: ...
    def mT__44(self) -> None: ...
    def mT__45(self) -> None: ...
    def mT__46(self) -> None: ...
    def mT__47(self) -> None: ...
    def mT__48(self) -> None: ...
    def mT__49(self) -> None: ...
    def mT__50(self) -> None: ...
    def mT__51(self) -> None: ...
    def mT__52(self) -> None: ...
    def mT__53(self) -> None: ...
    def mT__54(self) -> None: ...
    def mT__55(self) -> None: ...
    def mT__56(self) -> None: ...
    def mT__57(self) -> None: ...
    def mT__58(self) -> None: ...
    def mT__59(self) -> None: ...
    def mT__60(self) -> None: ...
    def mT__61(self) -> None: ...
    def mT__62(self) -> None: ...
    def mT__63(self) -> None: ...
    def mT__64(self) -> None: ...
    def mT__65(self) -> None: ...
    def mT__66(self) -> None: ...
    def mT__67(self) -> None: ...
    def mT__68(self) -> None: ...
    def mT__69(self) -> None: ...
    def mT__70(self) -> None: ...
    def mT__71(self) -> None: ...
    def mT__72(self) -> None: ...
    def mT__73(self) -> None: ...
    def mT__74(self) -> None: ...
    def mT__75(self) -> None: ...
    def mT__76(self) -> None: ...
    def mT__77(self) -> None: ...
    def mT__78(self) -> None: ...
    def mT__79(self) -> None: ...
    def mT__80(self) -> None: ...
    def mT__81(self) -> None: ...
    def mT__82(self) -> None: ...
    def mT__83(self) -> None: ...
    def mT__84(self) -> None: ...
    def mT__85(self) -> None: ...
    def mT__86(self) -> None: ...
    def mT__87(self) -> None: ...
    def mT__88(self) -> None: ...
    def mT__89(self) -> None: ...
    def mT__90(self) -> None: ...
    def mT__91(self) -> None: ...
    def mT__92(self) -> None: ...
    def mT__93(self) -> None: ...
    def mTokens(self) -> None: ...
