AantalPersonen = int(input("Met hoeveel aantal personen komt u? : "))
Toegangsticket = float(input("Weet u hoeveel een toegangsticket kost? : ")) * 100

VRtijd = int(input("Voor hoeveel minuten heeft u de VRbril gehuurd? : "))
Kostenper5minuten = float(input("Weet u ook hoeveel het kost om de VR voor 5 minuten te huren? : ")) * 100

print(f'‘Dit geweldige dagje-uit met {AantalPersonen} mensen in de Speelhal met {VRtijd} minuten VR kost je maar {round(Toegangsticket + VRtijd*int(Kostenper5minuten*AantalPersonen), 2)} euro’')