personnes = ["Stallman", "Torvalds", "Perlis", "Turing", "VomNeumann",
             "Iverson", "Boole", "Hamming", "Knuth", "Ritchie", "Thompson"]
salaires = [1500, 4700, 1500, 3800, 890, 4200, 480, 395, 1710, 1300, 3900]
primes = [190, 0, 117, 100, 500, 60, 0, 150, 0, 100, 180]

def statistiques_salaires(personnes: list,
                          salaires: list,
                          primes: list) -> list:

    personnes_salaires_plus_de_3000 = []
    for index in range(len(personnes)):
        if salaires[index] >= 3000:
            personnes_salaires_plus_de_3000.append(personnes[index])

    personnes_prime_plus_de_250 = []
    for index in range(len(personnes)):
        if primes[index] >= 250:
            personnes_prime_plus_de_250.append(personnes[index])

    personnes_prime_6_pourcents = []
    for index in range(len(personnes)):
        if (primes[index] / salaires[index]) >= 6/100:
            personnes_prime_6_pourcents.append(personnes[index])

    return [personnes_salaires_plus_de_3000, personnes_prime_plus_de_250, personnes_prime_6_pourcents]


print(statistiques_salaires(personnes, salaires, primes))