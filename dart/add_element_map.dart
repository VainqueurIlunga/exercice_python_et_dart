//Dans cet exercice, 
//vous devez additionner toutes 
//les valeurs du dictionnaire ensemble.
//Votre script doit donc retourner 
//le nombre entier 8700 dans la variable resultat


void main (){
  Map<String, int> employes = {"Pierre": 2500, "Marie": 5000, "Julien": 1200};
  int result = 0;
  for(int i in employes.values){
    result += i;
  }
  print(result);
   // ou encore 
  int resultat = employes.values.reduce((Pierre, Marie) => Pierre +Marie);
  print(resultat);
}