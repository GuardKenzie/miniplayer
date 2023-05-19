import os
import toml
from pathlib import Path

CONFIG_FOLDER               = Path(os.environ.get("XDG_CONFIG_HOME", "~/.config")).expanduser()
MINIPLAYER_CONFIG_FOLDER    = CONFIG_FOLDER / "miniplayer"
MINIPLAYER_MAIN_CONFIG_FILE = MINIPLAYER_CONFIG_FOLDER / "config.toml"

class Config:
    def __init__(self):
        # Read the config
        with open(MINIPLAYER_MAIN_CONFIG_FILE, "r") as f:
            self.config = toml.loads(f.read())
        
        self.mpd   = self.config.get("mpd",
            {
                "host": "localhost",
                "port": 6600
            }
        )

        self.chafa = self.config.get("chafa",
            {
                "graphics": "symbols"
            }
        )