# Etude comparative du temps d'exécution d'un algorithme de Page Ranking 

Travail réalisé par NORMAND Louis, COLIN Thibault, TENAUD Raphaël

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
        <td>14m 08s</td>
        <td>+64.3%</td>
    </tr>
</table>

Nous n'avons pas la possibilité de tester avec un plus grand nombre de noeuds à cause du quota de CPU allouable par compte : nous sommes limité à 26 CPU, soit 5 noeuds + 1 noeud maître de 4 processeurs chacun (24 CPU au total).  
Il est cependant possible de demander une augmentation du quota de CPU ou diminuer le nombre de processeur par noeud (et ainsi donc augmenter la taille du cluster). 

---
## Mise en place de l'expérience

#### Prérequis

- un fichier de crawling (peut-être généré grâce à la commande ```sh generateCrawl.sh <nombre d'url>``` ou récupéré sur Internet)
- le gcloud SDK sur la machine locale
- python3 sur la machine locale (si on souhaite générer un crawl)
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

Exécuter le script *pig.sh* présent à la racine de projet :
```
sh pig.sh <cluster_name> 
```
**Attention**: Il faut changer le nom du bucket cloud storage dans le fichier dans le fichier: ```pythonProject/src/PageRankPig.py```  
En effet,  ```gcloud submit pig job``` ne permet pas d'ajouter des arguments à notre fichier python.

Le résultat est présent sous la forme du fichier **pagerank-final/pagerank-final_part-r-00000**, stocké dans le bucket **<bucket_name>** passé en paramètre.  
Ce fichier sans extension est ouvrable à l'aide des principaux* éditeurs de texte.  
*\*Le bloc-note de Windows ne permet pas de lire ce fichier : il est nécéssaire de passer par un logiciel tiers ou de changer l'extension à la main*

3 - Exécuter l'algorithme de page ranking sous Spark

Exécuter le script *spark.sh* présent à la racine de projet :
```
sh spark.sh <cluster_name> <bucket_name>
```
Le résultat est présent sous la forme du fichier **result.csv**, stocké dans le bucket **<bucket_name>** passé en paramètre.

4 - Modifier le nombre de noeuds dans le cluster

Se rendre dans l'outil **Dataproc** > **Cluster** > ***Mon_cluster*** > **Configuration** > **Modifier**  
Faire varier le nombre de noeuds en modifiant le champs **Noeuds de calcul**

5 - Le code

Le code de génération de crawl génére des url sous forme "x[0-9]\*", le nombre d'url nécessaire en paramètre pour atteindre 1 Go est environ 15000.
Cette génération donne une probabilité de lien vers les premières URLs de 70%, cette probabilité baisse linéairement jusqu'à 0 pour les dernières URLs.  
La génération est sous forme: ```x0 x1``` par ligne.

Le code du pig a été trouvé sur [internet](https://github.com/julienledem/Pig-scripting-examples/tree/master/Page%20Rank) et remanié car il prend des instances sous forme:   
```xO 1 {(x1), (x2), (x3)....}``` par ligne.

Le code du spark a été trouvé aussi sur [internet](https://github.com/apache/spark/blob/master/examples/src/main/python/pagerank.py).

Ces deux algorithmes sont modifiés pour être utilisé avec le Dataproc Google.

