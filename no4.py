class Buah:
    def _init_(self, nama, warna, vitamin, rasa):
        self.nama = nama
        self.warna = warna
        self.vitamin = vitamin
        self.rasa = rasa

    def setNama(self, nama):
        self.nama = nama

    def setWarna(self, warna):
        self.warna = warna

    def setVitamin(self, vitamin):
        self.vitamin = vitamin

    def setRasa(self, rasa):
        self.rasa = rasa

    def information(self):
        return f"Nama: {self.nama}, Warna: {self.warna}, Vitamin: {self.vitamin}, Rasa: {self.rasa}"

class Mangga(Buah):
    def _init_(self, nama, warna, vitamin, rasa, varietas):
        super()._init_(nama, warna, vitamin, rasa)
        self.varietas = varietas

    def setVarietas(self, varietas):
        self.varietas = varietas

    def getVarietas(self):
        return self.varietas

    def information(self):
        info = super().information()
        return f"{info}, Varietas: {self.varietas}"

