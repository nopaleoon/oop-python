
class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = 0.0
        
    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Jurusan: {self.jurusan}")
        print(f"Ipk : {self.ipk}")
        
    def update_ipk(self, new_ipk):
        self.ipk = new_ipk
        print(f"Ipk {self.nama} : telah diperbarui")
        
    def info_lulus(self, min_ipk=3.0):
        if self.ipk >= min_ipk:
            print(f"{self.nama} telah lulus.")
        else:
            print(f"{self.nama} belum lulus.")
        
#membuat objek (Mahasiswa)
mhs1 = Mahasiswa("Naufal", "L250046", "Teknik Informatika")

#menggunakan method untuk menampilkan info
mhs1.tampilkan_info()
print('------------')
mhs1.update_ipk(3.75)
print('------------')
mhs1.tampilkan_info()


mhs1.info_lulus() #Cek IPK mhs1

#pertanyaan
"""
1. Kenapa kita perlu untuk memanggil self. pada setiap atribut dan method di dalam kelas?
    Jawaban: Karena self adalah data yang terikat pada objek kelas. bukan data umum
    ~
-self → menunjuk ke object itu sendiri
-self.ipk → data yang disimpan di dalam object
-Tanpa self → bukan bagian dari object

2. Apa itu __init__?
__init__ adalah fungsi khusus yang otomatis dijalankan saat Anda membuat objek baru. 
Fungsinya adalah menginisialisasi (menyiapkan) data awal untuk objek tersebut.
        """
#Contoh penggunaan __init__:
class Siswa:
    def __init__(self, nama, ips):
        self.nama = nama
        self.ips = ips

# Saat Anda membuat objek, __init__ langsung jalan
siswa1 = Siswa("Budi", 3.5)
# __init__ otomatis dipanggil dengan nama="Budi", ips=3.5

#tanpa init__, Anda harus mengatur data secara manual setelah membuat objek, seperti ini:
class Siswa:
    pass

siswa1 = Siswa()
siswa1.nama = "Budi"  # ❌ Repot, harus manual
siswa1.ips = 3.5      # ❌ Repot, harus manual