import java.lang
import java.util
import org.openhab.core.config.discovery
import org.openhab.core.thing
import typing


class UsbSerialDeviceInformation(java.lang.Object):
    """
    Java class 'org.openhab.core.config.discovery.usbserial.UsbSerialDeviceInformation'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * UsbSerialDeviceInformation(int, int, java.lang.String, java.lang.String, java.lang.String, int, java.lang.String, java.lang.String)
    
    """
    def __init__(self, vendorId: int, productId: int, serialNumber: java.lang.String, manufacturer: java.lang.String, product: java.lang.String, interfaceNumber: int, interfaceDescription: java.lang.String, serialPort: java.lang.String): ...
    def equals(self, obj: typing.Any) -> bool: ...
    def getInterfaceDescription(self) -> java.lang.String: ...
    def getInterfaceNumber(self) -> int: ...
    def getManufacturer(self) -> java.lang.String: ...
    def getProduct(self) -> java.lang.String: ...
    def getProductId(self) -> int: ...
    def getSerialNumber(self) -> java.lang.String: ...
    def getSerialPort(self) -> java.lang.String: ...
    def getVendorId(self) -> int: ...
    def hashCode(self) -> int: ...
    def toString(self) -> java.lang.String: ...

class UsbSerialDiscovery(java.lang.Object):
    """
    @NonNullByDefault public interface UsbSerialDiscovery
    
        Interface for implementations for discovering serial ports provided by a USB device. An implementation of this interface
        is required by the :code:`UsbSerialDiscoveryService`.
    
    
    """
    def doSingleScan(self) -> None: ...
    def registerDiscoveryListener(self, listener: 'UsbSerialDiscoveryListener') -> None: ...
    def startBackgroundScanning(self) -> None: ...
    def stopBackgroundScanning(self) -> None: ...
    def unregisterDiscoveryListener(self, listener: 'UsbSerialDiscoveryListener') -> None: ...

class UsbSerialDiscoveryListener(java.lang.Object):
    """
    @NonNullByDefault public interface UsbSerialDiscoveryListener
    
        Listener interface for :class:`~org.openhab.core.config.discovery.usbserial.UsbSerialDiscovery`s.
    
    
    """
    def usbSerialDeviceDiscovered(self, usbSerialDeviceInformation: UsbSerialDeviceInformation) -> None: ...
    def usbSerialDeviceRemoved(self, usbSerialDeviceInformation: UsbSerialDeviceInformation) -> None: ...

class UsbSerialDiscoveryParticipant(java.lang.Object):
    """
    @NonNullByDefault public interface UsbSerialDiscoveryParticipant
    
        A :class:`~org.openhab.core.config.discovery.usbserial.UsbSerialDiscoveryParticipant` that is registered as a component
        is picked up by the :code:`UsbSerialDiscoveryService` and can thus contribute
        :class:`~org.openhab.core.config.discovery.usbserial.https:.github.com.openhab.infrastructure.org.openhab.core.reactor.org.openhab.core.reactor.bundles.org.openhab.core.config.discovery.apidocs.org.openhab.core.config.discovery.DiscoveryResult?is`s
        from scans for USB devices with an associated serial port.
    
    
    """
    def createResult(self, deviceInformation: UsbSerialDeviceInformation) -> org.openhab.core.config.discovery.DiscoveryResult: ...
    def getSupportedThingTypeUIDs(self) -> java.util.Set[org.openhab.core.thing.ThingTypeUID]: ...
    def getThingUID(self, deviceInformation: UsbSerialDeviceInformation) -> org.openhab.core.thing.ThingUID: ...