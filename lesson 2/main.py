# Phương thức
'''Không trả về'''
def sum(a,b):
    print("Tổng là: {0}".format(a + b))

sum(3, 7)


# Hàm
'''Có giá trị trả về'''
def checkbool(boan):
    if boan is False: return True
    else: return False

print("Check bool: {0}".format(checkbool(False)))

# Viết một chương trình Python để đếm số lượng ký tự trong một chuỗi nhập từ người dùng.
chuoi = input("Nhap vao 1 chuoi ngau nhien: ")
def xulychuoi(chuoi):
    result = 0
    for i in chuoi:
        result += 1
    return result

def chuoixuly(chuoi):
    result = 0
    for i in chuoi:
        result += 1
    print("chuoi nay dai {} ky tu".format(result))

chuoixuly(chuoi)
print(xulychuoi(chuoi), "ky tu")

# Tạo một danh sách các số nguyên. Viết một phương thức để đếm số lượng số lẻ trong danh sách.
list = [123, 456, 789, 222, 333, 444, 777]
def demsole(list):
    tongsole = 0
    for i in list:
        if i % 2 != 0:
            tongsole += 1

    print("Tong cac so le trong danh sach la: {}".format(tongsole))

demsole(list)

# Cho một danh sách các chuỗi, hãy viết một hàm để đếm số lượng chuỗi có độ dài lớn hơn hoặc bằng 5.
danhsachnhieuchuoi = ["cohaibao", "mobahongkong", "phiphaisongdaithanhhuyenthoai", "lienquanthangbaitaikynang"]
def xulychuoi(lst):
    counter = 0
    for i in lst:
        counter +=1
    if counter >= 5:
        print(i)

xulychuoi(danhsachnhieuchuoi)

# Viết một phương thức để đếm số lượng số chia hết cho 3 trong một dãy số nguyên từ 1 đến N.
n = int(input("Nhap so nguyen: "))
def demsoluongchiahetcho3(n):
    total = 0
    lstchiahetcho3 = []
    for i in range(1, n + 1):
        lstchiahetcho3.append(i)
    for i in range(1, n + 1):
        if i % 3 == 0:
            total += 1
        return total
    print(demsoluongchiahetcho3 (n))

# Tạo một lớp đại diện cho một hình tròn. Viết các phương thức để tính diện tích và chu vi của hình tròn.
# Viết một chương trình Python để đếm số lượng từ trong một câu nhập từ người dùng.
# Tạo một lớp đại diện cho một sách. Viết các phương thức để thêm sách mới, đếm tổng số lượng sách và in ra thông tin về các cuốn sách.
# Cho một danh sách các số thực, viết một hàm để đếm số lượng số âm trong danh sách.
# Viết một phương thức Python để kiểm tra xem một chuỗi có phải là chuỗi palindrome hay không.
# Tạo một lớp đại diện cho một người. Viết các phương thức để nhập thông tin cá nhân, đếm số lượng người đã được tạo và hiển thị thông tin của mỗi người.