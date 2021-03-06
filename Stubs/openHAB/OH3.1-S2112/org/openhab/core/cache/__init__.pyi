import java.lang
import java.time
import java.util
import java.util.concurrent
import java.util.function
import typing


class ByteArrayFileCache(java.lang.Object):
    """
    Java class 'org.openhab.core.cache.ByteArrayFileCache'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ByteArrayFileCache(java.lang.String)
        * ByteArrayFileCache(java.lang.String, java.time.Duration)
    
    """
    @typing.overload
    def __init__(self, servicePID: java.lang.String): ...
    @typing.overload
    def __init__(self, servicePID: java.lang.String, expiry: java.time.Duration): ...
    def clear(self) -> None: ...
    def clearExpired(self) -> None: ...
    def containsKey(self, key: java.lang.String) -> bool: ...
    def get(self, key: java.lang.String) -> typing.List[int]: ...
    def put(self, key: java.lang.String, content: typing.List[int]) -> None: ...
    def putIfAbsent(self, key: java.lang.String, content: typing.List[int]) -> None: ...
    def putIfAbsentAndGet(self, key: java.lang.String, content: typing.List[int]) -> typing.List[int]: ...
    def remove(self, key: java.lang.String) -> None: ...

_ExpiringCache__V = typing.TypeVar('_ExpiringCache__V')  # <V>
class ExpiringCache(java.lang.Object, typing.Generic[_ExpiringCache__V]):
    """
    Java class 'org.openhab.core.cache.ExpiringCache'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ExpiringCache(java.time.Duration, java.util.function.Supplier)
        * ExpiringCache(long, java.util.function.Supplier)
    
    """
    @typing.overload
    def __init__(self, expiry: java.time.Duration, action: typing.Union[java.util.function.Supplier[_ExpiringCache__V], typing.Callable[[], _ExpiringCache__V]]): ...
    @typing.overload
    def __init__(self, expiry: int, action: typing.Union[java.util.function.Supplier[_ExpiringCache__V], typing.Callable[[], _ExpiringCache__V]]): ...
    def getValue(self) -> _ExpiringCache__V: ...
    def invalidateValue(self) -> None: ...
    def isExpired(self) -> bool: ...
    def putValue(self, value: _ExpiringCache__V) -> None: ...
    def refreshValue(self) -> _ExpiringCache__V: ...

_ExpiringCacheAsync__V = typing.TypeVar('_ExpiringCacheAsync__V')  # <V>
class ExpiringCacheAsync(java.lang.Object, typing.Generic[_ExpiringCacheAsync__V]):
    """
    Java class 'org.openhab.core.cache.ExpiringCacheAsync'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ExpiringCacheAsync(java.time.Duration)
        * ExpiringCacheAsync(long)
    
    """
    @typing.overload
    def __init__(self, expiry: java.time.Duration): ...
    @typing.overload
    def __init__(self, expiry: int): ...
    def getLastKnownValue(self) -> _ExpiringCacheAsync__V: ...
    def getValue(self, requestNewValueFuture: typing.Union[java.util.function.Supplier[java.util.concurrent.CompletableFuture[_ExpiringCacheAsync__V]], typing.Callable[[], java.util.concurrent.CompletableFuture[_ExpiringCacheAsync__V]]]) -> java.util.concurrent.CompletableFuture[_ExpiringCacheAsync__V]: ...
    def invalidateValue(self) -> None: ...
    def isExpired(self) -> bool: ...
    def refreshValue(self, requestNewValueFuture: typing.Union[java.util.function.Supplier[java.util.concurrent.CompletableFuture[_ExpiringCacheAsync__V]], typing.Callable[[], java.util.concurrent.CompletableFuture[_ExpiringCacheAsync__V]]]) -> java.util.concurrent.CompletableFuture[_ExpiringCacheAsync__V]: ...

_ExpiringCacheMap__K = typing.TypeVar('_ExpiringCacheMap__K')  # <K>
_ExpiringCacheMap__V = typing.TypeVar('_ExpiringCacheMap__V')  # <V>
class ExpiringCacheMap(java.lang.Object, typing.Generic[_ExpiringCacheMap__K, _ExpiringCacheMap__V]):
    """
    Java class 'org.openhab.core.cache.ExpiringCacheMap'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ExpiringCacheMap(java.time.Duration)
        * ExpiringCacheMap(long)
    
    """
    @typing.overload
    def __init__(self, expiry: java.time.Duration): ...
    @typing.overload
    def __init__(self, expiry: int): ...
    def clear(self) -> None: ...
    def containsKey(self, key: _ExpiringCacheMap__K) -> bool: ...
    def get(self, key: _ExpiringCacheMap__K) -> _ExpiringCacheMap__V: ...
    def invalidate(self, key: _ExpiringCacheMap__K) -> None: ...
    def invalidateAll(self) -> None: ...
    def keys(self) -> java.util.Set[_ExpiringCacheMap__K]: ...
    @typing.overload
    def put(self, key: _ExpiringCacheMap__K, action: typing.Union[java.util.function.Supplier[_ExpiringCacheMap__V], typing.Callable[[], _ExpiringCacheMap__V]]) -> None: ...
    @typing.overload
    def put(self, key: _ExpiringCacheMap__K, item: ExpiringCache[_ExpiringCacheMap__V]) -> None: ...
    def putIfAbsent(self, key: _ExpiringCacheMap__K, item: ExpiringCache[_ExpiringCacheMap__V]) -> None: ...
    @typing.overload
    def putIfAbsentAndGet(self, key: _ExpiringCacheMap__K, action: typing.Union[java.util.function.Supplier[_ExpiringCacheMap__V], typing.Callable[[], _ExpiringCacheMap__V]]) -> _ExpiringCacheMap__V: ...
    @typing.overload
    def putIfAbsentAndGet(self, key: _ExpiringCacheMap__K, item: ExpiringCache[_ExpiringCacheMap__V]) -> _ExpiringCacheMap__V: ...
    def putValue(self, key: _ExpiringCacheMap__K, value: _ExpiringCacheMap__V) -> None: ...
    def refresh(self, key: _ExpiringCacheMap__K) -> _ExpiringCacheMap__V: ...
    def refreshAll(self) -> java.util.Collection[_ExpiringCacheMap__V]: ...
    def remove(self, key: _ExpiringCacheMap__K) -> None: ...
    def values(self) -> java.util.Collection[_ExpiringCacheMap__V]: ...
