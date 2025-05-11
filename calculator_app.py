from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

KV = '''
<Calculator>:
    orientation: 'vertical'
    padding: 10
    spacing: 10

    TextInput:
        id: input_box
        font_size: 32
        size_hint_y: 0.2
        multiline: False
        readonly: True
        halign: 'right'
        text: root.display

    GridLayout:
        cols: 4
        spacing: 10
        size_hint_y: 0.8

        Button:
            text: '7'
            on_press: root.button_press(self.text)
        Button:
            text: '8'
            on_press: root.button_press(self.text)
        Button:
            text: '9'
            on_press: root.button_press(self.text)
        Button:
            text: '/'
            on_press: root.button_press(self.text)

        Button:
            text: '4'
            on_press: root.button_press(self.text)
        Button:
            text: '5'
            on_press: root.button_press(self.text)
        Button:
            text: '6'
            on_press: root.button_press(self.text)
        Button:
            text: '*'
            on_press: root.button_press(self.text)

        Button:
            text: '1'
            on_press: root.button_press(self.text)
        Button:
            text: '2'
            on_press: root.button_press(self.text)
        Button:
            text: '3'
            on_press: root.button_press(self.text)
        Button:
            text: '-'
            on_press: root.button_press(self.text)

        Button:
            text: 'C'
            on_press: root.clear_display()
        Button:
            text: '0'
            on_press: root.button_press(self.text)
        Button:
            text: '='
            on_press: root.calculate_result()
        Button:
            text: '+'
            on_press: root.button_press(self.text)
'''

class Calculator(BoxLayout):
    display = ""

    def button_press(self, button_text):
        self.display += button_text
        self.ids.input_box.text = self.display

    def clear_display(self):
        self.display = ""
        self.ids.input_box.text = self.display

    def calculate_result(self):
        try:
            result = str(eval(self.display))
            self.display = result
            self.ids.input_box.text = result
        except Exception:
            self.ids.input_box.text = "Error"
            self.display = ""

class CalculatorApp(App):
    def build(self):
        Builder.load_string(KV)
        return Calculator()

if __name__ == '__main__':
    CalculatorApp().run()