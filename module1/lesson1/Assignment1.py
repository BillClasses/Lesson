# |1| Viết chương trình nhập vào một chuỗi và in ra độ dài của chuỗi đó.| 
print("bai1")
HY = input("Nhập chuỗi cmm vào😊: ")
print("Độ dài của chuỗi:", len(HY))
# |2| Viết chương trình nhập vào một chuỗi và in ra chuỗi đó được viết hoa (uppercase).|\
print("bai 2")
print("Chữ Chữ viết hoa của m đây 🥱: ", HY.upper())
# |3| Viết chương trình nhập vào một chuỗi và in ra chuỗi đó được viết thường (lowercase).|
print("bai 3")
print("Chữ viết thường 🐷: ", HY.lower())
# |4| Viết chương trình nhập vào hai chuỗi và nối chúng lại với nhau.|
print("bai 4")
TK= input("Nhập chuỗi 2: ")
print(HY + TK)
# |5| Viết chương trình nhập vào một chuỗi và loại bỏ tất cả các khoảng trắng ở đầu và cuối chuỗi.|
print("bai5")
print("Loại cmm khoản trắng ở đầu và cuối chuỗi😓 :", HY.strip())
# |6| Viết chương trình nhập vào một chuỗi và kiểm tra xem chuỗi đó có bắt đầu hoặc kết thúc bằng một chuỗi con nào đó không.|
print("bai6")
Đềlol3 = "🐧"
# Hello World
if HY.startswith(Đềlol3):
    print("chuỗi bắt đầu bằng chuỗi con")
elif HY.endswith(Đềlol3):
    print("Chuỗi kết thúc bằng chuỗi con")
else:
    print("chuỗi nào cũng dc miễn sao đéo ko bắt đầu hay kết thúc bằng chuỗi con >_<")
# |7| Viết chương trình nhập vào một chuỗi và tìm kiếm một chuỗi con nào đó trong chuỗi đó và in ra vị trí xuất hiện đầu tiên của chuỗi con đó.|
print("bai7")
lunuxuser = HY.find(Đềlol3)
if lunuxuser != -1:
    print("The chuỗi that appears in the first location is  : ", lunuxuser)
else:
    print("The chuỗi not spawn is: ")

# |8| Viết chương trình nhập vào một chuỗi và thay thế tất cả các ký tự trong chuỗi đó bằng một ký tự khác.|
# |9| Viết chương trình nhập vào một chuỗi và đảo ngược thứ tự các từ trong chuỗi đó.|
# |10| Viết chương trình nhập vào một chuỗi và in ra số lần xuất hiện của từng ký tự trong chuỗi đó.|
# |11| Viết chương trình nhập vào một chuỗi và in ra chuỗi đó chỉ bao gồm các ký tự không phân biệt hoa thường.|
# |12| Viết chương trình nhập vào hai chuỗi và kiểm tra xem chuỗi thứ nhất có chứa toàn bộ các ký tự của chuỗi thứ hai hay không.|
# |13| Viết chương trình nhập vào một chuỗi và tách chuỗi thành các từ riêng biệt, sau đó sắp xếp các từ theo thứ tự bảng chữ cái.|
# |14| Viết chương trình nhập vào một chuỗi và tạo ra một chuỗi mới bằng cách lặp lại các ký tự của chuỗi cũ nhưng bỏ qua ký tự lặp lại.|
# |15| Viết chương trình nhập vào một chuỗi và in ra các từ trong chuỗi được viết hoa (uppercase).|
# |16| Viết chương trình nhập vào một chuỗi và in ra các từ trong chuỗi được viết thường (lowercase).|
# |17| Viết chương trình nhập vào một chuỗi và in ra chuỗi đó với tất cả các từ viết hoa (capitalize).|
# |18| Viết chương trình nhập vào một chuỗi và in ra chuỗi đó bằng cách thay thế khoảng trắng bằng "_".|
# |19| Viết chương trình nhập vào một chuỗi và in ra những từ có độ dài lớn hơn hoặc bằng n.|
# |20| Viết chương trình nhập vào một chuỗi và kiểm tra xem chuỗi đó có phải là chuỗi palindrome hay không.|