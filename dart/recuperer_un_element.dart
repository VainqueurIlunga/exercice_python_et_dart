
//L'objectif de l'exercice est de récupérer un élément sur deux dans la liste.

//Votre script doit donc récupérer dans la variable resultat la liste suivante :

//[1, 3, 5, 7, 9]


void main(){
  List<int> ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  List <int> resultat= [];
  int pas = 2;
  for(int i = 0; i < ma_liste.length; i+=pas){
    resultat.add(ma_liste[i]);
  }
  print(resultat);
}