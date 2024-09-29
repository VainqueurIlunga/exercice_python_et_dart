"""Dans une entreprise, chaque mois, les salariés ont un salaire et une prime.
Le comptable cherche à faire des statistiques. Et comme il ne sait pas se
servir d'un ordinateur, comme d'habitude c'est sur vous que ça retombe !
On cherche donc à savoir quels sont les salariés :

qui ont au moins 3000 euros de salaire par mois.
qui ont eu au moins 250 euros de prime ce mois ci.
dont la prime fait au moins 6% du salaire.
Les données en entrée sont :

personnes : la liste des salariés.
salaires : la liste de salaires par mois (liste d'entiers).
primes : la liste des primes du mois (liste d'entiers).
Les 3 listes sont dans le même ordre, c'est-à-dire que le premier nom de la liste personnes à pour salaire le premier de salaires, et pour prime la première de primes, et ainsi de suite pour le deuxième, le troisième etc.

On veut en sortie 3 listes :

la liste des personnes dont le salaire est 3000 euros ou plus.
la liste des personnes dont la prime est de 250 euros ou plus.
la liste des personnes dont la prime fait au moins 6% du salaire.
Vous devez écrire une fonction statistiques_salaires qui prends dans l'ordre les paramètres personnes, salaires, primes et qui renvoie dans l'ordre les 3 listes de personnes.
"""

personnes = ["Stallman", "Torvalds", "Perlis", "Turing", "VomNeumann",
             "Iverson", "Boole", "Hamming", "Knuth", "Ritchie", "Thompson"]
salaires = [1500, 4700, 1500, 3800, 890, 4200, 480, 395, 1710, 1300, 3900]
primes = [190, 0, 117, 100, 500, 60, 0, 150, 0, 100, 180]

# Votre code ici 👇
def statistiques_salaires(personnes, salaires,primes):
    salaire_sup=[personnes[i] for i in range(len(salaires)) if salaires[i]>3000]
    prime=[personnes[i] for i in range(len(salaires)) if primes[i] >= 250]
    prime_6= [personnes[i] for i in range(len(salaires))if primes[i] >= salaires[i] * 0.06]
    
    return f"{salaire_sup} \n {prime} \n {prime_6}"

print(statistiques_salaires(personnes, salaires, primes))