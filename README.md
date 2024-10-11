# Tic-Tac-Toe

Ce projet est une implémentation du célèbre jeu Tic-Tac-Toe (morpion) avec une IA qui utilise l'algorithme Minimax pour déterminer les coups optimaux. Le joueur humain affronte l'ordinateur, qui joue toujours de manière parfaite grâce à cet algorithme.

## Table des matières

- [Introduction](#introduction)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Fonctionnalités](#fonctionnalités)
- [Exemple](#exemple)
- [Structure du Projet](#structure-du-projet)
- [Contributeurs](#contributeurs)

## Introduction

Ce projet permet aux utilisateurs de jouer au jeu Tic-Tac-Toe contre une IA qui utilise l'algorithme Minimax pour ne jamais perdre. Le jeu est exécuté dans le terminal et propose une interface simple pour jouer contre l'ordinateur. L'IA analyse tous les coups possibles et choisit toujours le meilleur pour garantir qu'elle ne peut pas être battue.

## Prérequis

Python 3.7 ou version ultérieure
Modules Python : Aucun

## Installation

1. Clonez le dépôt Git :

```bash
git clone git@github.com:florian-labadie/Tic-Tac-Toe.git
```

2. Accédez au répertoire du projet :

``` bash
cd Tic-Tac-Toe
```

## Utilisation

### Lancer le jeu

Pour démarrer le jeu, exécutez la commande suivante dans le terminal :

``` bash
./tic-tac-toe
```

Cela lancera le script Bash qui appelle le programme Python. Le jeu commencera directement dans le terminal.

### Règles du Jeu

1- Le jeu affiche une grille 3x3.
2- Le joueur humain choisit où placer son symbole (X) en entrant d'abord la ligne puis la colonne correspondant à la case voulu.
3- L'IA jouera ensuite son coup optimal (O).
4- Le jeu continue jusqu'à ce que l'un des joueurs gagne ou que la grille soit pleine.

### Options

Actuellement, le jeu ne propose pas de niveaux de difficulté ni d'autres modes. L'IA joue toujours de manière optimale.

## Fonctionnalités

Algorithme Minimax : IA imbattable qui utilise Minimax pour jouer de manière parfaite.
Interface en Ligne de Commande : Simple et efficace pour jouer directement depuis le terminal.
Tours Joueur/IA : Tour par tour entre le joueur humain et l'ordinateur.

## Exemple

``` bash
Bienvenue dans le jeu de Tic-Tac-Toe !
  |   |  
---------
  |   |  
---------
  |   |  
C'est le tour du joueur X.
Entrez la ligne (0, 1, 2) : 0
Entrez la colonne (0, 1, 2) : 1
  | X |  
---------
  |   |  
---------
  |   |  
C'est le tour de l'IA (O).
O | X |  
---------
  |   |  
---------
  |   |  
```

## Structure du Projet

Le projet est organisé comme suit :

``` bash
Tic-Tac-Toe/
├── src/                # Code source principal
│   ├── ai.py                   # Algorythme de jeu le l'IA
│   ├── board.py                # Affichage du board et création
│   ├── get_free_position.py    # Vérification de si la case jouer et vide ou déjà remplie
│   ├── player.py               # Gestion du tour du player
│   └── tic_tac_toe.py          # Script principal
├── .gitignore  
├── tic-tac-toe         # Executable
├── main.py             # Point d'entrée du script principal
└── README.md           # Documentation du projet
```

## Contributeurs

- Labadie Florian ([GitHub](https://github.com/florian-labadie))
