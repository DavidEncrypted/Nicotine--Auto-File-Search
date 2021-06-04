from pynicotine.pluginsystem import BasePlugin
from pynicotine.logfacility import log
import sys

def enable(plugins):
    global PLUGIN
    PLUGIN = Plugin(plugins)


def disable(plugins):
    global PLUGIN
    PLUGIN = None


class Plugin(BasePlugin):
    __name__ = "Now Playing Search"

    settings = {
        'filename': '',
    }
    metasettings = {
        'filename': {
            'description': 'Filename of search entries',
            'type': 'textview'},
    }

    def init(self):
        self.currentloadedfile = ""
        self.songs = []
        self.currentsong = 0

    def OutgoingGlobalSearchEvent(self, text):  # noqa
        return (self.get_next_search(text),)

    def get_next_search(self, text):
        if text == "!n":
            if self.currentloadedfile != self.settings['filename']:
                try:
                    self.songs = open(self.settings['filename'], 'r').readlines()

                    log.add(_("Opened search file, read {} lines".format(len(self.songs))))

                    self.currentloadedfile = self.settings['filename']
                    self.currentsong = 0
                except:
                    log.add(_("FAILED TO OPEN SEARCH FILE".format(self.currentsong, len(self.songs))))
                    return text
            if self.currentsong >= len(self.songs):
                return ""
            else:
                log.add(_("\nSearching song: {} / {}".format(self.currentsong, len(self.songs))))
                print("{} / {}".format(self.currentsong, len(self.songs)))
                song = self.songs[self.currentsong]
                self.currentsong = self.currentsong + 1
                return song
        return text
