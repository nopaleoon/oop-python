class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def perkenalan(self):
        print(f"Halo, nama saya {self.nama}, umur {self.umur} tahun.")


class Mahasiswa(Manusia):  # <- mewarisi Manusia
    def __init__(self, nama, umur, nim):
        super().__init__(nama, umur)  # ambil dari parent
        self.nim = nim

    def perkenalan(self):
        super().perkenalan() # memanggil method perkenalan dari parent, lalu print saya mahasiswa
        print("Saya adalah mahasiswa.")

    def info_mahasiswa(self): #overide
        print(f"NIM saya adalah {self.nim}")


# Membuat object
mhs1 = Mahasiswa("Naufal", 19, "L200250046")

mhs1.perkenalan()     # method dari parent , tampil saya mahasiswa
mhs1.info_mahasiswa() # method dari child