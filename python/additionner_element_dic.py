"""Dans cet exercice, vous devez additionner 
toutes les valeurs 
du dictionnaire ensemble.

Votre script doit donc retourner le nombre entier 
8700 dans la variable resultat."""

employes = {"Pierre": 2500, "Marie": 5000, "Julien": 1200}
result= 0
for i in employes.values():
    result += i
print(result)


# ou encore 
result = sum(employes.values())
print(result)