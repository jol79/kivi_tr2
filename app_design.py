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


'''
for button img I can use ButtonBehavior class of Button
parent class
'''
from kivy.uix.button import ButtonBehavior


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

    # # method to get path from filechooser:
    # def load(self, path, filename):
    #     with open(os.path.join(path, filename), 'w') as stream:
    #         stream.write(self.text)


# class to hold the content of popup:
class Upload_FileBrowser:

    def __init__(self, heading_text="Choose files"):

        if platform == 'win':
            user_path = dirname(expanduser('~')) + sep + 'Documents'
        else:
            user_path = expanduser('~') + sep + 'Documents'

        # initializing filebrowser object:
        browser = FileBrowser(select_string='Select', cancel_string='Cancel',
                              favorites=[(user_path, 'Documents')])

        # binding events:
        browser.bind(
            on_success=self._fbrowser_success,
            on_cancel=self._fbrowser_cancel
        )

        # popup to hold FileBrowser:
        self.popup = Popup(
            title=heading_text,
            content=browser,
            size_hint=(None, None),
            size=(600, 600)
        )

    def _fbrowser_success(self, instance):
        result_success = instance.selection
        return result_success

    def _fbrowser_cancel(self, instance):
        print("Nothing choosed")

    def start(self):
        self.popup.open()

# # button widget to open popup window with datetime chooser:
# class TimeButton(Widget):
#
#     datetime_chooser = ObjectProperty(None)
#
#         # popup window with datetime widget
#         popup = Popup(title="test")


# to change name of the app you need to refactor
# name of the this main class:
class PingPong(App):
    def build(self):
        return MainPage()


if __name__ == '__main__':
    PingPong().run()
