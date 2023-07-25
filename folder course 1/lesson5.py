#if (10%2==0):
 #   print(yes)
#
#number = int(input("nhâp số nguyên vào"))
#if number%2==0:
    #print("Yes")
#else:
   # print("no")
#number = int(input("nhập vào một số"))
#if number>16:
  #  print("True")
#else:
   # print("false")
#number = int(input("điểm trung bình của hs"))
#if number<5:
   # print("kém")
#elif number<=5 and number<=6:
   # print("trung bình")
#elif number<=6 and number<=7 and number<=8:
   # print("khá")
#else:
 #   print("giỏi")
number_1 = int(input("Nhập số nguyên 1: "))
number_2 = int(input("Nhập số nguyên 2: "))
number_3 = int(input("Nhập số nguyên 3: "))
if number_1>=number_2 and number_1>=number_3:
    print("number_1 là số lớn nhất")
elif number_2>=number_1 and number_2>=number_3:
    print("number_2 là số lớn nhất")
else :
    print("number_3 là số lớn nhất")


