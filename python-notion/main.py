from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.graphics.svg import Svg
from kivy.uix.scatter import Scatter

Window.size = (1920, 1080)
Window.fullscreen = True
Builder.load_file('stylish.kv')

class SvgWidget(Scatter):
    def __init__(self, **kwargs):
        super(SvgWidget, self).__init__(**kwargs)
        with self.canvas:
            svg = Svg('pictures/1f3e1.svg')
        self.size = svg.width*2, svg.height*2

class NotionWidget(Widget):
    pass

class NotionApp(App):
    def build(self,):
        return NotionWidget()

NotionApp().run()