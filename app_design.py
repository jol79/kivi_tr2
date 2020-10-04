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
    # fixed size for window:
    Config.set('graphics', 'resizable', False)

    # initializing variables to get from kv file:
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    keyword = ObjectProperty(None)

    # method to open popup window:
    def show_popup(self):
        show = P()

        popupWindow = Popup(title="Choose file",
                            content=show,
                            size_hint=(None, None),
                            size=(400, 400))
        popupWindow.open()

    # button to get data provided in TextInput widgets:
    def btn__txt(self):
        print("email: ", self.email.text,
              ", password: ", self.password.text,
              ", keyword: ", self.keyword.text)

    # button to work with popup window:
    def btn__popup(self):
        self.show_popup()

    # # method to get path from filechooser:
    # def load(self, path, filename):
    #     with open(os.path.join(path, filename), 'w') as stream:
    #         stream.write(self.text)


# class to hold the content of our popup:
class P(FloatLayout):
    global selection
    global selection_result

    def set_filebrowser(self):

        if platform == 'win':
            user_path = dirname(expanduser('~')) + sep + 'Documents'
        else:
            user_path = expanduser('~') + sep + 'Documents'

        browser = FileBrowser(select_string='Select',
                              favorites=[(user_path, 'Documents')])

        # binding buttons events:
        browser.bind(
            on_success=self._fbrowser_success,
            on_canceled=self._fbrowser_canceled)

    def _fbrowser_canceled(self, instance):
        print('cancelled, Close self.')

    ###
    # if user successfully selected needed file
    # path for that file will be saved in selection
    # read-only ListProperty that will contain the list
    # of files that are currently selected
    ###
    def _fbrowser_success(self, instance):
        selection_result = instance.selection

        return selection_result


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
