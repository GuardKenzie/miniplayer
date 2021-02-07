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

The config file is located at `~/.config/miniplayer/config`. The example configuration file, `config.example`, has all the default values. You will need to create the file yourself.

#### player
* ***music_directory*:** The path to your music directory for extracting album art.
* ***font_width*:** The width of your font in pixels in the actual terminal.
* ***font_height*:** The height of your font in pixels in the actual terminal.

    ![font-example](https://github.com/GuardKenzie/miniplayer/blob/main/img/font.png?raw=true)

* ***image_method*:** The method to use for drawing album art. Available values are `pixcat` and `ueberzug`
    If you are not using Kitty, try `ueberzug`.


#### mpd
* ***host*:** The mpd host
* ***port*:** The mpd port


## Keybinds

| Key | function      |
|-----|---------------|
| h   | Show keybinds |
| p   | Play/pause    |
| >   | Next track    |
| <   | Last track    |
| q   | Quit          |
| +   | Volume +5     |
| -   | Volume -5     |

    
## F.A.Q.
1. **Q:** Album art is not showing up.  
**A:** Make sure your `music_directory` is not quoted i.e. if your music directory is `~/My Music` then your config should look like `music_directory = ~/My Music`.  
If this does not work, try changing `image_method` from `pixcat` to `ueberzug` or vice versa.

2. **Q:** Album art is too big/too small.  
**A:** You need to configure `font_height` and `font_width`. Their values should be the actual pixel height and width of a character in your terminal.
