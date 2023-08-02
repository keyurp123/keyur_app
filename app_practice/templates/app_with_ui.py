# app_with_ui.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyAppWithUI(App):
    
    # Define button texts and their corresponding messages as tuples
    buttons_info = [
        ('Click Me 0', 'HELLO FROM THE GOO'),
        ('Click Me 1', 'HOW ARE YOU'),
        ('Click Me 2', 'SIUUUUU')
    ]
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Create multiple buttons and bind them to the on_button_click function
        for button_text, message in MyAppWithUI.buttons_info:
            button = Button(text=button_text)
            button.bind(on_press=self.on_button_click)
            layout.add_widget(button)

        return layout

    def on_button_click(self, instance):
        # This function will be called when the button is clicked
        for button_text, message in MyAppWithUI.buttons_info:
            if instance.text == button_text:
                instance.text = message
                instance.font_size = 70  # Increase the button's font size to 90
                instance.disabled = True

if __name__ == '__main__':
    MyAppWithUI().run()
