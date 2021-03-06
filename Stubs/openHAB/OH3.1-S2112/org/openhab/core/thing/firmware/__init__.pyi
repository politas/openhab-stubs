import java.lang
import java.util
import org
import org.openhab.core.events
import org.openhab.core.thing
import org.openhab.core.thing.binding.firmware
import typing


class FirmwareEventFactory(org.openhab.core.events.AbstractEventFactory):
    """
    Java class 'org.openhab.core.thing.firmware.FirmwareEventFactory'
    
        Extends:
            org.openhab.core.events.AbstractEventFactory
    
      Constructors:
        * FirmwareEventFactory()
    
    """
    def __init__(self): ...
    @classmethod
    def createFirmwareStatusInfoEvent(cls, firmwareStatusInfo: 'FirmwareStatusInfo') -> 'FirmwareStatusInfoEvent': ...
    @classmethod
    def createFirmwareUpdateProgressInfoEvent(cls, progressInfo: 'FirmwareUpdateProgressInfo') -> 'FirmwareUpdateProgressInfoEvent': ...
    @classmethod
    def createFirmwareUpdateResultInfoEvent(cls, firmwareUpdateResultInfo: 'FirmwareUpdateResultInfo') -> 'FirmwareUpdateResultInfoEvent': ...

class FirmwareProvider(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.firmware.FirmwareProvider'
    
    """
    @typing.overload
    def getFirmware(self, thing: org.openhab.core.thing.Thing, version: java.lang.String) -> org.openhab.core.thing.binding.firmware.Firmware: ...
    @typing.overload
    def getFirmware(self, thing: org.openhab.core.thing.Thing, version: java.lang.String, locale: java.util.Locale) -> org.openhab.core.thing.binding.firmware.Firmware: ...
    @typing.overload
    def getFirmwares(self, thing: org.openhab.core.thing.Thing) -> java.util.Set[org.openhab.core.thing.binding.firmware.Firmware]: ...
    @typing.overload
    def getFirmwares(self, thing: org.openhab.core.thing.Thing, locale: java.util.Locale) -> java.util.Set[org.openhab.core.thing.binding.firmware.Firmware]: ...

class FirmwareRegistry(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.firmware.FirmwareRegistry'
    
    """
    @typing.overload
    def getFirmware(self, thing: org.openhab.core.thing.Thing, firmwareVersion: java.lang.String) -> org.openhab.core.thing.binding.firmware.Firmware: ...
    @typing.overload
    def getFirmware(self, thing: org.openhab.core.thing.Thing, firmwareVersion: java.lang.String, locale: java.util.Locale) -> org.openhab.core.thing.binding.firmware.Firmware: ...
    @typing.overload
    def getFirmwares(self, thing: org.openhab.core.thing.Thing) -> java.util.Collection[org.openhab.core.thing.binding.firmware.Firmware]: ...
    @typing.overload
    def getFirmwares(self, thing: org.openhab.core.thing.Thing, locale: java.util.Locale) -> java.util.Collection[org.openhab.core.thing.binding.firmware.Firmware]: ...
    @typing.overload
    def getLatestFirmware(self, thing: org.openhab.core.thing.Thing) -> org.openhab.core.thing.binding.firmware.Firmware: ...
    @typing.overload
    def getLatestFirmware(self, thing: org.openhab.core.thing.Thing, locale: java.util.Locale) -> org.openhab.core.thing.binding.firmware.Firmware: ...

class FirmwareStatus(java.lang.Enum[org.openhab.core.thing.firmware.FirmwareStatus]):
    """
    Java class 'org.openhab.core.thing.firmware.FirmwareStatus'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        UNKNOWN (org.openhab.core.thing.firmware.FirmwareStatus): final static enum constant
        UP_TO_DATE (org.openhab.core.thing.firmware.FirmwareStatus): final static enum constant
        UPDATE_AVAILABLE (org.openhab.core.thing.firmware.FirmwareStatus): final static enum constant
        UPDATE_EXECUTABLE (org.openhab.core.thing.firmware.FirmwareStatus): final static enum constant
    
    """
    UNKNOWN: typing.ClassVar['FirmwareStatus'] = ...
    UP_TO_DATE: typing.ClassVar['FirmwareStatus'] = ...
    UPDATE_AVAILABLE: typing.ClassVar['FirmwareStatus'] = ...
    UPDATE_EXECUTABLE: typing.ClassVar['FirmwareStatus'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, name: java.lang.String) -> 'FirmwareStatus': ...
    @classmethod
    def values(cls) -> typing.List['FirmwareStatus']: ...

class FirmwareStatusInfo(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.firmware.FirmwareStatusInfo'
    
        Extends:
            java.lang.Object
    
    """
    @classmethod
    def createUnknownInfo(cls, thingUID: org.openhab.core.thing.ThingUID) -> 'FirmwareStatusInfo': ...
    @classmethod
    def createUpToDateInfo(cls, thingUID: org.openhab.core.thing.ThingUID) -> 'FirmwareStatusInfo': ...
    @classmethod
    def createUpdateAvailableInfo(cls, thingUID: org.openhab.core.thing.ThingUID) -> 'FirmwareStatusInfo': ...
    @classmethod
    def createUpdateExecutableInfo(cls, thingUID: org.openhab.core.thing.ThingUID, firmwareVersion: java.lang.String) -> 'FirmwareStatusInfo': ...
    def equals(self, obj: typing.Any) -> bool: ...
    def getFirmwareStatus(self) -> FirmwareStatus: ...
    def getThingUID(self) -> org.openhab.core.thing.ThingUID: ...
    def getUpdatableFirmwareVersion(self) -> java.lang.String: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...

class FirmwareStatusInfoEvent(org.openhab.core.events.AbstractEvent):
    """
    Java class 'org.openhab.core.thing.firmware.FirmwareStatusInfoEvent'
    
        Extends:
            org.openhab.core.events.AbstractEvent
    
      Attributes:
        TYPE (java.lang.String): final static field
    
    """
    TYPE: typing.ClassVar[java.lang.String] = ...
    def equals(self, obj: typing.Any) -> bool: ...
    def getFirmwareStatusInfo(self) -> FirmwareStatusInfo: ...
    def getType(self) -> java.lang.String: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...

class FirmwareUpdateProgressInfo(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.firmware.FirmwareUpdateProgressInfo'
    
        Extends:
            java.lang.Object
    
    """
    @classmethod
    @typing.overload
    def createFirmwareUpdateProgressInfo(cls, thingUID: org.openhab.core.thing.ThingUID, firmwareVersion: java.lang.String, progressStep: org.openhab.core.thing.binding.firmware.ProgressStep, sequence: typing.Union[java.util.Collection[org.openhab.core.thing.binding.firmware.ProgressStep], typing.Sequence[org.openhab.core.thing.binding.firmware.ProgressStep]], pending: bool, progress: int) -> 'FirmwareUpdateProgressInfo': ...
    @classmethod
    @typing.overload
    def createFirmwareUpdateProgressInfo(cls, thingUID: org.openhab.core.thing.ThingUID, thingTypeUID: org.openhab.core.thing.ThingTypeUID, firmwareVersion: java.lang.String, progressStep: org.openhab.core.thing.binding.firmware.ProgressStep, sequence: typing.Union[java.util.Collection[org.openhab.core.thing.binding.firmware.ProgressStep], typing.Sequence[org.openhab.core.thing.binding.firmware.ProgressStep]], pending: bool) -> 'FirmwareUpdateProgressInfo': ...
    def equals(self, obj: typing.Any) -> bool: ...
    def getFirmwareVersion(self) -> java.lang.String: ...
    def getProgress(self) -> int: ...
    def getProgressStep(self) -> org.openhab.core.thing.binding.firmware.ProgressStep: ...
    def getSequence(self) -> java.util.Collection[org.openhab.core.thing.binding.firmware.ProgressStep]: ...
    def getThingUID(self) -> org.openhab.core.thing.ThingUID: ...
    def hashCode(self) -> int: ...
    def isPending(self) -> bool: ...
    def toString(self) -> java.lang.String: ...

class FirmwareUpdateProgressInfoEvent(org.openhab.core.events.AbstractEvent):
    """
    Java class 'org.openhab.core.thing.firmware.FirmwareUpdateProgressInfoEvent'
    
        Extends:
            org.openhab.core.events.AbstractEvent
    
      Attributes:
        TYPE (java.lang.String): final static field
    
    """
    TYPE: typing.ClassVar[java.lang.String] = ...
    def equals(self, obj: typing.Any) -> bool: ...
    def getProgressInfo(self) -> FirmwareUpdateProgressInfo: ...
    def getType(self) -> java.lang.String: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...

class FirmwareUpdateResult(java.lang.Enum[org.openhab.core.thing.firmware.FirmwareUpdateResult]):
    """
    Java class 'org.openhab.core.thing.firmware.FirmwareUpdateResult'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        SUCCESS (org.openhab.core.thing.firmware.FirmwareUpdateResult): final static enum constant
        ERROR (org.openhab.core.thing.firmware.FirmwareUpdateResult): final static enum constant
        CANCELED (org.openhab.core.thing.firmware.FirmwareUpdateResult): final static enum constant
    
    """
    SUCCESS: typing.ClassVar['FirmwareUpdateResult'] = ...
    ERROR: typing.ClassVar['FirmwareUpdateResult'] = ...
    CANCELED: typing.ClassVar['FirmwareUpdateResult'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @typing.overload
    def valueOf(cls, class_: typing.Type[_valueOf_0__T], string: java.lang.String) -> _valueOf_0__T: ...
    @classmethod
    @typing.overload
    def valueOf(cls, name: java.lang.String) -> 'FirmwareUpdateResult': ...
    @classmethod
    def values(cls) -> typing.List['FirmwareUpdateResult']: ...

class FirmwareUpdateResultInfo(java.lang.Object):
    """
    Java class 'org.openhab.core.thing.firmware.FirmwareUpdateResultInfo'
    
        Extends:
            java.lang.Object
    
    """
    @classmethod
    def createFirmwareUpdateResultInfo(cls, thingUID: org.openhab.core.thing.ThingUID, result: FirmwareUpdateResult, errorMessage: java.lang.String) -> 'FirmwareUpdateResultInfo': ...
    def equals(self, obj: typing.Any) -> bool: ...
    def getErrorMessage(self) -> java.lang.String: ...
    def getResult(self) -> FirmwareUpdateResult: ...
    def getThingUID(self) -> org.openhab.core.thing.ThingUID: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...

class FirmwareUpdateResultInfoEvent(org.openhab.core.events.AbstractEvent):
    """
    Java class 'org.openhab.core.thing.firmware.FirmwareUpdateResultInfoEvent'
    
        Extends:
            org.openhab.core.events.AbstractEvent
    
      Attributes:
        TYPE (java.lang.String): final static field
    
    """
    TYPE: typing.ClassVar[java.lang.String] = ...
    def equals(self, obj: typing.Any) -> bool: ...
    def getFirmwareUpdateResultInfo(self) -> FirmwareUpdateResultInfo: ...
    def getType(self) -> java.lang.String: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...

class FirmwareUpdateService(java.lang.Object):
    """
    @NonNullByDefault public interface FirmwareUpdateService
    
        The firmware update service is registered as an OSGi service and is responsible for tracking all available
        :class:`~org.openhab.core.thing.binding.firmware.FirmwareUpdateHandler`s. It provides access to the current
        :class:`~org.openhab.core.thing.firmware.FirmwareStatusInfo` of a thing and is the central instance to start a firmware
        update.
    
    
    """
    def cancelFirmwareUpdate(self, thingUID: org.openhab.core.thing.ThingUID) -> None: ...
    def getFirmwareStatusInfo(self, thingUID: org.openhab.core.thing.ThingUID) -> FirmwareStatusInfo: ...
    def updateFirmware(self, thingUID: org.openhab.core.thing.ThingUID, firmwareVersion: java.lang.String, locale: java.util.Locale) -> None: ...
