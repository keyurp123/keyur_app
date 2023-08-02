from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

from buttons_info import buttons_info

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')

        options_button = Button(text='Options', on_press=self.goto_options_screen)
        layout.add_widget(options_button)

        woah_button = Button(text='Woah', on_press=self.goto_woah_screen)
        layout.add_widget(woah_button)

        for button_text, message in buttons_info:
            button = Button(text=button_text)
            button.bind(on_press=self.on_button_click)
            layout.add_widget(button)

        self.add_widget(layout)

    def goto_options_screen(self, instance):
        self.parent.current = 'settings'

    def goto_woah_screen(self, instance):
        self.parent.current = 'woah'

    def on_button_click(self, instance):
        for button_text, message in buttons_info:
            if instance.text == button_text:
                instance.text = message
                instance.font_size = 70
                instance.disabled = True
