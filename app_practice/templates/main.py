from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from home_screen import HomeScreen
from settings_screen import SettingsScreen
from woah_screen import WoahScreen
from interesting_screen import InterestingScreen

class MyAppWithUI(App):
    def build(self):

        self.screen_manager = ScreenManager()

        home_screen = HomeScreen(name='home')
        self.screen_manager.add_widget(home_screen)

        settings_screen = SettingsScreen(name='settings')
        self.screen_manager.add_widget(settings_screen)

        woah_screen = WoahScreen(name='woah')
        self.screen_manager.add_widget(woah_screen)

        interesting_screen = InterestingScreen(name = 'interesting')
        self.screen_manager.add_widget(interesting_screen)

        return self.screen_manager

if __name__ == '__main__':
    MyAppWithUI().run()
