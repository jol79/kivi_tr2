from kivy.lang import Builder
from kivy.app import App
from kivy.uix import filechooser
from kivy.uix.popup import Popup
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.popup import Popup
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.properties import ObjectProperty, StringProperty
from kivy.config import Config


# class to storage object in Popup
class FileChoosePopup(Popup):
    load = ObjectProperty()


class Tab(TabbedPanel):

    Config.set('graphics', 'resizable', False)

    # when user don't choose any file and trying to load path:
    file_path = StringProperty("No file chosen")
    the_popup = ObjectProperty(None)
    get_email = ObjectProperty(None)
    get_password = ObjectProperty(None)
    get_keyword = ObjectProperty(None)

    def get_data(self):
        print("email: ", self.get_email.text,
              "\npassword: ", self.get_password.text,
              "\nkeyword: ", self.get_keyword.text)

    def open_popup(self):
        # loads data for popup:
        self.the_popup = FileChoosePopup(load=self.load)

        # opens popup with loaded data:
        self.the_popup.open()

    def load(self, selection):
        # save data
        self.file_path = str(selection[0])
        # after button pressed, and data selected -> close popup
        self.the_popup.dismiss()

        # check for non-empty list i.e file selected:
        if self.file_path:
            self.ids.get_file.text = self.file_path


Builder.load_file('app_design_FINAL.kv')


class AppAnalizer(App):

    def build(self):
        return Tab()


if __name__ == "__main__":
    AppAnalizer().run()


