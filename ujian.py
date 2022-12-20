# bahasa_pemograman

print ("No.1")
a = “saya belajar Bahasa Pemrograman menggunakan python”
print (a)

print ("No.2")
print ("Menghitung Luas Segitiga")

a = float(input("Masukkan alas: "))
t = float(input("Masukkan tinggi: "))
luas = 0.5*a*t
print (luas) 

print ("No.3")
print ("============")
print ("PROGRAM QUIZ")
print ("============")

str(input("Masukkan Nama: "))
int(input("Masukkan NIM: "))

print("No.4")
print ("============")
names = ['Kalimantan', 'Sumatra', 'Sulawesi']
for name in names:
    count = 0
    while count < 1:
        print(name, end= ' West ' " ")
        print(name, end= ' North ' " ")
        print(name, end= ' South ' " ")
        count = count + 1
    print()
    
print("No.5")
print ("============")
print ("NIM : 12345567")
print ("NAMA : QWERTY")

while True:
    print("Pilihan")
    print("1. capucino")
    print("2. teh")
    print("3. Exit")
    choice = int(input("masukkan pilihan : "))
    if choice == 1:
        print("memilih capucino")
        print ("masukan harga: 5000")
        a = 5000 * 0.10
        b = 5000 + a
        print ("Jumlah yang harus di bayarkan : ",b)
    elif choice == 2:
        print ("memilih teh")
        print("masukan harga: 3000 ")
        c = 3000 * 0.10
        d = 3000 + c
        print ("Jumlah yang harus di bayarkan : ",d)
    else : break


