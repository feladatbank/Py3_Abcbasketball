'''
hazai	idegen	hazai_pont	idegen_pont	helysz�n	id�pont
7up Joventut	Adecco Estudiantes	81	73	Palacio Mun. De Deportes De Badalona	2005-04-03
'''

class Project():
    def __init__(self, sor):
        hazai, idegen, hazai_pont, idegen_pont, helyszin, idopont = sor.strip().split(";")
        self.hazai = hazai
        self.idegen = idegen
        self.hazai_pont = hazai_pont
        self.idegen_pont = idegen_pont
        self.helyszin = helyszin
        self.idopont = idopont
        
with open("eredmenyek.txt", "r", encoding="latin2") as f:
    cim_sor = f.readline()
    lista = [Project(sor) for sor in f]


#3
madridh = [sor for sor in lista if sor.hazai == "Real Madrid"]
madridi = [sor for sor in lista if sor.idegen == "Real Madrid"]
print(f"3. Feladat: Real Madrid: Hazai: {len(madridh)}, Idegen: {len(madridi)}")        

#4

dontettlen = [sor for sor in lista if sor.hazai_pont == sor.idegen_pont]
ha_nem_dontettlen = [sor for sor in lista if sor.hazai_pont != sor.idegen_pont]
if len(dontettlen) != 0:
    print("4. Feladat: Volt döntettlen? Igen")
else:
    print("4. Feladat: Volt döntettlen? Nem")
    
#5
barca = [sor.hazai for sor in lista if "Barcelona" in sor.hazai][0]

print(f"5. Feladat: barcelonai csapat neve: {barca}")
