#No 1
kendaraan = [ "Mobil","Lamborgini", 6500, "Biru", 4]
print(kendaraan)

kendaraan = [ "Mobil","Lamborgini", 6500, "Biru", 4]
kendaraan.append ("Rp 61.4 M")
print(kendaraan)

kendaraan = [ "Mobil","Lamborgini", 6500, "Biru", 4]
kendaraan.append ("Rp 61.4 M")
kendaraan.append ("Kopling")
print(kendaraan)

kendaraan = [ "Mobil","Lamborgini", 6500, "Biru", 4]
kendaraan.append ("Rp 61.4 M")
kendaraan.append ("Kopling")
kendaraan.insert (2, "Veneno")
print(kendaraan)

#No 2

print("""Selamat datang di aplikasi menghitung luas bangun datar.
Silahkan pilih salah satu menu dibawah ini:
1. Menghitung Luas Persegi
2. Menghitung Luas Lingkaran
3. Menghitung Luas Segitiga
""")

pilihan = int(input("Masukan Pilihan Kamu"))

match pilihan:
    case 1:
        print("Kamu memilih 1, Menghitung Luas Persegi")
        sisi = int(input("Masukan Sisi Persegi"))
        Lpersegi = sisi*sisi
        print("Luas Persegi dengan", sisi, "adalah", Lpersegi)

    case 2:
        print("Kamu memilih 2, Menghitung Luas Lingkaran")
        r = float(input("Masukan Jari-jari Lingkaran"))
        Llingkaran = 3.14*r*r
        print("Luas Lingkaran dengan", r, "adalah", int(Llingkaran))

    case 3:
        print("Kamu memilih 3, Menghitung Luas Segitiga")
        alas = int(input("Masukan Alas Segitiga"))
        tinggi = int(input("Masukan Tinggi Segitiga"))
        LSegitiga = 1/2 * alas * tinggi
        print ("Luas Segitiga adalah", int(LSegitiga))

    case _:
        print("Salah memilih pilihan")