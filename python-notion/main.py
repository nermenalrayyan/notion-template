from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('Stylish.kv')
class NotionWidget(Widget):
    pass

class NotionApp(App):
    def build(self,):
        return NotionWidget()

NotionApp().run()