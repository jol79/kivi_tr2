import kivy as kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button


# initializing gridlayout widget with label:
class MainPage(Widget):
    # def __init__(self, **kwargs):
    #     super(MainPage, self).__init__(**kwargs)
    #     self.add_widget(Label(text="Hello on this page"))
    pass


###
# to change name of the app you need to refactor
# name of the this main class:
###
class PingPong(App):

    def build(self):
        return MainPage()


if __name__ == '__main__':
    PingPong().run()
