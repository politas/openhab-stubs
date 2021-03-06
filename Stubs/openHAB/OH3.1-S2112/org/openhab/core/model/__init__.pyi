import com.google.inject
import java.lang
import org.eclipse.xtext
import org.eclipse.xtext.conversion
import org.eclipse.xtext.generator
import org.eclipse.xtext.naming
import org.eclipse.xtext.parser
import org.eclipse.xtext.parser.antlr
import org.eclipse.xtext.scoping
import org.eclipse.xtext.serializer
import org.eclipse.xtext.serializer.sequencer
import org.eclipse.xtext.service
import org.openhab.core.model.parser.antlr.internal
import org.openhab.core.model.validation
import typing


class AbstractItemsRuntimeModule(org.eclipse.xtext.service.DefaultRuntimeModule):
    """
    Java class 'org.openhab.core.model.AbstractItemsRuntimeModule'
    
        Extends:
            org.eclipse.xtext.service.DefaultRuntimeModule
    
      Constructors:
        * AbstractItemsRuntimeModule()
    
    """
    def __init__(self): ...
    def bindClassLoaderToInstance(self) -> java.lang.ClassLoader: ...
    def bindIAntlrTokenFileProvider(self) -> typing.Type[org.eclipse.xtext.parser.antlr.IAntlrTokenFileProvider]: ...
    def bindIGenerator2(self) -> typing.Type[org.eclipse.xtext.generator.IGenerator2]: ...
    def bindIGlobalScopeProvider(self) -> typing.Type[org.eclipse.xtext.scoping.IGlobalScopeProvider]: ...
    def bindIGrammarAccess(self) -> typing.Type[org.eclipse.xtext.IGrammarAccess]: ...
    def bindIParser(self) -> typing.Type[org.eclipse.xtext.parser.IParser]: ...
    def bindIQualifiedNameProvider(self) -> typing.Type[org.eclipse.xtext.naming.IQualifiedNameProvider]: ...
    def bindIScopeProvider(self) -> typing.Type[org.eclipse.xtext.scoping.IScopeProvider]: ...
    def bindISemanticSequencer(self) -> typing.Type[org.eclipse.xtext.serializer.sequencer.ISemanticSequencer]: ...
    def bindISerializer(self) -> typing.Type[org.eclipse.xtext.serializer.ISerializer]: ...
    def bindISyntacticSequencer(self) -> typing.Type[org.eclipse.xtext.serializer.sequencer.ISyntacticSequencer]: ...
    def bindITokenDefProvider(self) -> typing.Type[org.eclipse.xtext.parser.antlr.ITokenDefProvider]: ...
    def bindITokenToStringConverter(self) -> typing.Type[org.eclipse.xtext.parser.ITokenToStringConverter]: ...
    def bindItemsValidator(self) -> typing.Type[org.openhab.core.model.validation.ItemsValidator]: ...
    def bindLexer(self) -> typing.Type[org.eclipse.xtext.parser.antlr.Lexer]: ...
    def configure(self, binder: com.google.inject.Binder) -> None: ...
    def configureFileExtensions(self, binder: com.google.inject.Binder) -> None: ...
    def configureIResourceDescriptions(self, binder: com.google.inject.Binder) -> None: ...
    def configureIResourceDescriptionsPersisted(self, binder: com.google.inject.Binder) -> None: ...
    def configureIScopeProviderDelegate(self, binder: com.google.inject.Binder) -> None: ...
    def configureIgnoreCaseLinking(self, binder: com.google.inject.Binder) -> None: ...
    def configureLanguageName(self, binder: com.google.inject.Binder) -> None: ...
    def configureRuntimeLexer(self, binder: com.google.inject.Binder) -> None: ...
    def provideInternalItemsLexer(self) -> com.google.inject.Provider[org.openhab.core.model.parser.antlr.internal.InternalItemsLexer]: ...

class ItemsStandaloneSetupGenerated(org.eclipse.xtext.ISetup):
    """
    Java class 'org.openhab.core.model.ItemsStandaloneSetupGenerated'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.eclipse.xtext.ISetup
    
      Constructors:
        * ItemsStandaloneSetupGenerated()
    
    """
    def __init__(self): ...
    def createInjector(self) -> com.google.inject.Injector: ...
    def createInjectorAndDoEMFRegistration(self) -> com.google.inject.Injector: ...
    def register(self, injector: com.google.inject.Injector) -> None: ...

class ItemsRuntimeModule(AbstractItemsRuntimeModule):
    """
    Java class 'org.openhab.core.model.ItemsRuntimeModule'
    
        Extends:
            org.openhab.core.model.AbstractItemsRuntimeModule
    
      Constructors:
        * ItemsRuntimeModule()
    
    """
    def __init__(self): ...
    def bindIValueConverterService(self) -> typing.Type[org.eclipse.xtext.conversion.IValueConverterService]: ...
    def configureUseIndexFragmentsForLazyLinking(self, binder: com.google.inject.Binder) -> None: ...

class ItemsStandaloneSetup(ItemsStandaloneSetupGenerated):
    """
    Java class 'org.openhab.core.model.ItemsStandaloneSetup'
    
        Extends:
            org.openhab.core.model.ItemsStandaloneSetupGenerated
    
      Constructors:
        * ItemsStandaloneSetup()
    
    """
    def __init__(self): ...
    @classmethod
    def doSetup(cls) -> None: ...
    @classmethod
    def unregister(cls) -> None: ...
