from moviepy.editor import *
import ffmpy
from os import walk
import tkinter.messagebox as mb
import random

def convert(outputExt, outputSize, firstCut, secondCut):
    print("output extention: ", outputExt)
    print("output size: ", outputSize)
    print("start cut: ", firstCut)
    print("finish cut: ", secondCut)

    def process(filename, fileExt):
        clip = VideoFileClip(f"input/{filename}{fileExt}")
        
        if secondCutInSec > 0 and firstCutInSec < secondCutInSec:
            clip = clip.subclip(firstCutInSec, secondCutInSec)
        
        if outputSize == '1280:720' or outputSize == '1920:1080':
            clip = clip.fx(vfx.resize, width = int(outputSize.split(":")[0]))
        
        outputName = f'output-{random.randint(0, 99999999)}'

        if outputExt == "mp4":
            clip.write_videofile(f"output/{outputName}.mp4", codec="libx264")
        elif outputExt == "avi":
            clip.write_videofile(f"output/{outputName}.avi", codec="rawvideo")
        elif outputExt == "mkv":
            clip.write_videofile(f"bin/temp/{outputName}.mp4", codec="mpeg4")
            ff = ffmpy.FFmpeg(
                executable='bin/ffmpeg/ffmpeg.exe',
                inputs={f'bin/temp/{outputName}.mp4': None},
                outputs={f'output/{outputName}.mkv': None}
            )
            ff.run() # and then convert to mkv

        clip.close()
    
    firstCutInSec = (int(firstCut.split(":")[0])*3600) + (int(firstCut.split(":")[1])*60) + int(firstCut.split(":")[2])
    secondCutInSec = (int(secondCut.split(":")[0])*3600) + (int(secondCut.split(":")[1])*60) + int(secondCut.split(":")[2])

    filenames = next(walk("input/"), (None, None, []))[2]  # [] if no file
    print(filenames)
    extentionsToWorkOn = [".mp4", ".avi", ".mkv"]
    for i in filenames:
        filename = i.split(".")[0]
        fileExt = f'.{i.split(".")[-1]}'
        if fileExt in extentionsToWorkOn:
            process(filename, fileExt)

    print("################\n\033[32m process finished \033[0m\n################")
    msg = "Процесс конвертации завершен! Конвертированные файлы будут сохранены в папку output"
    mb.showinfo("Процесс завершен", msg)