# DJI HD FPV Helper Scripts
This repository is dedicated to helper scripts used on the host machine to help with different tasks like image conversion.

## Installation
Clone the repository and use [pipenv](https://pipenv.pypa.io/en/latest/) to install the dependencies:

```
pipenv shell
pipenv install
```

## Features

### Convert images to Screensaver images
On the DJI goggles there are two images used as screensaver images:

* `/system/gui/screen01.data`
* `/system/gui/screen02.data`

Those can be swapped with custom images, given that the correct format is provided. `screen_convert.py` will convert any image with the correct size (**1440x810**) into a raw image that can be displayed by the goggles:

```
python screen_convert.py source.png screen01_new.data
```

> A correctly converted image should alway have the size of **4665600** bytes.

This converted image can then be pushed to the goggles via adb:

```
adb push screen01_new.data /system/gui/screen01.data
# or to replace the second image:
adb push screen01_new.data /system/gui/screen02.data
```

> For some reason pushing this file might result in the file not being completely written, in this case try to transmit again or push the file to a different place and simply use `mv` on the goggles to move it into the correct place.
