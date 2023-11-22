print("")
print("====Nomor 1 Data Diri====")
def profil(nama,alamat,gender,umur,hobby):
    print("nama saya adalah",nama)
    print("tinggal di",alamat)
    print("gender saya",gender)
    print("umur saya",umur)
    print("hobby saya",hobby)

profil("Adis Rain","Bogor","Laki-Laki","18 tahun","Futsal")

print("")
print("====Nomor 2 Mencari Nilai Kelulusan====")
def menentukan_kelulusan(nilai):
    if nilai<60:
        return "Gagal"
    elif 61<= nilai <=70:
        return "Baik"
    elif 71<= nilai <=80:
        return "Sangat Baik"
    elif 81<= nilai <=100:
        return "Istimewa"
    else:
        return "Masukan Nilai"

nilai=89    
print(menentukan_kelulusan(nilai))

print("")
print("====Nomor 3 Mencari Mencetak Bilangan Ganjil====")
def cetak_bilangan_ganjil(nilai):
    for i in range(1,nilai+1,2):
        print(i)

cetak_bilangan_ganjil(100)