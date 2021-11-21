# Miniplayer

A curses based mpd client with basic functionality and album art.

![player-preview](https://github.com/GuardKenzie/miniplayer/blob/main/img/preview.png?raw=true)

After installation, the player can be opened from the terminal with `miniplayer`.

## Installation

This package can be installed by:
1. Cloning this repository to your computer and running
```
python setup.py install
```
2. Through PyPi with
```
pip install miniplayer
```
3. By installing the `miniplayer-git` package with your AUR package manager of choice.

## Configuration

The config file is located at `~/.config/miniplayer/config`. The example configuration file, [`config.example`](config.example), has all the default values. You will need to create the file yourself.

#### player
* ***font_width*:** The width of your font in pixels in the actual terminal.
* ***font_height*:** The height of your font in pixels in the actual terminal.

    ![font-example](https://github.com/GuardKenzie/miniplayer/blob/main/img/font.png?raw=true)

* ***volume_step*:** The ammount (in percents) the volume will be adjusted on pressing the volume up and volume down keys.
* ***album_art_only*:** Whether or not to only draw the album art and no other track info (`true/false`).
* ***auto_close*:** Whether or not to automatically close the player once the mpd playlist has concluded (`true/false`).
* ***show_playlist*:** Whether or not to show the playlist view.

#### art
* ***music_directory*:** The path to your music directory for extracting album art from the files.
* ***http_base_url*:** Base URL of webserver which serves the album art for your albums (takes precedence over `music_directory`). Useful for users of Android MPD clients _MAFA_ or _MPDroid_. For more information see [the MPDroid wiki](https://github.com/abarisain/dmix/wiki/Album-Art-on-your-LAN).
* ***http_cover_filenames*:** Space separated list of filenames to use in the call to the webserver to fetch the album art.
* ***image_method*:** The method to use for drawing album art. Available values are `pixcat` and `ueberzug`
    If you are not using Kitty, try `ueberzug`.

#### mpd
* ***host*:** The mpd host
* ***port*:** The mpd port
* ***pass*:** The mpd password


#### keybindings
This section allows you to change the keybinds for the player. The format for a keybind is `key = action` (for example `p = play_pause` or `left = last_track`). Available actions are
* `play_pause`
* `next_track`
* `last_track`
* `volume_down`
* `volume_up`
* `toggle_info`
* `help`
* `quit`
* `select_down`
* `select_up`
* `select`


#### theme
This section allows you to customise the colors and progress bar
* ***accent_color*:** The color to use for selections in the playlist 
* ***bar_color*:** The color for the progress bar 
* ***time_color*:** The color for the time stamp
* ***bar_body*:** A single character to use for the body of the progress bar
* ***bar_head*:** A single character to use for the head of the progress bar

The following terminal colors can be used:
* `black`
* `red`
* `green`
* `yellow`
* `blue`
* `magenta`
* `cyan`
* `white`
* `auto`

If the `auto` color is specified, the player will try to determine the dominant color in the album art and use that.


## Default keybinds

| Key   | function           |
| ----- | ------------------ |
| h     | Show keybinds      |
| p     | Play/pause         |
| >     | Next track         |
| <     | Last track         |
| q     | Quit               |
| +     | Volume up          |
| -     | Volume down        |
| i     | Toggle info        |
| Up    | Selection up       |
| Down  | Selection down     |
| Enter | Play selected song |

These keybinds can be changed by editing the config file. See the [`config.example`](config.example) file for the format.
    

## F.A.Q.
- **Q:** Album art is not showing up.  
   **A:** If you're using `music_directory` for fetching your album art, make sure your it is not quoted i.e. if your music directory is `~/My Music` then your config should look like `music_directory = ~/My Music`.  
   If this does not work, try changing `image_method` from `pixcat` to `ueberzug` or vice versa.

- **Q:** Album art is too big/too small.  
   **A:** You need to configure `font_height` and `font_width`. Their values should be the actual pixel height and width of a character in your terminal.


## More screenshots!

![playlist](img/playlist.png)
