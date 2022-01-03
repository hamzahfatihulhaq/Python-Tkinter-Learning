# harus ada inheritance(udah) sama enkapsulasi minimal2(sudah) sama polymorfis(sudah)
# class minimal ...
class bidang():#parrent class
    def __init__(self):
        self.sisi1 = 0
        self.sisi2 = 0
        self.sisi3 = 0 
    def luas(self):#overriding
        self._luas = 0
    def keliling(self):#overriding
        self._keliling = 0

class persegi(bidang):#child class1
    def __init__(self,sisi1,sisi2):
        super().__init__()#inheritance
        self.sisi1= sisi1
        self.sisi2= sisi2
    def luas(self):#overriding
        self._luas = self.sisi1 * self.sisi2#overloading
        return self._luas
    def keliling(self):#overriding
        self._keliling = 2*(self.sisi1+self.sisi2)#overloading
        return self._keliling

class segitiga(bidang):#child class2
    def __init__(self,alas,tinggi,miring):
        super().__init__()#inheritance
        self.sisi1 = alas
        self.sisi2 = tinggi
        self.sisi3 = miring
    def luas(self):#overriding
        self._luas = 0.5 * self.sisi1 * self.sisi2#overloading
        return self._luas
    def keliling(self):#overriding
        self._keliling = (self.sisi1+self.sisi2 + self.sisi3)#overloading
        return self._keliling
