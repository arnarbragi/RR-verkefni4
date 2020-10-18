from math import *

class Vigur:

    # Smiður frumstillir x og y hnit vigurs eftir parametrum
    def __init__(self,x,y): 
        self.x = x
        self.y = y

    # Fall sem skrifar hnit vigurs Ã¡ skjÃ¡
    def prenta(self):       
        print("[", self.x ," ", self.y ,"]", sep="")
    
    # Fall sem skilar lengd
    def lengd(self):        
        return round((sqrt(self.x**2 + self.y**2)),2)
    
    # Fall sem skilar hallatÃ¶lu
    def halli(self):        
        return round(self.y/self.x,2)
    
    # Fall sem skilar Ã¾vervigri
    def þvervigur(self):     
        return Vigur(-self.y,self.x)
    
    # Fall sem skilar stefnuhorni
    def stefnuhorn(self):   
        if self.y < 0:
            return -round(degrees(acos((self.x/self.lengd()))),1)
        else:
            return round(degrees(acos((self.x/self.lengd()))),1)
    
    # Fall sem tekur vigur sem parameter og skilar horni milli vigra
    def horn(self,v):       
        innf = self.x * v.x + self.y * v.y
        return round(degrees(acos((innf/(self.lengd()*v.lengd())))),1)
    
    # Fall sem tekur vigur sem parameter og skilar summu vigri
    def summa(self,v):
        return Vigur(self.x + v.x, self.y + v.y)

# Keyrsluforrit
v1 = Vigur(1,3)
v1.prenta()
print("Lengd: ", v1.lengd())
print("Halli: ", v1.halli())
vþ = v1.þvervigur()
print("þvervigur: " , end=" ")
vþ.prenta()
print("Stefnuhorn: ", v1.stefnuhorn())    
v2 = Vigur(-3,1)
print("Horn milli vigra: " , v2.horn(v1))
v3 = v1.summa(v2)
print("Summa: " , end=" ")
v3.prenta()
