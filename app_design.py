import kivy as kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.filechooser import FileChooserListView

'''
Texture atlas in official kivy documentation, I can
use img as texture for each object I will want
'''
from kivy.uix.textinput import Texture
from kivy.uix.image import Image

'''
for button img I can use ButtonBehavior class of Button
parent class
'''
from kivy.uix.button import ButtonBehavior


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

    # # method to get path from filechooser:
    # def load(self, path, filename):
    #     with open(os.path.join(path, filename), 'w') as stream:
    #         stream.write(self.text)


# button widget to open popup window with filechooser:
class SearchButton(Widget):

    filechooser = ObjectProperty(None)

    def btn_filechooser(self):

        # popup window with filechooser:
        popup = Popup(title="Choose file",
                      content=self.filechooser,
                      auto_dismiss=False,
                      size=(400, 200))


'''
to change name of the app you need to refactor
name of the this main class:
'''
class PingPong(App):

    def build(self):
        return MainPage()


if __name__ == '__main__':
    PingPong().run()
