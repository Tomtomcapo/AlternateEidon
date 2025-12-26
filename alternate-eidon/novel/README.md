# Compilation des chapitres en PDF

Ce dossier contient le script pour compiler les chapitres markdown en PDF format livre roman français.

## Prérequis

### Installation de Pandoc et LaTeX

**Sur macOS :**
```bash
# Installer Pandoc
brew install pandoc

# Installer BasicTeX (distribution LaTeX légère)
brew install --cask basictex

# Mettre à jour tlmgr et installer les packages nécessaires
sudo tlmgr update --self
sudo tlmgr install collection-fontsrecommended \
  fancyhdr \
  setspace \
  microtype \
  xetex \
  unicode-math \
  libertine
```

**Sur Linux (Debian/Ubuntu) :**
```bash
sudo apt-get install pandoc texlive-xetex texlive-fonts-recommended texlive-latex-extra
```

## Utilisation

### Compiler tous les chapitres en un seul PDF

```bash
cd novel
python compile_pdf.py --all
```

Génère : `output/alternate-eidon-complet.pdf`

### Compiler chaque chapitre séparément

```bash
python compile_pdf.py --separate
```

Génère : `output/chapitre-01.pdf`, `output/chapitre-02.pdf`, etc.

### Compiler un chapitre spécifique

```bash
python compile_pdf.py --chapter 5
```

Génère : `output/chapitre-05.pdf`

## Format du PDF

Le PDF généré utilise les paramètres standard d'un livre roman français :

- **Format** : A5 (148 × 210 mm) - format livre poche
- **Police** : Linux Libertine O (serif classique)
- **Taille** : 11pt
- **Marges** :
  - Gauche : 2 cm (pour la reliure)
  - Droite : 1,5 cm
  - Haut/Bas : 2 cm
- **Interligne** : 1,2
- **En-têtes** : Numéros de page et titres de chapitres

## Personnalisation

Pour modifier les paramètres de mise en page, éditez les valeurs dans `compile_pdf.py` :

```python
BOOK_CONFIG = {
    "papersize": "a5",        # Format : a4, a5, letter, etc.
    "fontsize": "11pt",       # Taille : 10pt, 11pt, 12pt
    "margin-left": "2cm",     # Marges personnalisées
    "margin-right": "1.5cm",
    "margin-top": "2cm",
    "margin-bottom": "2cm",
    "mainfont": "Linux Libertine O",  # Police principale
    "linestretch": "1.2",     # Interligne
}
```

## Dépannage

### Erreur "pandoc: command not found"
Installez Pandoc avec `brew install pandoc`

### Erreur LaTeX
Vérifiez que XeLaTeX est installé : `which xelatex`
Si absent, installez BasicTeX comme indiqué ci-dessus.

### Police manquante
Si Linux Libertine O n'est pas disponible, le script utilisera la police par défaut.
Pour installer Linux Libertine :
- macOS : `brew install --cask font-linux-libertine`
- Linux : `sudo apt-get install fonts-linuxlibertine`

### Encodage UTF-8
Tous les fichiers markdown doivent être encodés en UTF-8. Si vous rencontrez des problèmes d'encodage, vérifiez l'encodage des fichiers sources.

## Structure des fichiers

```
novel/
├── chapters/              # Chapitres markdown
│   ├── chapitre-01.md
│   ├── chapitre-02.md
│   └── ...
├── output/               # PDFs générés (créé automatiquement)
│   ├── alternate-eidon-complet.pdf
│   ├── chapitre-01.pdf
│   └── metadata.yaml
├── compile_pdf.py        # Script de compilation
└── README.md            # Ce fichier
```
