from platform import platform

from kivy.app import App
from os.path import sep, expanduser, isdir, dirname

from kivy_garden.filebrowser import FileBrowser


class TestApp(App):

    def build(self):

        if platform == 'win':
            user_path = dirname(expanduser('~')) + sep + 'Documents'
        else:
            user_path = expanduser('~') + sep + 'Documents'
        browser = FileBrowser(select_string='Select',
                              favorites=[(user_path, 'Documents')])
        browser.bind(
                    on_success=self._fbrowser_success,
                    on_canceled=self._fbrowser_canceled)
        return browser

    def _fbrowser_canceled(self, instance):
        print('cancelled, Close self.')

    ###
    # if user successfully selected needed file
    # path for that file will be saved in selection
    # read-only ListProperty that will contain the list
    # of files that are currently selected
    ###
    def _fbrowser_success(self, instance):
        print(instance.selection)

TestApp().run()


