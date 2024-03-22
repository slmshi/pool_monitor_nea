import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button

class MainUI(Widget):
    pass

class MainApp(App):
    def build(self):
        return MainUI()



if __name__ == "__main__":
    MainApp().run()