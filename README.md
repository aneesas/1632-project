# Swing-up Control of the Acrobot

TODO project description

## What's included?
All of the project code lives in the iPython notebook titled `acrobot.ipynb`. There is explanatory text within the notebook describing each section's purpose.

## Requirements
Required packages found on [PyPI](https://pypi.org/) are listed in `requirements.txt` and can be installed via `pip` or similar. Additionally, the following tools are needed to run the included iPython notebook:

- ffmpeg (for generating animation)
- YAPSS v1.0.0-alpha.1

### Installing ffmpeg
MacOSX does not ship with ffmpeg installed by default. The easiest way to get ffmpeg is via [Homebrew](https://brew.sh/):

```bash
brew install ffmpeg
```

If on Linux, similarly use apt:

```bash
sudo apt install ffmpeg
```

The notebook kernel may need to be restarted after installation.

## References
- Mark Spong, "The Swingup Control Problem for the Acrobot", IEEE Control Systems Magazine, vol. 15, no. 1, pp. 49-55, February, 1995.
- Mark W. Spong, "Energy Based Control of a Class of Underactuated Mechanical Systems", Proceedings of the 1996 IFAC World Congress, 1996.
- Mark W. Spong, "Swing up control of the Acrobot", Proceedings of the IEEE International Conference on Robotics and Automation (ICRA), pp. 2356-2361, 1994.
- DOI:10.1016/j.ifacol.2016.10.194