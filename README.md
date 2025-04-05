# Square to Circle

**Square to Circle** est une application Python qui transforme les images carrées en images rondes. Le script applique un masque circulaire qui conserve uniquement le centre de l'image et rend transparent l’extérieur du cercle. Ce projet utilise la bibliothèque [Pillow](https://python-pillow.org/) pour le traitement d'images et [tkinter](https://docs.python.org/3/library/tkinter.html) pour la sélection des dossiers via une interface graphique.

---

## Fonctionnalités

- **Détection des images carrées :** Le programme parcourt un dossier source et ne traite que les images ayant des dimensions égales (largeur = hauteur).
- **Application d'un masque circulaire :** Un masque est appliqué pour conserver le contenu central en forme de cercle et rendre transparent le reste.
- **Gestion des formats d'image :**  
  - Conversion en mode `RGBA` pour la gestion de la transparence.
  - Sauvegarde automatique des images JPEG au format PNG pour éviter les erreurs liées à la transparence.
- **Interface simple pour le choix des dossiers :** Utilisation de boîtes de dialogue tkinter pour sélectionner le dossier source et le dossier de destination.

---

## Prérequis

- **Python 3.x**
- **Pillow** (version 9.0.0 ou ultérieure)
- **tkinter** (généralement inclus avec Python)

---

## Installation

1. **Cloner ou télécharger le dépôt :**

   ```bash
   git clone https://github.com/s0urc3k0d/SquareToCircle.git
   cd SquareToCircle

2. **Installer les dépendances**  
   ```bash
   pip install -r requirements.txt

3. **Lancer l'application**  
   ```bash
   python SquareToCircle.py

## Utilisation

1. **Choix du dossier source**  

2. **Choix du dossier destination**


## Licence

SquareToCircle est un logiciel libre distribué sous la licence GNU General Public License v3.0 (GPLv3).

```text
Copyright (C) [2025]  
S0URC3K0D

Ce programme est libre ; vous pouvez le redistribuer et/ou le modifier selon les termes de la GNU General Public License publiée par la Free Software Foundation, soit la version 3 du GPL, soit (à votre choix) toute version ultérieure.

Ce programme est distribué dans l'espoir qu'il soit utile, mais SANS AUCUNE GARANTIE, ni garantie implicite de COMMERCIALISABILITÉ ou d'ADÉQUATION À UN USAGE PARTICULIER.

Vous devriez avoir reçu une copie de la GNU General Public License avec ce programme. Si ce n'est pas le cas, consultez :  
<https://www.gnu.org/licenses/gpl-3.0.html>
