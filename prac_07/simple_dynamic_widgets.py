from kivy.app import App
from kivy.lang import Builder


class SimpleDynamicWidgetsApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = {"John Smith", "Julian cain", "Fred Andrews"}

    def build(self):
        self.title = "Simple Dynamic widgets"
        self.root = Builder.load_file('simple_dynamic_widgets.kv')
        return self.root

    def create_label(self):
        for name in self.names:
            temp_label = Label(text=name, id=name)
            self.root.ids.entries_box.add_widget(temp_label)


SimpleDynamicWidgetsApp().run()
