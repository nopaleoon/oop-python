class Mahasiswa:
    def __init__(self, nama, jurusan, ipk):
        self.nama = nama
        self.jurusan = jurusan
        self.ipk = ipk

    def tampilkan_info(self):
        print(self.nama, "-", self.jurusan, "-", self.ipk)
        
    #manipulasi data
    def update_ipk(self, ipk_baru):
        self.ipk = ipk_baru

        
mhs1 = Mahasiswa("Naufal", "Informatika", 3.8)
mhs2 = Mahasiswa("Rizky", "Sistem Informasi", 3.5)
mhs3 = Mahasiswa("Dina", "Teknik Komputer", 3.9)

daftar_mahasiswa = [mhs1, mhs2, mhs3]

for mhs in daftar_mahasiswa:
    mhs.tampilkan_info()

#contoh penggunaan method untuk manipulasi data
print()
mhs1.update_ipk(3.9)

#menampilkan mahasiswa dengan ipk > 3.5
for mhs in daftar_mahasiswa:
    if mhs.ipk > 3.5:
        mhs.tampilkan_info() 
        
print()

#latihan mandiri

class Mahasiswa2:
    def __init__(self, nama, ipk):
        self.nama = nama
        self.ipk = ipk
        
    def info(self):
        print(f"{self.nama} - {self.ipk}")
        
m1 = Mahasiswa2("Dio", 3.0)
m2 = Mahasiswa2("Tono", 3.5)
m3 = Mahasiswa2("Budi", 3.2)

daftar_mhs = [m1, m2, m3]

for mhs in daftar_mhs:
    if mhs.ipk > 3.0:
        mhs.info()
        
        
a = Mahasiswa2("Andi")
b = a

b.nama = "Tio"

print(a.nama) #outputnya Tio, karena a dan b menunjuk ke object yang sama