# Générateur d'exercices de calculs en LaTeX

Ce programme Python permet de générer des fichiers d'exercices de calculs adaptés au niveau primaire. Les exercices sont exportés sous forme de fichiers LaTeX, puis compilés avec PDFLaTeX pour obtenir un document PDF prêt à être imprimé.

Les documents générés sont basés sur un exercice qui a été donné à mon enfant par son institutrice: un ensemble de 40 calculs à résoudre en 3 minutes avec au final une notation par couleurs de ceinture de judo.

Néanmoins, certaines fiches générées ne sont que des tests et ne sont pas forcement destinées à un enfant.

Aussi le programme en lui-même reste simple avec beaucoup de redondances, je ne vois pas d'intérêt à améliorer le programme au delà.

## Exercices générés

Le programme produit un livret PDF composé de 100 pages d'exercices de 40 calculs (pour la plupart). Les pages sont au format A5 (la moitié d'une page A4). Il est préférable d'imprimer le livret à 2 page par feuilles. Chaque livret coûte un peu plus de 300 ko.

Les calculs proposés sont générés avec des nombres aléatoires. Aussi, un mécanisme permet de limiter les redondances dans une même fiche de calculs.

### Les types d'exercices:

#### calculs classiques
$5 + 2 = \ldots$

#### calculs opérande manquante
$5+\ldots=7$

#### calculs posés
```  10
+  5
-----
  ...
```

### La liste des exercices produits:

- **Exo 01:**  $[1, 10] + [1, 3] = \ldots$
- **Exo 02:**  $[1,10]+[1,5]= \ldots$ 
- **Exo 03:**  $[1,10] + [1,10] = \ldots$
- **Exo 04:** $[1,10]+[1,10]+[1,10] = \ldots$
- **Exo 05:**
  - $[1,10]+[1,10]=\ldots$
  - $10-[1,10] = \ldots$
- **Exo 06:** $[1,30] + [1,10] = \ldots$
- **Exo 07:** $[1,100] + [1,10] = \ldots$
- **Exo 08:** $[1,100] + [1,20] = \ldots$
- **Exo 09:** $[1,100] + [1,20]=\ldots$
- **Exo 10:** $[1,10]-[1,10]=\ldots$
- **Exo 11:** $[1,19] - [1,10]=\ldots$
- **Exo 12:** $[1,100] - [1,10]=\ldots$
- **Exo 13:** $[1,100]-[1,20]=\ldots$
- **Exo 14:** $[1,100]-[1,100]=\ldots$
- **Exo 15:**
  - $[1,20] - [1;10]= \dots$
  - $[1;10] + [1;10]=\ldots$
- **Exo 16:**
  - $[1,100]-[1,10]=\ldots$
  - $[1,100]+[1,10]=\ldots$
- **Exo 17:** *calcul posés* $[1,100] + [1,100]=\ldots$
- **Exo 18:** *calcul posés* $[1,100] - [1,100]=\ldots$
- **Exo 19:** 
  - $2 \times [1,10]=\ldots$
  - $2 \times \ldots = \{ 2 \times [0;10]\}$
- **Exo 20:** 
  - $3 \times [1,10]=\ldots$
  - $3 \times \ldots = \{ 3 \times [0;10]\}$
- **Exo 21:** 
  - $[2,3] \times [1,10]=\ldots$
  - $[2,3] \times \ldots = \{ [2,3] \times [0;10]\}$
- **Exo 22:**
  - $4 \times [1,10]=\ldots$
  - $4 \times \ldots = \{ 4 \times [0;10]\}$
- **Exo 23:** 
  - $[2,4] \times [1,10]=\ldots$
  - $[2,4] \times \ldots = \{ [2,3] \times [0;10]\}$
- **Exo 24:**
  - $5 \times [1,10]=\ldots$
  - $5 \times \ldots = \{ 5 \times [0;10]\}$
- **Exo 25:**
  - $[2,5] \times [1,10]=\ldots$
  - $[2,5] \times \ldots = \{ [2,5] \times [0;10]\}$
- **Exo 26:**
  - $[2 ~ ou ~ 5] \times [1,10]=\ldots$
  - $[2 ~ ou ~ 5] \times \ldots = \{ [2 ~ ou ~ 5] \times [0;10]\}$

# Licence

 Le programme est proposé avec la licence GNU GPL v2
