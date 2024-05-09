# Swing-up Control of the Acrobot

TODO project description

## What's included?
All of the project code lives in the iPython notebook titled `acrobot.ipynb`. There is explanatory text within the notebook describing each section's purpose. The core of the optimization is in the function `acrobot_swing_up`, which takes in boundary conditions and references to dynamics and cost functions (for which multiple options are defined in the notebook).

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
- DOI:10.1016/j.ifacol.2016.10.194
- Russ Tedrake. Underactuated Robotics: Algorithms for Walking, Running, Swimming, Flying, and Manipulation (Course Notes for MIT 6.832). Downloaded on April 29, 2024 from https://underactuated.csail.mit.edu/.