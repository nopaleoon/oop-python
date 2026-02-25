
class Laptop:
    ram = 8
    def __init__(self, merk, ram, storage):
        self.merk = merk
        self.ram = ram
        self.storage = storage
        
    def info(self):
        print(f"Merk : {self.merk}")
        print(f"Ram : {self.ram} Gb")
        print(f"Storage : {self.storage} Gb")
        
    def upgrade_ram(self, new_ram):
        self.ram = new_ram
        print("ram berhasil diupgrade")
        
laptop_1 = Laptop("Lenovo", 20, 512)
laptop_1.info()
laptop_1.upgrade_ram(32)
laptop_1.info() 

class Laptop2:
    ram = 8 # attribute milik class, bukan milik object

laptop_2 = Laptop2()
print(laptop_2.ram)

class Laptop3:
    def __init__(self, ram):
        self.ram = ram #instance attribute
        
l3 = Laptop3(8)
l4 = Laptop3(16)
#Setiap object punya nilai masing2

print(l3.ram)
print(l4.ram)


class Laptopp:
    ram = 8

    def __init__(self, merk):
        self.merk = merk


l1 = Laptopp("Asus")
l2 = Laptopp("Lenovo")

l2.ram = 16

print(l1.ram)
print(l2.ram)

#note
#urutan pencarian attribute di python
"""Instance → Class → Parent class"""