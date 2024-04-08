

'''color = ["red", "green","blue"]
color.append("black")
print(color)
color.remove("green")
print(len(color))
print(color)
color.pop()
print(color)
color.insert(1 ,"gray")
print(color)
color = ["red", "green","blue","red"]
try:
	print(color.index(input("Nhap PT:")))
except:
	print("Not Exist")

red_index = []
for i in range(len(color)):
	if color[i] == "red":
		red_index.append(i)

print(red_index)

print("So lan :" + str(color.count("red")))

a = [4,1,6,8,0,3,7,9,10,2,11]
a.sort()
print(a)

a[3] = "TrungTu"
print(a)'''

trung = [1,3,5,7,2,4,6,8,10,9]
print(trung)

trung.sort()
print("SORT(sap xep):" + str(trung))

trung.remove(3)
print("REMOVE(xoa):" + str(trung))

trung.pop()
print("POP(xoa ptu cuoi):" + str(trung))

trung.insert(3,7)
print("INSERTT(them ptu vao vi tri):" + str(trung))

trung.append(5)
print("APPEND(them ptu vao cuoi) :" + str(trung))

print("LEN (tong so ptu):" + str(len(trung)))

print("COUNT(so lan xuat hien:)" + str(trung.count(5)))

print("INDEX (tim vi tri 1 ptu):" + str(trung.index(7)))

trung[6] = "TrungTu"
print("[6] (thay doi ptu vi tri 6):" + str(trung))

cc = []
for i in range(len(trung)):
	if trung[i] == 5:
		cc.append(i)
print("list:" + str(trung))
print("Vi tri nhieu ptu (Vi tri so :5):" + str(cc))

