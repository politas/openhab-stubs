import java.io
import java.lang
import java.util
import org.slf4j.spi
import typing


class ILoggerFactory(java.lang.Object):
    """
    Java class 'org.slf4j.ILoggerFactory'
    
    """
    def getLogger(self, string: java.lang.String) -> 'Logger': ...

class IMarkerFactory(java.lang.Object):
    """
    Java class 'org.slf4j.IMarkerFactory'
    
    """
    def detachMarker(self, string: java.lang.String) -> bool: ...
    def exists(self, string: java.lang.String) -> bool: ...
    def getDetachedMarker(self, string: java.lang.String) -> 'Marker': ...
    def getMarker(self, string: java.lang.String) -> 'Marker': ...

class Logger(java.lang.Object):
    """
    Java class 'org.slf4j.Logger'
    
      Attributes:
        ROOT_LOGGER_NAME (java.lang.String): final static field
    
    """
    ROOT_LOGGER_NAME: typing.ClassVar[java.lang.String] = ...
    @typing.overload
    def debug(self, string: java.lang.String) -> None: ...
    @typing.overload
    def debug(self, string: java.lang.String, object: typing.Any) -> None: ...
    @typing.overload
    def debug(self, string: java.lang.String, object: typing.Any, object2: typing.Any) -> None: ...
    @typing.overload
    def debug(self, string: java.lang.String, objectArray: typing.List[typing.Any]) -> None: ...
    @typing.overload
    def debug(self, string: java.lang.String, throwable: java.lang.Throwable) -> None: ...
    @typing.overload
    def debug(self, marker: 'Marker', string: java.lang.String) -> None: ...
    @typing.overload
    def debug(self, marker: 'Marker', string: java.lang.String, object: typing.Any) -> None: ...
    @typing.overload
    def debug(self, marker: 'Marker', string: java.lang.String, object: typing.Any, object2: typing.Any) -> None: ...
    @typing.overload
    def debug(self, marker: 'Marker', string: java.lang.String, objectArray: typing.List[typing.Any]) -> None: ...
    @typing.overload
    def debug(self, marker: 'Marker', string: java.lang.String, throwable: java.lang.Throwable) -> None: ...
    @typing.overload
    def error(self, string: java.lang.String) -> None: ...
    @typing.overload
    def error(self, string: java.lang.String, object: typing.Any) -> None: ...
    @typing.overload
    def error(self, string: java.lang.String, object: typing.Any, object2: typing.Any) -> None: ...
    @typing.overload
    def error(self, string: java.lang.String, objectArray: typing.List[typing.Any]) -> None: ...
    @typing.overload
    def error(self, string: java.lang.String, throwable: java.lang.Throwable) -> None: ...
    @typing.overload
    def error(self, marker: 'Marker', string: java.lang.String) -> None: ...
    @typing.overload
    def error(self, marker: 'Marker', string: java.lang.String, object: typing.Any) -> None: ...
    @typing.overload
    def error(self, marker: 'Marker', string: java.lang.String, object: typing.Any, object2: typing.Any) -> None: ...
    @typing.overload
    def error(self, marker: 'Marker', string: java.lang.String, objectArray: typing.List[typing.Any]) -> None: ...
    @typing.overload
    def error(self, marker: 'Marker', string: java.lang.String, throwable: java.lang.Throwable) -> None: ...
    def getName(self) -> java.lang.String: ...
    @typing.overload
    def info(self, string: java.lang.String) -> None: ...
    @typing.overload
    def info(self, string: java.lang.String, object: typing.Any) -> None: ...
    @typing.overload
    def info(self, string: java.lang.String, object: typing.Any, object2: typing.Any) -> None: ...
    @typing.overload
    def info(self, string: java.lang.String, objectArray: typing.List[typing.Any]) -> None: ...
    @typing.overload
    def info(self, string: java.lang.String, throwable: java.lang.Throwable) -> None: ...
    @typing.overload
    def info(self, marker: 'Marker', string: java.lang.String) -> None: ...
    @typing.overload
    def info(self, marker: 'Marker', string: java.lang.String, object: typing.Any) -> None: ...
    @typing.overload
    def info(self, marker: 'Marker', string: java.lang.String, object: typing.Any, object2: typing.Any) -> None: ...
    @typing.overload
    def info(self, marker: 'Marker', string: java.lang.String, objectArray: typing.List[typing.Any]) -> None: ...
    @typing.overload
    def info(self, marker: 'Marker', string: java.lang.String, throwable: java.lang.Throwable) -> None: ...
    @typing.overload
    def isDebugEnabled(self) -> bool: ...
    @typing.overload
    def isDebugEnabled(self, marker: 'Marker') -> bool: ...
    @typing.overload
    def isErrorEnabled(self) -> bool: ...
    @typing.overload
    def isErrorEnabled(self, marker: 'Marker') -> bool: ...
    @typing.overload
    def isInfoEnabled(self) -> bool: ...
    @typing.overload
    def isInfoEnabled(self, marker: 'Marker') -> bool: ...
    @typing.overload
    def isTraceEnabled(self) -> bool: ...
    @typing.overload
    def isTraceEnabled(self, marker: 'Marker') -> bool: ...
    @typing.overload
    def isWarnEnabled(self) -> bool: ...
    @typing.overload
    def isWarnEnabled(self, marker: 'Marker') -> bool: ...
    @typing.overload
    def trace(self, string: java.lang.String) -> None: ...
    @typing.overload
    def trace(self, string: java.lang.String, object: typing.Any) -> None: ...
    @typing.overload
    def trace(self, string: java.lang.String, object: typing.Any, object2: typing.Any) -> None: ...
    @typing.overload
    def trace(self, string: java.lang.String, objectArray: typing.List[typing.Any]) -> None: ...
    @typing.overload
    def trace(self, string: java.lang.String, throwable: java.lang.Throwable) -> None: ...
    @typing.overload
    def trace(self, marker: 'Marker', string: java.lang.String) -> None: ...
    @typing.overload
    def trace(self, marker: 'Marker', string: java.lang.String, object: typing.Any) -> None: ...
    @typing.overload
    def trace(self, marker: 'Marker', string: java.lang.String, object: typing.Any, object2: typing.Any) -> None: ...
    @typing.overload
    def trace(self, marker: 'Marker', string: java.lang.String, objectArray: typing.List[typing.Any]) -> None: ...
    @typing.overload
    def trace(self, marker: 'Marker', string: java.lang.String, throwable: java.lang.Throwable) -> None: ...
    @typing.overload
    def warn(self, string: java.lang.String) -> None: ...
    @typing.overload
    def warn(self, string: java.lang.String, object: typing.Any) -> None: ...
    @typing.overload
    def warn(self, string: java.lang.String, object: typing.Any, object2: typing.Any) -> None: ...
    @typing.overload
    def warn(self, string: java.lang.String, objectArray: typing.List[typing.Any]) -> None: ...
    @typing.overload
    def warn(self, string: java.lang.String, throwable: java.lang.Throwable) -> None: ...
    @typing.overload
    def warn(self, marker: 'Marker', string: java.lang.String) -> None: ...
    @typing.overload
    def warn(self, marker: 'Marker', string: java.lang.String, object: typing.Any) -> None: ...
    @typing.overload
    def warn(self, marker: 'Marker', string: java.lang.String, object: typing.Any, object2: typing.Any) -> None: ...
    @typing.overload
    def warn(self, marker: 'Marker', string: java.lang.String, objectArray: typing.List[typing.Any]) -> None: ...
    @typing.overload
    def warn(self, marker: 'Marker', string: java.lang.String, throwable: java.lang.Throwable) -> None: ...

class LoggerFactory(java.lang.Object):
    """
    Java class 'org.slf4j.LoggerFactory'
    
        Extends:
            java.lang.Object
    
    """
    @classmethod
    def getILoggerFactory(cls) -> ILoggerFactory: ...
    @classmethod
    @typing.overload
    def getLogger(cls, class_: typing.Type[typing.Any]) -> Logger: ...
    @classmethod
    @typing.overload
    def getLogger(cls, string: java.lang.String) -> Logger: ...

class MDC(java.lang.Object):
    """
    Java class 'org.slf4j.MDC'
    
        Extends:
            java.lang.Object
    
    """
    @classmethod
    def clear(cls) -> None: ...
    @classmethod
    def get(cls, string: java.lang.String) -> java.lang.String: ...
    @classmethod
    def getCopyOfContextMap(cls) -> java.util.Map[java.lang.String, java.lang.String]: ...
    @classmethod
    def getMDCAdapter(cls) -> org.slf4j.spi.MDCAdapter: ...
    @classmethod
    def put(cls, string: java.lang.String, string2: java.lang.String) -> None: ...
    @classmethod
    def putCloseable(cls, string: java.lang.String, string2: java.lang.String) -> 'MDC.MDCCloseable': ...
    @classmethod
    def remove(cls, string: java.lang.String) -> None: ...
    @classmethod
    def setContextMap(cls, map: typing.Union[java.util.Map[java.lang.String, java.lang.String], typing.Mapping[java.lang.String, java.lang.String]]) -> None: ...
    class MDCCloseable(java.io.Closeable):
        """
        Java class 'org.slf4j.MDC$MDCCloseable'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.io.Closeable
        
        """
        def close(self) -> None: ...

class Marker(java.io.Serializable):
    """
    Java class 'org.slf4j.Marker'
    
        Interfaces:
            java.io.Serializable
    
      Attributes:
        ANY_MARKER (java.lang.String): final static field
        ANY_NON_NULL_MARKER (java.lang.String): final static field
    
    """
    ANY_MARKER: typing.ClassVar[java.lang.String] = ...
    ANY_NON_NULL_MARKER: typing.ClassVar[java.lang.String] = ...
    def add(self, marker: 'Marker') -> None: ...
    @typing.overload
    def contains(self, string: java.lang.String) -> bool: ...
    @typing.overload
    def contains(self, marker: 'Marker') -> bool: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getName(self) -> java.lang.String: ...
    def hasChildren(self) -> bool: ...
    def hasReferences(self) -> bool: ...
    def hashCode(self) -> int: ...
    def iterator(self) -> java.util.Iterator['Marker']: ...
    def remove(self, marker: 'Marker') -> bool: ...

class MarkerFactory(java.lang.Object):
    """
    Java class 'org.slf4j.MarkerFactory'
    
        Extends:
            java.lang.Object
    
    """
    @classmethod
    def getDetachedMarker(cls, string: java.lang.String) -> Marker: ...
    @classmethod
    def getIMarkerFactory(cls) -> IMarkerFactory: ...
    @classmethod
    def getMarker(cls, string: java.lang.String) -> Marker: ...
