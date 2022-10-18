from gtts import gTTS
import os


#THIS FILE SHOULD NOT BE USED WITHOUT INTERNET,
#THIS FILE WAS JUST CREATED TO DOWNLOAD MP3
#THIS USES GOOGLE API 
# FILE READER WITH VOICE SPEECH GENERATOR USING GTTS

fileName = 'VoicePrompts.txt'

file1 = open(fileName, 'r')

doesExists = lambda x:os.path.exists(fileName)
if not (doesExists(fileName)):
    file1 = open(fileName)  
    
    
Lines = file1.readlines()
    
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    phrase = format(line.strip())
    # print(phrase)
    try:
        TEXT_TO_CONVERT = phrase

        language = 'en'
        myobj = gTTS(text=TEXT_TO_CONVERT, lang=language, slow=False)

        # myobj.save("EntranceSpeech.mp3")
        myobj.save("%s.wav" % os.path.join("src/voice",phrase))
    
    
    except:
        print("Error Generating MP3, Please check the Internet connection and or directory")