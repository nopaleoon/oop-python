
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














