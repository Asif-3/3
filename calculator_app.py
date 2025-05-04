from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class CalculatorApp(App):
    def build(self):
        self.operators = {'+', '-', '*', '/'}
        self.result = TextInput(font_size=32, readonly=True, halign='right', multiline=False)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.result)

        grid = GridLayout(cols=4)
        buttons = [
            ('7', self.on_button_click), ('8', self.on_button_click), ('9', self.on_button_click), ('/', self.on_operator_click),
            ('4', self.on_button_click), ('5', self.on_button_click), ('6', self.on_button_click), ('*', self.on_operator_click),
            ('1', self.on_button_click), ('2', self.on_button_click), ('3', self.on_button_click), ('-', self.on_operator_click),
            ('C', self.clear), ('0', self.on_button_click), ('=', self.calculate), ('+', self.on_operator_click),
        ]

        for label, on_press in buttons:
            button = Button(text=label, on_press=on_press)
            grid.add_widget(button)

        layout.add_widget(grid)
        return layout

    def on_button_click(self, instance):
        current = self.result.text
        new_text = current + instance.text
        self.result.text = new_text

    def on_operator_click(self, instance):
        current = self.result.text
        if current and current[-1] not in self.operators:
            new_text = current + instance.text
            self.result.text = new_text

    def clear(self, instance):
        self.result.text = ''

    def calculate(self, instance):
        try:
            result = str(eval(self.result.text))
            self.result.text = result
        except Exception:
            self.result.text = 'Error'

if __name__ == '__main__':
    CalculatorApp().run()
