def hextodex(num):

    if len(num) == 0:
        return "please input real number"
    if len(num) == 1:
        print(f"your decimal sum is {hexNumbers[num]}")
    if len(num) > 1:
        sum = 0
        for i in range(len(num)-1, -1, -1):
                print(i)
                print(num[i])
                print(hexNumbers[num[i]])
                sum = sum +(hexNumbers[num[i]])*(16**i)
                print(f"your decimal sum is {sum}")

hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

hextodex('ABCD')
