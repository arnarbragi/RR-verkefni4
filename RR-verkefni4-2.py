import re

class Marglida:
    def __init__(self,fall):
        self.fall = fall

    def heilda(self, em):
        formerki = []
        
        for i in self.fall:
            if i == "+" or i == "-":
                formerki.append(i)
        lidir = re.split('[-+]',self.fall)
        if self.fall[0] == '-':
            lidir.remove('')
        else:
            formerki.insert(0,'+')
        
        summa = 0
        tel = 0
        for i in lidir:
            lidur = re.split('[x]',i)

            if len(lidur)==1:
                if formerki[tel]=='+':
                    summa += (int(lidur[0])*em)
                else:
                    summa -= (int(lidur[0])*em)
            elif lidur[0] == '' and lidur[1] == '':
                if formerki[tel] == '+':
                    summa += (em**2/2)
                else:
                    summa -= (em**2/2)
            elif lidur[0] == '' and lidur[1] != '':
                if formerki[tel] == '+':
                    summa += ((em**(int(lidur[1])+1))/(int(lidur[1])+1))
                else:
                    summa -= ((em**(int(lidur[1])+1))/(int(lidur[1])+1))
            elif lidur[0] != '' and lidur[1] == '':
                if formerki[tel] == '+':
                    summa += (int(lidur[0])*x**2/2)
                else:
                    summa -= (int(lidur[0])*x**2/2)
            else:
                if formerki[tel] == '+':
                    summa += (int(lidur[0])*x**(int(lidur[1])+1)/(int(lidur[1])+1))
                else:
                    summa -= (int(lidur[0])*x**(int(lidur[1])+1)/(int(lidur[1])+1))
            tel += 1
        return summa
    
    def flatarmal(self, em, nm):
        return self.heilda(em) - self.heilda(nm)


em = int(input("Sláðu inn efri mörk: "))
nm = int(input("Sláðu inn neðri mörk: "))

f0 = Marglida("-x2+2")
print(f0.flatarmal(em,nm))
