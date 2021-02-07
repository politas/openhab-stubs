import java.lang
import java.util
import org.osgi.framework
import typing


class ComponentConstants(java.lang.Object):
    """
    Java class 'org.osgi.service.component.ComponentConstants'
    
      Attributes:
        SERVICE_COMPONENT (java.lang.String): final static field
        COMPONENT_NAME (java.lang.String): final static field
        COMPONENT_ID (java.lang.String): final static field
        COMPONENT_FACTORY (java.lang.String): final static field
        REFERENCE_TARGET_SUFFIX (java.lang.String): final static field
        DEACTIVATION_REASON_UNSPECIFIED (int): final static field
        DEACTIVATION_REASON_DISABLED (int): final static field
        DEACTIVATION_REASON_REFERENCE (int): final static field
        DEACTIVATION_REASON_CONFIGURATION_MODIFIED (int): final static field
        DEACTIVATION_REASON_CONFIGURATION_DELETED (int): final static field
        DEACTIVATION_REASON_DISPOSED (int): final static field
        DEACTIVATION_REASON_BUNDLE_STOPPED (int): final static field
        COMPONENT_CAPABILITY_NAME (java.lang.String): final static field
        COMPONENT_SPECIFICATION_VERSION (java.lang.String): final static field
    
    """
    SERVICE_COMPONENT: typing.ClassVar[java.lang.String] = ...
    COMPONENT_NAME: typing.ClassVar[java.lang.String] = ...
    COMPONENT_ID: typing.ClassVar[java.lang.String] = ...
    COMPONENT_FACTORY: typing.ClassVar[java.lang.String] = ...
    REFERENCE_TARGET_SUFFIX: typing.ClassVar[java.lang.String] = ...
    DEACTIVATION_REASON_UNSPECIFIED: typing.ClassVar[int] = ...
    DEACTIVATION_REASON_DISABLED: typing.ClassVar[int] = ...
    DEACTIVATION_REASON_REFERENCE: typing.ClassVar[int] = ...
    DEACTIVATION_REASON_CONFIGURATION_MODIFIED: typing.ClassVar[int] = ...
    DEACTIVATION_REASON_CONFIGURATION_DELETED: typing.ClassVar[int] = ...
    DEACTIVATION_REASON_DISPOSED: typing.ClassVar[int] = ...
    DEACTIVATION_REASON_BUNDLE_STOPPED: typing.ClassVar[int] = ...
    COMPONENT_CAPABILITY_NAME: typing.ClassVar[java.lang.String] = ...
    COMPONENT_SPECIFICATION_VERSION: typing.ClassVar[java.lang.String] = ...

class ComponentContext(java.lang.Object):
    """
    Java class 'org.osgi.service.component.ComponentContext'
    
    """
    def disableComponent(self, string: java.lang.String) -> None: ...
    def enableComponent(self, string: java.lang.String) -> None: ...
    def getBundleContext(self) -> org.osgi.framework.BundleContext: ...
    _getComponentInstance__S = typing.TypeVar('_getComponentInstance__S')  # <S>
    def getComponentInstance(self) -> 'ComponentInstance'[_getComponentInstance__S]: ...
    def getProperties(self) -> java.util.Dictionary[java.lang.String, typing.Any]: ...
    def getServiceReference(self) -> org.osgi.framework.ServiceReference[typing.Any]: ...
    def getUsingBundle(self) -> org.osgi.framework.Bundle: ...
    _locateService_0__S = typing.TypeVar('_locateService_0__S')  # <S>
    @typing.overload
    def locateService(self, string: java.lang.String) -> _locateService_0__S: ...
    _locateService_1__S = typing.TypeVar('_locateService_1__S')  # <S>
    @typing.overload
    def locateService(self, string: java.lang.String, serviceReference: org.osgi.framework.ServiceReference[_locateService_1__S]) -> _locateService_1__S: ...
    def locateServices(self, string: java.lang.String) -> typing.List[typing.Any]: ...

class ComponentException(java.lang.RuntimeException):
    """
    Java class 'org.osgi.service.component.ComponentException'
    
        Extends:
            java.lang.RuntimeException
    
      Constructors:
        * ComponentException(java.lang.Throwable)
        * ComponentException(java.lang.String)
        * ComponentException(java.lang.String, java.lang.Throwable)
    
    """
    @typing.overload
    def __init__(self, string: java.lang.String): ...
    @typing.overload
    def __init__(self, string: java.lang.String, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...
    def getCause(self) -> java.lang.Throwable: ...
    def initCause(self, throwable: java.lang.Throwable) -> java.lang.Throwable: ...

_ComponentFactory__S = typing.TypeVar('_ComponentFactory__S')  # <S>
class ComponentFactory(java.lang.Object, typing.Generic[_ComponentFactory__S]):
    """
    Java class 'org.osgi.service.component.ComponentFactory'
    
    """
    def newInstance(self, dictionary: java.util.Dictionary[java.lang.String, typing.Any]) -> 'ComponentInstance'[_ComponentFactory__S]: ...

_ComponentInstance__S = typing.TypeVar('_ComponentInstance__S')  # <S>
class ComponentInstance(java.lang.Object, typing.Generic[_ComponentInstance__S]):
    """
    Java class 'org.osgi.service.component.ComponentInstance'
    
    """
    def dispose(self) -> None: ...
    def getInstance(self) -> _ComponentInstance__S: ...

_ComponentServiceObjects__S = typing.TypeVar('_ComponentServiceObjects__S')  # <S>
class ComponentServiceObjects(java.lang.Object, typing.Generic[_ComponentServiceObjects__S]):
    """
    Java class 'org.osgi.service.component.ComponentServiceObjects'
    
    """
    def getService(self) -> _ComponentServiceObjects__S: ...
    def getServiceReference(self) -> org.osgi.framework.ServiceReference[_ComponentServiceObjects__S]: ...
    def ungetService(self, s2: _ComponentServiceObjects__S) -> None: ...