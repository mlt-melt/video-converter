# Video Converter

The Video Converter is a software tool that allows the user to convert videos from one format to another, as well as to adjust the video's resolution and length. This software is written in Python and includes a graphical user interface (GUI) to make it easy for users to select their desired conversion settings.

## Installation

To use the Video Converter, you'll need to install Python 3.6 or later and the following Python packages:
- tkinter
- moviepy

These packages can be installed using pip:

```shell
    $ pip install tkinter
    $ pip install moviepy
```


## Usage

To use the Video Converter, follow these steps:

1. Open the command prompt or terminal and navigate to the directory where the video converter software is located.

2. Run the following command to start the software:

```shell
    $ python main.py
```

Or you can you build version. Just open ``build`` folder and start ``converter.exe``


3. The Video Converter GUI will open. Select your desired conversion settings:
- Start Position: The starting point in the video where the conversion should begin - in format XX:XX:XX (hours:minutes:seconds).
- Finish Position: The ending point in the video where the conversion should end - in format XX:XX:XX (hours:minutes:seconds).
- Output Extension: The output format of the converted video (mp4, avi, or mkv).
- Output Resolution: The output resolution of the converted video (1920:1080, 1280:720, or original resolution of input video).

4. Click the "Start convertation" button to begin the conversion process. The software will convert each video in the ``input`` folder according to the specified settings and save the resulting videos in the ``output`` folder.

5. After the conversion process is complete, a message box will appear indicating that the videos were converted successfully.

## Limitations

The Video Converter has the following limitations:

- Only supports video formats that can be read by the moviepy package (e.g. mp4, avi, and mkv).
- The converted video's quality may be reduced if the resolution is changed during the conversion process.
- The software may run slower or faster depending on the hardware of the computer it is running on and the size of the input video files.

## Contributing

If you find any bugs or issues with the Video Converter software, please feel free to open an issue on the Github repository or submit a pull request with your changes.

## License

The Video Converter software is licensed under the MIT License. Feel free to use and modify the software for your own purposes.