class BankHashiv:
    def __init__(self,mnacord):
        if mnacord<0:
            raise ValueError("bacasakan mnacord")
        self.mnacord=mnacord

    def gumar_avelacnel(self,gumar):
        if gumar<0:
            raise ValueError("gumar@ bacasakan e")
        self.mnacord+=gumar
    def gumar_hanel(self,gumar):
        if not 0<gumar<=self.mnacord:
            raise ValueError("cheq karox hanel")
        self.mnacord-=gumar


A1=BankHashiv(100)
A1.gumar_avelacnel(200)
A1.gumar_hanel(50)

print(A1.mnacord)
