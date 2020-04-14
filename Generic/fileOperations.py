#! python3
# Files and its operation
ROOT ='C:/Users/Meher Kiran/PycharmProjects/hello-world/Data/'

ran_file = open(ROOT+'test_file_1', 'r')  # open function has two params(path,mode)
"""Modes -->
'w' - Write (Every time you call this function, pointer points to starts of the file, and overwrites the file if data exists)
'a'- append (Pointer points to EOF,Without removing existing data , it appends new data to the file)
r - 'read' <-- the above three modes are for unicode (like files)
'wb', 'rb' <-- for binary code (like images,audio files)
"""
print(ran_file.readline())  # readline() reads only one line and pointer will be pointing to that very line

# writing data to a new file
wri_file = open(ROOT +'test_file_2', 'w')   # first checks in the root directory for specified file name, if not found it creates one
for data in ran_file:
    wri_file.write(data)

img = open(ROOT+'image.jpg', 'rb')
img_copy = open(ROOT + 'image_copy.jpg', 'wb')
for pix in img:
    img_copy.write(pix)




