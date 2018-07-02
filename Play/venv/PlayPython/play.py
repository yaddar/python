# file = open("C:/Users/yarona/Downloads/fruits.txt", "r")
# content = file.read()
# file.close()
# print(content)
#
# mylist = [1, 2, 3, 4, 5]
# for i in mylist:
#     print(i)
#
#
# a = "Tricky"
#
# for i in a[:3]:
#
#     print(i)
# mylist = [1, 2, 3, 4, 5]
# for i in mylist:
#     if i > 2:
#         print(i)

# mylist = ["Terribly Tricky"]
#
# for word in mylist:
#    for letter in word[-6:]:
#        print(letter)

import  os

os.listdir()

file = open("C:/Users/yarona/Downloads/fruits.txt", "r")
content = file.read()
# content =content.splitlines()
file.close()

for word in content.splitlines():
    print(len(word))