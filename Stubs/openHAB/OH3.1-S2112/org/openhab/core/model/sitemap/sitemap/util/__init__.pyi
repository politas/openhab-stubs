import org.eclipse.emf.common.notify
import org.eclipse.emf.common.notify.impl
import org.eclipse.emf.ecore
import org.eclipse.emf.ecore.util
import org.openhab.core.model.sitemap.sitemap
import typing


class SitemapAdapterFactory(org.eclipse.emf.common.notify.impl.AdapterFactoryImpl):
    """
    Java class 'org.openhab.core.model.sitemap.sitemap.util.SitemapAdapterFactory'
    
        Extends:
            org.eclipse.emf.common.notify.impl.AdapterFactoryImpl
    
      Constructors:
        * SitemapAdapterFactory()
    
    """
    def __init__(self): ...
    def createAdapter(self, target: org.eclipse.emf.common.notify.Notifier) -> org.eclipse.emf.common.notify.Adapter: ...
    def createChartAdapter(self) -> org.eclipse.emf.common.notify.Adapter: ...
    def createColorArrayAdapter(self) -> org.eclipse.emf.common.notify.Adapter: ...
    def createColorpickerAdapter(self) -> org.eclipse.emf.common.notify.Adapter: ...
    def createDefaultAdapter(self) -> org.eclipse.emf.common.notify.Adapter: ...
    def createEObjectAdapter(self) -> org.eclipse.emf.common.notify.Adapter: ...
    def createFrameAdapter(self) -> org.eclipse.emf.common.notify.Adapter: ...
    def createGroupAdapter(self) -> org.eclipse.emf.common.notify.Adapter: ...
    def createImageAdapter(self) -> org.eclipse.emf.common.notify.Adapter: ...
    def createLinkableWidgetAdapter(self) -> org.eclipse.emf.common.notify.Adapter: ...
    def createListAdapter(self) -> org.eclipse.emf.common.notify.Adapter: ...
    def createMappingAdapter(self) -> org.eclipse.emf.common.notify.Adapter: ...
    def createMapviewAdapter(self) -> org.eclipse.emf.common.notify.Adapter: ...
    def createNonLinkableWidgetAdapter(self) -> org.eclipse.emf.common.notify.Adapter: ...
    def createSelectionAdapter(self) -> org.eclipse.emf.common.notify.Adapter: ...
    def createSetpointAdapter(self) -> org.eclipse.emf.common.notify.Adapter: ...
    def createSitemapAdapter(self) -> org.eclipse.emf.common.notify.Adapter: ...
    def createSitemapModelAdapter(self) -> org.eclipse.emf.common.notify.Adapter: ...
    def createSliderAdapter(self) -> org.eclipse.emf.common.notify.Adapter: ...
    def createSwitchAdapter(self) -> org.eclipse.emf.common.notify.Adapter: ...
    def createTextAdapter(self) -> org.eclipse.emf.common.notify.Adapter: ...
    def createVideoAdapter(self) -> org.eclipse.emf.common.notify.Adapter: ...
    def createVisibilityRuleAdapter(self) -> org.eclipse.emf.common.notify.Adapter: ...
    def createWebviewAdapter(self) -> org.eclipse.emf.common.notify.Adapter: ...
    def createWidgetAdapter(self) -> org.eclipse.emf.common.notify.Adapter: ...
    def isFactoryForType(self, object: typing.Any) -> bool: ...

_SitemapSwitch__T = typing.TypeVar('_SitemapSwitch__T')  # <T>
class SitemapSwitch(org.eclipse.emf.ecore.util.Switch[_SitemapSwitch__T], typing.Generic[_SitemapSwitch__T]):
    """
    Java class 'org.openhab.core.model.sitemap.sitemap.util.SitemapSwitch'
    
        Extends:
            org.eclipse.emf.ecore.util.Switch
    
      Constructors:
        * SitemapSwitch()
    
    """
    def __init__(self): ...
    def caseChart(self, object: org.openhab.core.model.sitemap.sitemap.Chart) -> _SitemapSwitch__T: ...
    def caseColorArray(self, object: org.openhab.core.model.sitemap.sitemap.ColorArray) -> _SitemapSwitch__T: ...
    def caseColorpicker(self, object: org.openhab.core.model.sitemap.sitemap.Colorpicker) -> _SitemapSwitch__T: ...
    def caseDefault(self, object: org.openhab.core.model.sitemap.sitemap.Default) -> _SitemapSwitch__T: ...
    def caseFrame(self, object: org.openhab.core.model.sitemap.sitemap.Frame) -> _SitemapSwitch__T: ...
    def caseGroup(self, object: org.openhab.core.model.sitemap.sitemap.Group) -> _SitemapSwitch__T: ...
    def caseImage(self, object: org.openhab.core.model.sitemap.sitemap.Image) -> _SitemapSwitch__T: ...
    def caseLinkableWidget(self, object: org.openhab.core.model.sitemap.sitemap.LinkableWidget) -> _SitemapSwitch__T: ...
    def caseList(self, object: org.openhab.core.model.sitemap.sitemap.List) -> _SitemapSwitch__T: ...
    def caseMapping(self, object: org.openhab.core.model.sitemap.sitemap.Mapping) -> _SitemapSwitch__T: ...
    def caseMapview(self, object: org.openhab.core.model.sitemap.sitemap.Mapview) -> _SitemapSwitch__T: ...
    def caseNonLinkableWidget(self, object: org.openhab.core.model.sitemap.sitemap.NonLinkableWidget) -> _SitemapSwitch__T: ...
    def caseSelection(self, object: org.openhab.core.model.sitemap.sitemap.Selection) -> _SitemapSwitch__T: ...
    def caseSetpoint(self, object: org.openhab.core.model.sitemap.sitemap.Setpoint) -> _SitemapSwitch__T: ...
    def caseSitemap(self, object: org.openhab.core.model.sitemap.sitemap.Sitemap) -> _SitemapSwitch__T: ...
    def caseSitemapModel(self, object: org.openhab.core.model.sitemap.sitemap.SitemapModel) -> _SitemapSwitch__T: ...
    def caseSlider(self, object: org.openhab.core.model.sitemap.sitemap.Slider) -> _SitemapSwitch__T: ...
    def caseSwitch(self, object: org.openhab.core.model.sitemap.sitemap.Switch) -> _SitemapSwitch__T: ...
    def caseText(self, object: org.openhab.core.model.sitemap.sitemap.Text) -> _SitemapSwitch__T: ...
    def caseVideo(self, object: org.openhab.core.model.sitemap.sitemap.Video) -> _SitemapSwitch__T: ...
    def caseVisibilityRule(self, object: org.openhab.core.model.sitemap.sitemap.VisibilityRule) -> _SitemapSwitch__T: ...
    def caseWebview(self, object: org.openhab.core.model.sitemap.sitemap.Webview) -> _SitemapSwitch__T: ...
    def caseWidget(self, object: org.openhab.core.model.sitemap.sitemap.Widget) -> _SitemapSwitch__T: ...
    def defaultCase(self, object: org.eclipse.emf.ecore.EObject) -> _SitemapSwitch__T: ...