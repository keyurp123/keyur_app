from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

class WoahScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation = 'horizontal')

        thisworks_button = Button(text = 'This works!', on_press = self.goto_thisworks_screen)
        layout.add_widget(thisworks_button)

        self.add_widget(layout)

    def goto_thisworks_screen(self,instance):
        self.parent.current = 'interesting'