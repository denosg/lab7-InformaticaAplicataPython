raze_medii = {'Io': 1821.6, 'Europa': 1560.8,
              'Ganymede': 2634.1, 'Callisto': 2410.3}

gravitati_suprafata = {'Io': 1.796, 'Europa': 1.314,
                       'Ganymede': 1.428, 'Callisto': 1.235}

perioade_orbitale = {'Io': 1.769, 'Europa': 3.551,
                     'Ganymede': 7.154, 'Callisto': 16.689}

satelit = input(
    "Introduceti numele unui satelit al lui Jupiter (Io, Europa, Ganymede sau Callisto): ")

if satelit in raze_medii:
    print("Raza medie a lui", satelit, "este", raze_medii[satelit], "km")
    print("Gravitatea de suprafata a lui", satelit,
          "este", gravitati_suprafata[satelit], "m/s^2")
    print("Perioada orbitala a lui", satelit,
          "este", perioade_orbitale[satelit], "zile")
else:
    print("Numele introdus nu este valid.")
