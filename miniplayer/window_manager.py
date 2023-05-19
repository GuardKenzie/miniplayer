from .mpd_interface import MPDClient
from .config import Config
from .views.playlist_view import playlist_view

import urwid

main = playlist_view()
urwid.MainLoop(main).run()