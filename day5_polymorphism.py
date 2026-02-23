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


# hewan_list = [Kucing(), Anjing()]

# for h in hewan_list:
#     h.suara()