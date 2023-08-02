from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

class InterestingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation = 'horizontal')

        interesting_button = Button(text = 'Interesting', on_press = self.goto_interesting_screen)
        layout.add_widget(interesting_button)

        self.add_widget(layout)

    def goto_interesting_screen(self,instance):
        self.parent.current = 'wtf'