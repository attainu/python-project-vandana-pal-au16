#!/user/bin/python
#-*-coding: utf-8-*-
# File organizer

import os
import shutil

audio = ['.mp3','.wma','.aac','.aif','.cda','.mid','.midi','.ogg','.wav','.wpl','.FLAC',]

video = ['.mp4','.wmv','.avi','.mkv','.3gp']

docs = ['.docx','.doc.pdf','.pptx','.xlsx','.rtf','.txt']

software = ['.exe','.apk']

zips = ['.zip','.rar','.7z','.arj','.deb','.pkg','.rpm','.tar.gz','.z','.deb']

image = ['.ai','.bmp','.gif','.jpeg','.png','.tif']


#path = os.getcwd()
#path = "E:\\junk\\lab1"
path = input('Enter your target path:')

#print(path)
#
files = os.listdir(path)

#print(files)

os.mkdir(path + '\\' + 'audio')
os.mkdir(path + '\\' + 'image')
os.mkdir(path + '\\' + 'video')
os.mkdir(path + '\\' + 'docs')
os.mkdir(path + '\\' + 'software')
os.mkdir(path + '\\' + 'zips')
os.mkdir(path + '\\' + 'unknown')

for files in files:
    extension = os.path.splitext(file)[1]

    #print(extension)

    if extension :
        files1 = os.listdir(path + '\\' + file)
        for file1 in files1:
            ext = os.path.splitext(file1)[1]
            newpath = path + '\\' + file + '\\'
            if text in audio:
                shutil.move(newpath + file1,path + '\\' + 'audio')
            elif ext in video:
                shutil.move(newpath + file1,path + '\\' + 'video')
            elif ext in image:
                shutil.move(newpath + file1,path + '\\' + 'image')
            elif ext in docs:
                shutil.move(newpath + file1,path + '\\' + 'docs')
            elif ext in software:
                shutil.move(newpath +file1,path + '\\' + 'software')
            elif ext in zips:
                shutil.move(newpath + file1,path + '\\' + 'zips')
            else:
                shutil.move(newpath + file1,path + '\\' + 'unknown')