from ..mpd_interface import MPDInterface
import urwid

class PlaylistWidget(urwid.WidgetPlaceholder):
    def __init__(self):
        self.interface = MPDInterface()
        self.playlist = urwid.SimpleFocusListWalker([])
        self.update()

        self.overlay = False

        super(PlaylistWidget, self).__init__(urwid.ListBox(self.playlist))
        
    def update(self):
        self.playlist.clear()
    
        for song in self.interface.playlist:
            button = urwid.Text(str(song), wrap="clip")
            self.playlist.append(urwid.AttrMap(button, None, focus_map="reversed"))
        
    def close_popup(self):
        self.original_widget = self.original_widget.bottom_w
        self.overlay = False

    def open_popup(self):
        question = urwid.Text("Are you sure you want to clear the playlist?", align="center")
        
        confirm_button = urwid.Button("Do it!")
        deny_button    = urwid.Button("No!")

        def confirm(_):
            self.interface.clear_playlist()
            self.close_popup()
            self.update()

        def deny(_):
            self.close_popup()

        urwid.connect_signal(deny_button, 'click', deny)
        urwid.connect_signal(confirm_button, 'click', confirm)
        
        choices = urwid.GridFlow(
            [
                confirm_button,
                deny_button
            ],
            cell_width=10,
            h_sep=5,
            v_sep=0,
            align="center"
        )

        pad = urwid.Padding(choices, align="center", width=("relative", 75))
        
        widget = urwid.Filler(urwid.Pile([question, urwid.Divider(), pad]))

        self.original_widget = urwid.Overlay(
            urwid.LineBox(widget),
            self.original_widget,
            align="center",  width=("relative", 50),  min_width=30,
            valign="middle", height=("relative", 20), min_height=10
        )

        self.overlay = True

    def keypress(self, size, key):
        current_pos = self.playlist.get_focus()
        positions   = self.playlist.positions()

        if not self.overlay:
            if current_pos[1] is None:
                return

            elif key == "up":
                next_position = (current_pos[1] - 1) % len(positions)
                self.playlist.set_focus(next_position)

            elif key == "down":
                prev_position = (current_pos[1] + 1) % len(positions)
                self.playlist.set_focus(prev_position)

            elif key == "enter":
                self.interface.client.play(current_pos[1])
            
            elif key == "c":
                self.open_popup()

        else:
            return super(PlaylistWidget, self).keypress(size, key)