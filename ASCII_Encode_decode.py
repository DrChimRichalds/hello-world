# Python code​​​​​‌​​​​​‌​​‌‌‌​​​​‌‌​​​​‌​‌‌ below
import json 
import os 
import importlib.resources

def encodeString(stringVal):
    encodedList = []
    prevChar = None
    count = 0
    for char in stringVal:
        if prevChar != char and prevChar is not None:
            encodedList.append((prevChar, count))
            count = 0
        prevChar = char
        count = count + 1
    encodedList.append((prevChar, count))
    return encodedList

def decodeString(encodedList):
    decodedStr = ''
    for item in encodedList:
        decodedStr = decodedStr + item[0] * item[1]
    print(decodedStr)
    return decodedStr

# The filename that will be passed to this function
# is 10_04_challenge_art.txt
def encodeFile(filename, newFilename):
    with open(filename, 'r') as f:
        data = f.read()
        encoded_data = encodeString(data)
    with open(newFilename, 'w') as f:
        json.dump(encoded_data, f)
    return newFilename
    


def decodeFile(filename):
    with open(filename, 'r') as f:
        data = f.read()
        decoded_data = decodeString(data)
    with open(filename, 'w') as f:
        json.loads(decoded_data)

# decodeFile("/Users/charlesmullins/Documents/Documents - Charles’s MacBook Air/2026/LI_Courses/Ex_Files_Python_EssT/10_04_challenge_art_encoded.txt")

    
    
# encodeString("Hello World!")
# decodeString([('H', 1), ('e', 1), ('l', 2), ('o', 1), (' ', 1), ('W', 1), ('o', 1), ('r', 1), ('l', 1), ('d', 1), ('!', 1)])

original_filesize = os.path.getsize("10_04_challenge_art_second.txt.rtf")
print(f'Original file size: {original_filesize}')
# # Answer.encodeFile('10_04_challenge_art.txt', '10_04_challenge_art_encoded.txt')


# new_filesize = os.path.getsize("/Users/charlesmullins/Documents/Documents - Charles’s MacBook Air/2026/LI_Courses/Ex_Files_Python_EssT/10_04_challenge_art_encoded.txt")
# print(f'New file size: {new_filesize}')
# decoded = decodeFile("/Users/charlesmullins/Documents/Documents - Charles’s MacBook Air/2026/LI_Courses/Ex_Files_Python_EssT/10_04_challenge_art_encoded.txt")
# print(decoded)