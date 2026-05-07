import pyttsx3
engine = pyttsx3.init()


engine.say("I will speak this text")
engine.runAndWait()

import os

# specify directory path
path = "."

# list all files and folders
contents = os.listdir(path)

print("Contents of directory:")
for item in contents:
    print(item)