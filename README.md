# Etude comparative du temps d'exécution d'un algorithme de Page Ranking 

L'étude compare le temps d'exécution d'un algorithme de page ranking en fonction :
* Du nombre de machine dans le cluster
* Du langage utilisé (Pig/Spark)

---
## Page ranking à l'aide de *PIG*


---

---
## Génération et ajout d'un fichier de crawling

Pour commencer le calcul du PageRank nous avons besoin d'un fichier de crawling celui-ci va regrouper tous les url contenu dans une page web et parcourir ces urls et jusqu'où nous permettent d'aller ces liens.
Cela nous permettra ensuite de calculer grâce au PageRank la probabilité qu'on arrive sur notre page de départ.

Pour récupérer un fichier de crawling plusieurs solutions sont disponibles :
- Via des ressources en lignes comme "Common crawl".

- Via des logiciel dit des crawlers qui vont générer le fichier en partant d'une url donnée en entrée.

- Via des algorithmes que l'on implémente nous-mêmes qui vont généré des url fictifs avec des liens entre les urls. cette solution à l'avantage que l'on peut facilement gérer la taille du fichier de sortie que l'on veut obtenir.

Nous avons décidé d'utiliser la troisième solution.

Pour faire cela nous avons utilser le main.py de ce repository dans le dossier /python-project/src puis pour choisir le nombre d'url parcourus, à la fin du fichier lors de l'appel à la fonction goodgencrawl on modifie la valeur du paramètre, 100 si on veut parcourir 100 urls par exemple.

Après avoir donnée la valeur que l'on veut au paramètre de la fonction goodGenCrawl (15 000 pour un fichier de 1Go), on lance le fichier main.py. Pour se faire, via un terminal on se rend dans le dossier où le fichier est stocké et on l'exécute avec la commande "python main.py" ou "python3 main.py" (le compilateur python doit être installé). Suite à cela un fichier crawl.csv a été crée dans le dossier.

Pour ajouter et exploiter le fichier que l'on a généré, sur google cloud platform on crée un nouveau projet puis l'on se rend dans "cloud storage" ensuite on crée un bucket et l'on importe le fichier généré dans le bucket créé.

---


On doit voir:

- plus de noeuds dans le cluster -> plus rapide mais de combien ??

- Spark plus rapide que PIG

- Exec automatique  : Bash/Python/SnakeMake (comme vous voulez...)

- rendu sous forme d'un repo github (ou assimilé)  + Readme (par example : https://github.com/sage-org/sage-property-paths-experiments)


- VOTRE EXP doit ETRE REPETABLE !!
