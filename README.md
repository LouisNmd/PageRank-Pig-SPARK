# Etude comparative du temps d'exécution d'un algorithme de Page Ranking 

L'étude compare le temps d'exécution d'un algorithme de page ranking en fonction :
* Du nombre de machine dans le cluster
* Du langage utilisé (Pig/Spark)

---
## Page ranking à l'aide de *PIG*


---

---
## Génération d'un fichier de crawling

Pour commencer le calcul du PageRank nous avons besoin d'un fichier de crawling celui-ci va regrouper tous les url contenu dans une page web et parcourir ces urls et jusqu'où nous permettent d'aller ces liens.
Cela nous permettra ensuite de calculer grâce au PageRank la probabilité qu'on arrive sur notre page de départ.

Pour récupérer un fichier de crawling plusieurs solutions sont disponibles :
- Via des ressources en lignes comme "Common crawl".

- Via des logiciel dit des crawlers qui vont générer le fichier en partant d'une url donnée en entrée.

- Via des algorithmes que l'on implémente nous-mêmes qui vont généré des url fictifs avec des liens entre les urls. cette solution à l'avantage que l'on peut facilement gérer la taille du fichier de sortie que l'on veut obtenir.

Nous avons décidé d'utiliser la troisième solution.

---

On doit voir:

- plus de noeuds dans le cluster -> plus rapide mais de combien ??

- Spark plus rapide que PIG

- Exec automatique  : Bash/Python/SnakeMake (comme vous voulez...)

- rendu sous forme d'un repo github (ou assimilé)  + Readme (par example : https://github.com/sage-org/sage-property-paths-experiments)


- VOTRE EXP doit ETRE REPETABLE !!
