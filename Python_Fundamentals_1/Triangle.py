
global count 


# Python code​​​​​‌​​​​​‌​​​​‌‌​‌‌‌​‌​‌‌​​​​ below
def triangle(num, *args):
    if num == 1:
        return num
    return num + triangle(num - 1)

def square(num, count = 0):
    entry_1 = triangle(num)
    entry_2 = triangle(num - 1)
    sum_triangles = entry_1 + entry_2
    return print(sum_triangles)

test_num = 7
(triangle(test_num))

(square(test_num))



