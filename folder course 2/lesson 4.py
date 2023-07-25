#doc = open("vanban.txt", "r")
#"r" - Read - Default value. Opens a file for reading, error if the file does not exist
# #"a" - Append - Opens a file for appending, creates the file if it does not exist
# #"w" - Write - Opens a file for writing, creates the file if it does not exist
# #"x" - Create - Creates the specified file, returns an error if the file exists

#print(doc.read(5))
#print(doc.readline())
#đọc toàn bộ file text
#for i in doc:   #in toan bo
    #print(i)# van ban
#đóng file
#doc.close()

#print(doc.read())  
'''doc = open("vanban.txt", "w")
doc.write(" My city is HOChiMinh")
doc.close
doc = open("vanban.txt", "r")
print(doc.read())'''

"a" #Append - will append to the end of the file

"w"  #Write - will overwrite any existing content
'''
#bt1
doc = open("l4.txt", "x")

doc.write("My name is...")
doc.close
doc = open("l4.txt", "r")
print(doc.read())
'''


#xoa file
'''import os
os.remove("vanban.txt")
# xóa file nếu tồn tại
if os.path.exists("vanban.txt"):
    os.remove("vanban.txt")
else:
    print("this file doesm't exists")
#xóa folder rỗng
os.rmdir("hi")
'''



#bt 2
doc = open("locate.txt", "w")
doc.write("I have lived here for many years\n")
doc.write("I love this place\n")
#a
doc = open("locate.txt", "r")
print(doc.read())
#b
doc = open("locate.txt", "a")
doc.write("i live in Binh Thanh dist\n")
doc = open("locate.txt", "r")
print(doc.read())










