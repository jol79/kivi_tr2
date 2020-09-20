import kivy as kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import ObjectProperty


# initializing gridlayout widget with label:
class MainPage(Widget):

    # initializing variables to get from kv file:
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    keyword = ObjectProperty(None)

    def btn(self):
        print("email: ", self.email.text,
              ", password: ", self.password.text,
              ", keyword: ", self.keyword.text)


# # button widget:
# class Launch(BoxLayout):
#     def __init__(self, **kwargs):
#         super(Launch, self).__init__(**kwargs)
#         search_button = Button(
#                 text="Search",
#                 size=(80, 80),
#                 size_hint=(None, None)
#         )
#         # search_button.bind(on_press=self.)


###
# to change name of the app you need to refactor
# name of the this main class:
###
class PingPong(App):

    def build(self):
        return MainPage()


if __name__ == '__main__':
    PingPong().run()
