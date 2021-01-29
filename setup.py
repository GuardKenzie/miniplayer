from setuptools import setup

setup(name="miniplayer",
      version="1.0",
      description="An mpd client with album art and basic functionality written for use with the kitty terminal.",
      url="https://github.com/GuardKenzie/miniplayer",
      author="Tristan Ferrua",
      author_email="tristanferrua@gmail.com",
      license="MIT",
      scripts=["bin/miniplayer"],
      install_requires=[
          "python-mpd2",
          "ffmpeg",
          "pixcat",
          "pillow"
      ])

