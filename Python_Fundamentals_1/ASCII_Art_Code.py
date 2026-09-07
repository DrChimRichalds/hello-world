# Python code​​​​​‌​​​​​​​‌‌​‌‌​‌​‌​​‌​‌​​‌​ below

def encodeString(myword):
    print(myword.split())
    new_list = [(char, myword.count(char)) for char in set(myword)]
    print(new_list)
    
def decodeString(encodedList):
    # Your code goes here.
    result = ""
    for char, count in encodedList:
        result = result + char*count
        print(result)

encodeString('AAACCCCAA')

decodeString([('A', 4), ('C', 4), ('D', 3)])

#it'd be easy to iterate through and craete
#  a new list that represents the string as a list, 
# then i wonder if I can iterate through a list and 
# create a count in a dictionary where the value + 
