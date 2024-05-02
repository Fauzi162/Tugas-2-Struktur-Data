class Peta:
    def __init__(self):
        self.daftarKota = {}
    
    def tambahKota(self, kota):
        if kota not in self.daftarKota:
            self.daftarKota[kota] = {}
    
    def printKota(self):
        for kota in self.daftarKota:
            print(f"{kota} -- {self.daftarKota[kota]}")
    
    def tambahJarak(self, kota1, kota2, jarak):
        if kota1 and kota2 in self.daftarKota:
            self.daftarKota[kota1][kota2] = jarak
            self.daftarKota[kota2][kota1] = jarak
    
    def hapusKota(self, kotaDihapus):
        if kotaDihapus in self.daftarKota:
            for kota in self.daftarKota:
                if kotaDihapus in self.daftarKota[kota]:
                    del self.daftarKota[kota][kotaDihapus]
            del self.daftarKota[kotaDihapus]
    
    def hapusJarak(self, kota1, kota2):
    if kota1 and kota2 in self.daftarKota:
            del self.daftarKota[kota1][kota2]
            del self.daftarKota[kota2][kota1]

petaJepang = Peta()
petaJepang.tambahKota("Mori")
petaJepang.tambahKota("Iwata")
petaJepang.tambahKota("Fukuroi")
petaJepang.tambahKota("Kakegawa")
petaJepang.tambahKota("Kikugawa")
petaJepang.tambahKota("Shimada")
petaJepang.tambahKota("Fujieda")
petaJepang.tambahKota("Yaizu")
petaJepang.tambahKota("Yoshida")
petaJepang.tambahKota("Makinohara")
petaJepang.tambahKota("Omaezaki")

petaJepang.tambahJarak("Mori", "Iwata", 19)
petaJepang.tambahJarak("Mori", "Fukuroi", 12)
petaJepang.tambahJarak("Mori", "Kakegawa", 14)
petaJepang.tambahJarak("Mori", "Kikugawa", 23)
petaJepang.tambahJarak("Mori", "Shimada", 30)
petaJepang.tambahJarak("Mori", "Fujieda", 40)
petaJepang.tambahJarak("Iwata", "Fukuroi", 9)
petaJepang.tambahJarak("Iwata", "Omaezaki", 30)
petaJepang.tambahJarak("Fukuroi", "Kakegawa", 8)
petaJepang.tambahJarak("Fukuroi", "Omaezaki", 27)
petaJepang.tambahJarak("Kakegawa", "Kikugawa", 10)
petaJepang.tambahJarak("Kakegawa", "Omaezaki", 23)
petaJepang.tambahJarak("Kikugawa", "Shimada", 19)
petaJepang.tambahJarak("Kikugawa", "Makinohara",15)
petaJepang.tambahJarak("Kikugawa", "Yoshida", 21)
petaJepang.tambahJarak("Kikugawa", "Omaezaki", 17)
petaJepang.tambahJarak("Shimada", "Fujieda", 9)
petaJepang.tambahJarak("Shimada", "Yoshida", 11)
petaJepang.tambahJarak("Fujieda", "Yoshida", 13)
petaJepang.tambahJarak("Yaizu", "Fujieda", 7)
petaJepang.tambahJarak("Yaizu", "Yoshida", 15)
petaJepang.tambahJarak("Yoshida", "Makinohara", 5)
petaJepang.tambahJarak("Makinohara", "Omaezaki", 17)
petaJepang.tambahJarak("Shimada", "Omaezaki",16)
petaJepang.tambahJarak("Kikugawa", "Shimada", 19)
petaJepang.tambahJarak("Makinohara", "Shimada", 17)

petaJepang.hapusKota("Mori")
petaJepang.hapusJarak("Fujieda", "Yoshida")

petaJepang.printKota()


































      
