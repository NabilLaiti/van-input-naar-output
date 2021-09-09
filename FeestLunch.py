Aantalcroissantjes = int(input("Hoeveel croissantjes wilt u kopen? : "))
CroissantjesPrijs = float(input("Weet u hoeveel een croisant kost? : ")) * 100
print(' ----------------------------------------------------')
Aantalstokbroden = int(input("Hoeveel stokbroden wilt u kopen? : "))
StokbrodenPrijs = float(input("Weet u hoeveel een stokbrood kost? : ")) * 100
print(' ----------------------------------------------------')
Aantalkortingsbonnen = int(input("Hoeveel kortingsbonnen heeft u? : "))
Kortingsbonnen = float(input("Weet u hoeveel korting u krijg met al u bonnen? : ")) * 100
print(' ----------------------------------------------------')
print(f'‘De feestlunch kost je bij de bakker {round(Aantalcroissantjes*int(CroissantjesPrijs) + Aantalstokbroden*int(StokbrodenPrijs) - Aantalkortingsbonnen*int(Kortingsbonnen), 2)} euro voor de {Aantalcroissantjes} croissantjes en de {Aantalstokbroden} stokbroden als de {Aantalkortingsbonnen} kortingsbonnen nog geldig zijn!’')
