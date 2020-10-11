import kivy as kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivy_garden.filebrowser import FileBrowser

'''
 Libraries needed for file chooser:
'''
from kivy.uix.filechooser import FileChooserListView
from os.path import sep, expanduser, isdir, dirname
from platform import platform


'''
Texture atlas in official kivy documentation, I can
use img as texture for each object I will want
'''
from kivy.uix.textinput import Texture
from kivy.uix.image import Image


# initializing gridlayout widget with label:
class MainPage(Widget):

    # initializing upload_filebrowser class:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.show = Upload_FileBrowser()

    # fixed size for window:
    Config.set('graphics', 'resizable', False)

    # initializing variables to get from kv file:
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    keyword = ObjectProperty(None)

    # button to get data provided in TextInput widgets:
    def btn__txt(self):
        print("email: ", self.email.text,
              ", password: ", self.password.text,
              ", keyword: ", self.keyword.text)

    # button to work with popup window:
    def btn__popup(self):
        self.show.start()


# class to hold the content of popup:
class Upload_FileBrowser:

    def __init__(self, heading_text="Choose files"):

        # initializing filebrowser object:
        browser = FileBrowser(select_string='Select', cancel_string='Cancel')

        # binding events:
        browser.bind(
            on_success=self._fbrowser_success,
            on_cancel=self._fbrowser_canceled
        )

        # popup to hold FileBrowser:
        self.popup = Popup(
            title=heading_text,
            content=browser,
            size_hint=(None, None),
            size=(600, 500),
        )

    def _fbrowser_success(self, instance):
        result_success = instance.selection
        return result_success

    def _fbrowser_canceled(self, instance):
        print("Nothing chose")

    def start(self):
        self.popup.open()


# to change name of the app you need to refactor
# name of the this main class:
class PingPong(App):
    def build(self):

        return MainPage()


if __name__ == '__main__':
    PingPong().run()
