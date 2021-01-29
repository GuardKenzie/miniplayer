# Miniplayer

A curses based mpd client with basic functionality and album art written for the Kitty terminal.

## Configuration

The config file is located at `~/.config/miniplayer/config`. The example configuration file, `config.example`, has all the default values.

* ***music_directory*:** The path to your music directory for extracting album art.
* ***font_width*:** The width of your font in pixels in the actual terminal.
* ***font_height*:** The height of your font in pixels in the actual terminal.

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
