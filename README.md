# ♟️ Chess Game by Nico

Un jeu d'échecs à deux joueurs en local, développé en **Python** avec **Pygame**, avec pendule intégrée.

![Visuel du jeu](<visuel du jeu.png>)

---

## 📅 Informations

- **Développement :** mars – avril 2020
- **Publication sur GitHub :** 7 octobre 2026
- **Auteur :** Nicolas Brault ([@Cialson](https://github.com/Cialson))

> ⚠️ **Aucune IA générative n'a été utilisée** pour écrire le code de ce jeu ni pour créer ses visuels. L'ensemble du projet a été réalisé à la main en 2020.

---

## ✨ Fonctionnalités

- **Partie à deux joueurs** sur le même ordinateur (Blancs contre Noirs), les tours alternent automatiquement.
- **Choix de la cadence** avant la partie : **30 min**, **10 min** ou **5 min** par joueur.
- **Pendule** pour chaque camp, avec affichage des dixièmes de seconde en rouge quand le temps devient critique.
- **Affichage des coups possibles** quand on clique sur une pièce :
  - 🟢 cercle vert : case libre où la pièce peut aller ;
  - 🔴 cercle rouge : pièce adverse qui peut être prise.
- **Déplacements de toutes les pièces** : pion (avec double pas au premier coup et prise en diagonale), tour, cavalier, fou, dame et roi.
- **Roque** (petit et grand) tant que le roi et la tour concernée n'ont pas bougé.
- **Promotion** : un pion qui atteint la dernière rangée devient automatiquement une dame.
- **Compteur de pièces prises** affiché sur le côté de chaque joueur.
- **Fin de partie** :
  - par **prise du roi** adverse ;
  - au **temps**, quand la pendule d'un joueur tombe à zéro.
- Bouton **« Rejouer »** pour relancer une partie.

---

## 🎮 Comment jouer

1. Lancez le jeu.
2. Choisissez une cadence (**30 MIN**, **10 MIN** ou **5 MIN**).
3. Cliquez sur **« Jouer »**.
4. Le joueur dont c'est le tour voit le message **« À votre tour »** de son côté.
5. Cliquez sur une de vos pièces pour afficher ses déplacements possibles, puis cliquez sur la case de destination.
6. La partie se termine quand un roi est pris ou quand une pendule arrive à zéro.

Le plateau est affiché à l'horizontale : les **Blancs** jouent depuis la **gauche** de l'écran, les **Noirs** depuis la **droite**.

---

## 🚀 Installation et lancement

### Option 1 : exécutable Windows

Double-cliquez sur `Chess_Game_by_Nico.exe`.

> Les images (`Chess pieces *.png`, `Chess_Icon.png`) doivent se trouver **dans le même dossier** que l'exécutable.

### Option 2 : depuis le code source

**Prérequis :**
- Python 3
- [Pygame](https://www.pygame.org/)

```bash
pip install pygame
python Chess_Game_by_Nico.py
```

> Lancez le script **depuis le dossier du projet**, car les images sont chargées par chemin relatif.

---

## 📁 Structure du projet

| Fichier | Rôle |
|---|---|
| `Chess_Game_by_Nico.py` | Code source complet du jeu |
| `Chess_Game_by_Nico.exe` | Version exécutable pour Windows |
| `Chess pieces <Pièce> B.png` / `N.png` | Images des pièces blanches / noires sur le plateau |
| `Chess pieces <Pièce> BP.png` / `NP.png` | Petites images utilisées pour le compteur de pièces prises |
| `Chess pieces.png` | Planche d'origine des pièces |
| `Chess_Icon.png` / `Chess_Icon.ico` / `Chess ico.png` | Icônes de la fenêtre et de l'exécutable |
| `visuel du jeu.png` | Capture d'écran du jeu |

---

## 🛠️ Technologies

- **Python 3**
- **Pygame** : affichage, gestion de la souris et des événements
- **time** (bibliothèque standard) : gestion des pendules
