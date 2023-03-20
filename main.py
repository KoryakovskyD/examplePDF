import os
import time
import textract
import gtts
from PyPDF2 import PdfReader
from playsound import playsound
from os import listdir

def getSound(name, textPages):
    sound = gtts.gTTS(textPages)
    fullName = name + '.mp3'
    sound.save(fullName)

def getText(fileName):
    if '.pdf' in fileName:
        # pdf files
        reader = PdfReader(fileName)
        countPages = len(reader.pages)
        print("Count pages: ", countPages)
        pages = reader.pages[8]
        text = pages.extract_text().replace('\t', ' ').replace('\n', ' ')
        print(text.encode('utf-8'))
    elif '.docx' in fileName:
        # doc files
        textDocx = textract.process(fileName)
        text = str(textDocx).replace('\n', '').replace('\xc2', '').replace('\xa0', '')
        print(text)
    elif '.txt' in fileName:
        # txt files
        reader = open(fileName, 'r')
        text = str(reader.readlines())
        reader.close()
    return text


pathWithFiles = 'E:\\pythonFiles\\'
start = time.perf_counter()


# all files in path
for file in os.listdir(pathWithFiles):
    fullPath = pathWithFiles + file
    print(fullPath)
    getSound(file.split('.')[0], getText(fullPath))

end = time.perf_counter() - start
print(f"The time of execution of above program is: {end:0.4f} ms")



