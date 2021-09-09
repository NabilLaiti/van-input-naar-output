# Nabil Laiti 99067444
# Pizza calculator

prijssmall = 5.25
prijsmedium = 7.76
prijslarge = 10.99

small = int(input(f"Hoeveel small pizza's wilt u? (€{prijssmall}) : "))
medium = int(input(f"Hoeveel medium pizza's wilt? (€{prijsmedium}) : ")) 
large = int(input(f"Hoeveel large pizza's wilt u? (€{prijslarge}) : "))

print(f' Je bestelling is in totaal €{round((prijssmall * small) + (prijsmedium * medium) + (prijslarge * large), 2)}, Kies u betaalmethode.') 
