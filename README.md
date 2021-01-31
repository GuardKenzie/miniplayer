# Miniplayer

A curses based mpd client with basic functionality and album art written for the Kitty terminal.

After installation, the player can be opened from Kitty with `miniplayer`.

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

The config file is located at `~/.config/miniplayer/config`. The example configuration file, `config.example`, has all the default values.

#### player
* ***music_directory*:** The path to your music directory for extracting album art.
* ***font_width*:** The width of your font in pixels in the actual terminal.
* ***font_height*:** The height of your font in pixels in the actual terminal.

#### mpd
* ***host*:** The mpd host
* ***port*:** The mpd port

![font-example](https://github.com/GuardKenzie/miniplayer/blob/main/img/font.png?raw=true)

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
