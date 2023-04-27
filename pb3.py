def citeste_fisier(nume_fisier):
    with open(nume_fisier, 'r') as f:
        continut = f.read().lower()
        # transformam continutul in lowercase pentru a compara cuvintele indiferent de capitalizare
        cuvinte = set(continut.split())
        # folosim set pentru a elimina cuvintele duplicate
        return cuvinte

# Citim continutul celor doua fisiere
fisier1 = citeste_fisier('fisier1.txt')
fisier2 = citeste_fisier('fisier2.txt')

# Afișăm lista cu toate cuvintele unice conținute în ambele fișiere
toate_cuvintele = fisier1.union(fisier2)
print("Toate cuvintele unice din ambele fisiere:", toate_cuvintele)

# Afișăm lista de cuvinte care apar în ambele fișiere
cuvinte_comune = fisier1.intersection(fisier2)
print("Cuvintele comune din cele doua fisiere:", cuvinte_comune)

# Afișăm lista de cuvinte care apar în primul fișier, dar nu în al doilea
cuvinte_fisier1 = fisier1.difference(fisier2)
print("Cuvintele din fisierul 1, dar nu si in fisierul 2:", cuvinte_fisier1)

# Afișăm lista de cuvinte care apar în al doilea fișier, dar nu în primul
cuvinte_fisier2 = fisier2.difference(fisier1)
print("Cuvintele din fisierul 2, dar nu si in fisierul 1:", cuvinte_fisier2)

# Afișăm lista de cuvinte care apar fie în primul sau în al doilea fișier, dar nu în ambele
cuvinte_diferite = fisier1.symmetric_difference(fisier2)
print("Cuvintele diferite din cele doua fisiere:", cuvinte_diferite)
