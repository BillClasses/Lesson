print("HỆ THỐNG TÍNH TIỀN GIỮ XE")
print()
print("hãy nhập thời gian giữ xe của bạn")
a = int(input("nhập vào số giờ giữ xe: "))
b = int(input("nhập vào số phút giữ xe: "))
money = 0
print("tổng thời gian của bạn là:",a,"giờ",b, "phút" )
total_minutes = a * 60 + b
if total_minutes <=20:
    money = 0.00
    #print(" tổng số tiền bạn phải trả là 0.00")
elif total_minutes <=60:
    money = 1.50
   # print("tổng số tiền bạn phải trả là 1.50")
elif total_minutes <=120:
    money = 3.50
else:  
    money = 5.00
print("tổng số tiền cần trả: ",money, "$")
require = input("bạn có cần xuất hóa đơn không N for no, Y for yes:")
pay = float(input("Số tiền bạn thanh toán : "))
while pay<money:
        pay = float(input("nhập số tiền bạn trả: "))
if require == "Y":
    print("đang xuất hóa đơn")
    print("--- HÓA ĐƠN PHÍ GỮI XE---")
    print("số tiền thanh toán là: ", pay)
    print("số tiền dư: ",pay-money)
    print("CẢM ƠN HẸN GẶP LẠI")
if require =="N":
    print("CẢM ƠN HẸN GẶP LẠI")
