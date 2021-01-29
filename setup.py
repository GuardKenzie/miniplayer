from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name="miniplayer",
      version="1.0",
      description="An mpd client with album art and basic functionality written for use with the kitty terminal.",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/GuardKenzie/miniplayer",
      author="Tristan Ferrua",
      author_email="tristanferrua@gmail.com",
      license="MIT",
      scripts=["bin/miniplayer"],
      install_requires=[
          "python-mpd2",
          "ffmpeg-python",
          "pixcat",
          "pillow"
      ])

