import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class CalculatorApp(toga.App):
    def startup(self):
        # Create the main window
        self.main_window = toga.MainWindow(title=self.formal_name)
        
        # Current operator state
        self.operators = {'+', '-', '*', '/'}
        self.current_value = ""
        
        # Create the result display
        self.result_display = toga.TextInput(readonly=True, style=Pack(padding=5, font_size=20))
        
        # Create button layout
        button_style = Pack(width=50, height=50, padding=5)
        
        # Row 1: 7, 8, 9, /
        row1 = toga.Box(style=Pack(direction=ROW))
        btn_7 = toga.Button('7', on_press=self.on_button_click, style=button_style)
        btn_8 = toga.Button('8', on_press=self.on_button_click, style=button_style)
        btn_9 = toga.Button('9', on_press=self.on_button_click, style=button_style)
        btn_div = toga.Button('/', on_press=self.on_operator_click, style=button_style)
        row1.add(btn_7)
        row1.add(btn_8)
        row1.add(btn_9)
        row1.add(btn_div)
        
        # Row 2: 4, 5, 6, *
        row2 = toga.Box(style=Pack(direction=ROW))
        btn_4 = toga.Button('4', on_press=self.on_button_click, style=button_style)
        btn_5 = toga.Button('5', on_press=self.on_button_click, style=button_style)
        btn_6 = toga.Button('6', on_press=self.on_button_click, style=button_style)
        btn_mul = toga.Button('*', on_press=self.on_operator_click, style=button_style)
        row2.add(btn_4)
        row2.add(btn_5)
        row2.add(btn_6)
        row2.add(btn_mul)
        
        # Row 3: 1, 2, 3, -
        row3 = toga.Box(style=Pack(direction=ROW))
        btn_1 = toga.Button('1', on_press=self.on_button_click, style=button_style)
        btn_2 = toga.Button('2', on_press=self.on_button_click, style=button_style)
        btn_3 = toga.Button('3', on_press=self.on_button_click, style=button_style)
        btn_sub = toga.Button('-', on_press=self.on_operator_click, style=button_style)
        row3.add(btn_1)
        row3.add(btn_2)
        row3.add(btn_3)
        row3.add(btn_sub)
        
        # Row 4: C, 0, =, +
        row4 = toga.Box(style=Pack(direction=ROW))
        btn_clear = toga.Button('C', on_press=self.clear, style=button_style)
        btn_0 = toga.Button('0', on_press=self.on_button_click, style=button_style)
        btn_eq = toga.Button('=', on_press=self.calculate, style=button_style)
        btn_add = toga.Button('+', on_press=self.on_operator_click, style=button_style)
        row4.add(btn_clear)
        row4.add(btn_0)
        row4.add(btn_eq)
        row4.add(btn_add)
        
        # Main container
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
        main_box.add(self.result_display)
        main_box.add(row1)
        main_box.add(row2)
        main_box.add(row3)
        main_box.add(row4)
        
        # Set the content of the main window
        self.main_window.content = main_box
        self.main_window.show()
    
    def on_button_click(self, widget):
        self.current_value += widget.text
        self.result_display.value = self.current_value
    
    def on_operator_click(self, widget):
        if self.current_value and self.current_value[-1] not in self.operators:
            self.current_value += widget.text
            self.result_display.value = self.current_value
    
    def clear(self, widget):
        self.current_value = ""
        self.result_display.value = ""
    
    def calculate(self, widget):
        try:
            result = str(eval(self.current_value))
            self.current_value = result
            self.result_display.value = result
        except Exception:
            self.result_display.value = "Error"
            self.current_value = ""


def main():
    return CalculatorApp('Calculator', 'org.example.calculator')