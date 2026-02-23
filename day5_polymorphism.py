class Hewan:
    def suara(self):
        print("Hewan bersuara")

class Kucing(Hewan):
    def suara(self):
        super().suara() # memanggil method suara dari parent, lalu print suara kucing

class Anjing(Hewan):
    pass

kucing1 = Kucing()
kucing1.suara()

anjing1 = Anjing()
anjing1.suara()



hewan_list = [Kucing(), Anjing()]

for h in hewan_list:
    h.suara()
    
    
#Latihan 
# buat 3 class berbeda
# Mahasiswa, Dosen, Staff
# buat satu method yg sama tetapi isinya berbeda

class Mahasiswa:
    def kerja(self):
        print('Tugas Mahasiswa adalah belajar')
    
class Dosen:
    def kerja(self):
        print('Tugas Dosen adalah mengajar mata kuliah')
        
class Staff:
    def kerja(self):
        print('Tugas staff adalah mengelola admisnistrasi')
        
job = [Mahasiswa(), Dosen(), Staff()]
for j in job:
    j.kerja()