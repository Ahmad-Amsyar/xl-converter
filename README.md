<p align="center">
    <img src="icons/logo.svg" width="20%">
</p>
<h3 align="center">XL Converter</h3>

Powerful image converter for the latest formats with support for multithreading, drag 'n drop, and downscaling.

Available for Windows and Linux.

![](misc/screenshots/screenshot_0.png)

The [documentation](https://xl-docs.codepoems.eu)

## Supported Formats

Encode to **JPEG XL, AVIF, WEBP, and JPG**. Convert from **HEIF** and [more](https://xl-docs.codepoems.eu/supported-formats)

## Features
#### JPG Reconstruction

Reconstructs the original JPG from a JPEG XL file.

#### Multithreading

Speeds up JPEG XL encoding significantly.

#### Image Proxy

Avoid picky encoders. A proxy is generated when an encoder doesn't support a specific format.

For example, this enables HEIF -> JPEG XL conversion.

#### Downscaling

Scale down images to resolution, percent, shortest (and longest) side, or file size.

#### Smallest Lossless

Utilize multiple formats to achieve the smallest size.

![](misc/screenshots/screenshot_2.png)

#### Intelligent Effort

Optimizes `Effort` for smaller size.

#### Lossless (Only If Smaller)

Picks the smallest out of two.

## Bug Reports

You can submit a bug report in 2 ways
- \[public\] Submit a new [GitHub Issue](https://github.com/JacobDev1/xl-converter/issues)
- \[private\] Email me at contact@codepoems.eu

## Building from Source

### Windows 10

Prerequisites:
- Python `3.11.6` (with `pip`)
- `git`

Clone the repo.

```cmd
git clone -b v0.9.6 --depth 1 https://github.com/JacobDev1/xl-converter.git
cd xl-converter
```

Setup `venv`.

```cmd
python -m venv env
env\Scripts\activate.bat
pip install -r requirements.txt
```

Install redistributable

```cmd
misc\VC_redist.x64.exe
```

Run the application

```cmd
python main.py
```

You can also build it.

```cmd
python build.py
```

### Linux (Ubuntu-based)

Install packages.

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv git
sudo apt install '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev libxkbcommon-dev libxkbcommon-x11-dev
```

Clone and set up the repo.

```bash
git clone -b v0.9.6 --depth 1 https://github.com/JacobDev1/xl-converter.git
chmod -R +x xl-converter
cd xl-converter
```

Create and activate a virtual environment.

```bash
python3 -m venv env
source env/bin/activate
```

Install Python dependencies

```bash
pip install -r requirements.txt
```

Now, you can run it.

```bash
make run
```

...or build it.

```bash
make build
```

Extra building modes:
- `make build-7z` - package to a 7z file (with an installer) (requires `p7zip-full`)
- `make build-appimage` - package as an AppImage (requires `fuse`)

### Troubleshooting Build Issues

#### Building on Linux

The build may not be generated successfully, because `PyInstaller` sometimes clashes with virtual environments on Linux.

If the executable doesn't launch do the following.

Deactivate the virtual environment.

```bash
deactivate
```

Install packages globally.
```bash
pip install -r requirements.txt
```

Try again.

```bash
make build
```

#### Python Version on Linux

The project runs on Python `3.11.6`. The one in your repo should work, but If it doesn't use `pyenv` to get this one specifically. 

## Contributions

Pull requests are ignored to avoid potential legal complications when reusing the code.

Forward your code and feature suggestions to my email at contact@codepoems.eu