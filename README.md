# Swing-up Control of the Acrobot

TODO project description

## What's in the box?
TODO File descriptions

## Requirements
- ffmpeg (for generating animation)
- YAPSS

### Installing ffmpeg
MacOSX does not ship with ffmpeg installed by default. The easiest way to get ffmpeg is via Homebrew:

```bash
brew install ffmpeg
```

If on Linux, similarly use apt:

```bash
sudo apt install ffmpeg
```

## Notes
- Casadi doesn't support np.linalg.inv
- YAPSS doesn't support multiplying a numpy array by a float
- Casadi or YAPSS? doesn't support np.linalg.det

## References
- Mark Spong, "The Swingup Control Problem for the Acrobot", IEEE Control Systems Magazine, vol. 15, no. 1, pp. 49-55, February, 1995.
- Mark W. Spong, "Energy Based Control of a Class of Underactuated Mechanical Systems", Proceedings of the 1996 IFAC World Congress, 1996.
- Mark W. Spong, "Swing up control of the Acrobot", Proceedings of the IEEE International Conference on Robotics and Automation (ICRA), pp. 2356-2361, 1994. 