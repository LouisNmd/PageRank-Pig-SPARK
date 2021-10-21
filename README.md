# Etude comparative du temps d'exécution d'un algorithme de Page Ranking 

L'étude compare le temps d'exécution d'un algorithme de page ranking en fonction :
* Du nombre de machine dans le cluster
* Du langage utilisé (Pig/Spark)

## Page ranking
![unknown](https://user-images.githubusercontent.com/56700560/138350960-7101a83c-8b5c-45b1-94ac-76b5c3c54815.png)

<table>
    <caption>Tableau comparatif du temps d'exécution de l'algorithme de page ranking</caption>
    <tr>
        <th scope="col">Nombre de noeuds</th>
        <th scope="col">Temps d'exécution pour Pig</th>
        <th scope="col">Temps d'exécution pour Spark</th>
        <th scope="col">Gain de vitesse d'une exécution sous Spark par rapport à Pig</th>
    </tr>
    <tr>
        <td>2</td>
        <td>44m 22s</td>
        <td>18m 41s</td>
        <td>+57.9%</td>
    </tr>
    <tr>
        <td>4</td>
        <td>40m 47s</td>
        <td>14m 28s</td>
        <td>+64.6%</td>
    </tr>
    <tr>
        <td>5</td>
        <td>39m 37s</td>
        <td>+64.3</td>
    </tr>
</table>

Nous n'avons pas la possibilité de tester avec un plus grand nombre de noeuds à cause du quota de CPU allouable par compte : nous sommes limité à 26 CPU, soit 5 noeuds + 1 noeud maître de 4 processeurs chacun (24 CPU au total).  
Il est cependant possible de demander une augmentation du quota de CPU ou diminuer le nombre de processeur par noeud (et ainsi donc augmenter la taille du cluster). 

---
## Mise en place de l'expérience

#### Prérequis

- un fichier de crawling (peut-être généré grâce au script *.\pythonProject\src\main.py* ou récupéré sur Internet)
- le gcloud SDK sur la machine locale
- un environnement local sous Linux

1 - Mise en place de l'environnement d'exécution

Créer un nouveau projet gcp  
Se rendre dans l'outil **Dataproc** > **Cluster**   
Créer un cluster de 2 noeuds (à modifier plus tard pour varier les noeuds)  
Se rendre dans l'outil **Cloud Storage**  
Créer un nouveau bucket  

Déclarer votre nouveau projet comme celui utilisé :   
```
gcloud init
```

2 - Exécuter l'algorithme de page ranking sous Pig

2 - Exécuter l'algorithme de page ranking sous Spark
Exécuter le script *spark.sh* présent à la racine de projet :
```
spark.sh <cluster_name> <bucket_name>
```

---
