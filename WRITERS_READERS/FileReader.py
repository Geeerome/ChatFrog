import os


fileName = 'VoicePrompts.txt'


file1 = open(fileName, 'w')
# file1.writelines(L)

doesExists = lambda x:os.path.exists(fileName)
if not (doesExists(fileName)):
    file1 = open(fileName)    



# Using readlines()
def reads():
    file1 = open(fileName, 'r')
    Lines = file1.readlines()
    
    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        phrase = format(line.strip())
        return phrase
    
