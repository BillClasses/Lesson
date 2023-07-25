#chuỗi là tất cả các nội dung được đặt trong " " (' ')
# name = "Nam"
#integer (int) là các số nguyên 8 10 0 -5 
#dictionary gồm các phần tử là items(keys- values) {}
#list []
animal = ['dog','cat','monkey','duck','snake']
#in ra giá trị của phần tử thứ n thì ta dùng index n-1
name = "Hoai Nam"
#để in các giá trị trong khoảng a,b ta dùng [a:b+1]
#[start:end:step]
#len() => trả giá trị về độ dài list hay chuỗi
#append(phantu) thêm phần tử vào cuối mảng
#animal.append("gorilla")
#insert(vitri, phan) thêm phần tử vào vị trí chỉ định
animal.insert(3,"gorilla")
#pop(vitri) xóa phần tử tại vị trí
animal.pop(3)
#remove(phantu) xóa phần tử chỉ định
animal.remove("snake")
print(animal)

"""tạo list gồm có : chó, mèo, gà, vịt
1 dùng index dương lấy ra con mèo
2 dùng index âm lấy ra con vịt
3 dùng slicing lấy ra mèo gà vịt
4 thêm heo vào cuối list
5 thêm lợn vào đầu list
6 print các con vật từ vị trí thứ 2 đến vị trí kế cuối
7 thay đổi con đầu tiên thành con hổ
8 xóa con vịt đi
9 xóa con cuối cùng
10 xóa con cuối cùng và xem nó là con gì
"""
#1
animal =["dog","cat","chicken","duck"]
print(animal[1])
#2
print(animal[-1])
#3
print(animal[1:4])
#4
animal.append("pig")
print(animal)
#5
animal.insert(0,'pig1')
print(animal)
#6
print(animal[1:-1])
#7
animal[0]= "tiger"
print(animal)
#8
animal.remove("duck")
print(animal)
#9
animal.pop(4)
print(animal)
#10
animal.pop()
print(animal)