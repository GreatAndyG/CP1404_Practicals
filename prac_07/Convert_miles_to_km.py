from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class ConvertMilesApp(App):
    output_km = StringProperty

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('Convert_miles_to_km.kv')
        return self.root

    def handle_convert_miles(self):
        value = self.get_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        value = self.get_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_convert_miles()


    def get_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return "Number has to be > 0"


ConvertMilesApp().run()
