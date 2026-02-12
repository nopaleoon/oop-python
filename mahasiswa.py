
class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ips = 0.0
        
    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Jurusan: {self.jurusan}")
        print(f"Ips : {self.ips}")
        
    def update_ips(self, new_ips):
        self.ips = new_ips
        print(f"Ips {self.nama} : telah diperbarui")
        
#membuat objek (Mahasiswa)
mhs1 = Mahasiswa("Naufal", "L250046", "Teknik Informatika")

#menggunakan method untuk menampilkan info
mhs1.tampilkan_info()
print('------------')
mhs1.update_ips(3.75)
print('------------')
mhs1.tampilkan_info()