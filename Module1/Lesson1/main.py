import random

print("Hello World") # in ra bảng console

print("BIẾN VÀ TOÁN TỬ")


# variables
# tên_biến = dữ_liệu
a = 4
b = 6

# + - * / % // 
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a % b =", a % b)
print("a // b =", a // b)


'''________________________________________________________________'''


print("\nKIỂU DỮ LIỆU")

# Kiểu dữ liệu

# kiểu dữ liệu chữ
# Chuỗi (string) từ khóa là str
name = "thầy Bill"
print(type(name))
print(name)

# Kiểu dữ liệu số
age = 20 # int
age = 20.5 # float
print(type(age))
print(age)

# Kiểu dữ liệu logic
wibu_or_not = False
print(type(wibu_or_not))
print(wibu_or_not)


# Kiểu dữ liệu dãy 

# Danh sách (List)
lst = []
print(type(lst))
print(lst)

# Tập hợp (Tuple)
tple = ()
print(type(tple))
print(tple)


# Kiểu dữ liệu mapping (dạng bảng)

# Từ điển (Dictionary)
dct = {}
print(type(dct))
print(dct)


# Vòng lặp
name = "Bill"
# Vòng lặp for
for i in range(5):
    print("Bill")
'''
for <biến> in <tập hợp>:
    <lệnh thực thi>
    <lệnh thực thi>
    <lệnh thực thi>
'''
    
# Vòng lặp while
'''
while <điều kiện>:
    <lệnh thực thi>
    <lệnh thực thi>
    <lệnh thực thi>
'''
i = 0
while i < 5:
    print("Name")
    i += 1
