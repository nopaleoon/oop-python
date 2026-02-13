
class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.__ipk = 0.0 #encapsulation
        
    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"Ipk : {self.__ipk}")
        
    def set_ipk(self, nilai):
        if 0.0 <= nilai <= 4.0:
            self.__ipk = nilai
            print('IPK berhasil diperbarui')
        else:
            print("IPK harus antara 0.0 dan 4.0")
            
    def get_ipk(self):
        return self.__ipk
    
    def info_lulus(self, min_ipk=3.0):
        if self.__ipk >= min_ipk:
            print(f"{self.nama} telah lulus.")
        else:
            print(f"{self.nama} belum mencapai IPK minimal")
            
mhs1 = Mahasiswa("Naufal Fikri", "L200250046", "TI")
mhs1.set_ipk(2.75)
print(f"IPK sekarang : {mhs1.get_ipk()}")
mhs1.__ipk = -20
print(mhs1.__ipk)
print(mhs1.__dict__)
print(mhs1._Mahasiswa__ipk)
"""_summary_
Encapsulation bukan cuma soal menyembunyikan data.
Tapi soal:
Mengontrol bagaimana data boleh diakses dan diubah.

    """
print()


#latihan
class Siswa:
    def __init__(self, nama, asal_sekolah):
        self.nama = nama
        self.asal_sekolah = asal_sekolah
        self.__rata2_nilai_raport = 0.0
        
    def input_nilai(self, nilai):
        if nilai < 0 or nilai > 100:
            print("Nilai harus antara 0 - 100")
        else:
            self.__rata2_nilai_raport = nilai
            print("Nilai Berhasil Ditambahkan")
        
    def lihat_nilai(self):
        return self.__rata2_nilai_raport
        
    def status_kelulusan(self, min_nilai=75):
        if self.__rata2_nilai_raport < min_nilai:
            print(f"{self.nama} WAJIB melakukan remedial")
        else:
            print(f"Selamat kepada {self.nama}, Anda dinyatakan LULUS")
            
siswa1 = Siswa("Bimo", "SMA 1 Kendal")

siswa1.input_nilai(90)
print(f"Rata-rata Nilai Raport: {siswa1.lihat_nilai()}")
siswa1.status_kelulusan()






