#!/usr/bin/env python3
"""
Script de compilation des chapitres markdown en PDF et EPUB format livre roman français.

Usage:
    python compile_pdf.py --all              # Compile tous les chapitres en PDF et EPUB
    python compile_pdf.py --separate         # Compile chaque chapitre en PDF et EPUB séparés
    python compile_pdf.py --chapter 5        # Compile uniquement le chapitre 5 en PDF et EPUB
"""

import argparse
import subprocess
import os
from pathlib import Path
from typing import List

# Configuration
CHAPTERS_DIR = Path("chapters")
OUTPUT_DIR = Path("output")
TEMPLATE_DIR = Path("templates")

# Format livre français standard
BOOK_CONFIG = {
    "papersize": "a5",  # Format A5 (148 x 210 mm) - format livre poche
    "fontsize": "11pt",
    "margin-left": "2cm",
    "margin-right": "1.5cm",
    "margin-top": "2cm",
    "margin-bottom": "2cm",
    "mainfont": "Palatino",  # Police serif classique présente sur macOS
    "linestretch": "1.0",  # Interligne compact pour dialogues
    "documentclass": "book",
}


def get_chapters(chapters_dir: Path) -> List[Path]:
    """Récupère tous les fichiers de chapitres triés."""
    chapters = sorted(chapters_dir.glob("chapitre-*.md"))
    return chapters


def create_metadata_file(title: str, author: str = "Thomas", output_path: Path = None) -> Path:
    """Crée un fichier de métadonnées YAML pour Pandoc."""
    metadata = f"""---
title: "{title}"
author: "{author}"
lang: fr-FR
documentclass: book
papersize: a5
fontsize: 11pt
geometry:
  - left=2cm
  - right=1.5cm
  - top=2cm
  - bottom=2cm
mainfont: Palatino
linestretch: 1.0
toc: false
numbersections: false
header-includes: |
  \\usepackage{{fancyhdr}}
  \\pagestyle{{fancy}}
  \\fancyhf{{}}
  \\fancyhead[LE,RO]{{\\thepage}}
  \\fancyhead[RE]{{\\leftmark}}
  \\fancyhead[LO]{{\\rightmark}}
  \\renewcommand{{\\headrulewidth}}{{0pt}}
  \\usepackage{{setspace}}
  \\usepackage{{microtype}}
---
"""
    
    if output_path is None:
        output_path = OUTPUT_DIR / "metadata.yaml"
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(metadata, encoding='utf-8')
    return output_path


def compile_pdf(
    input_files: List[Path],
    output_file: Path,
    title: str,
    use_toc: bool = False
) -> bool:
    """Compile les fichiers markdown en PDF avec Pandoc."""
    
    # Créer le répertoire de sortie
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Créer le fichier de métadonnées
    metadata_file = create_metadata_file(title)
    
    # Construire la commande Pandoc
    cmd = [
        "pandoc",
        str(metadata_file),
    ]
    
    # Ajouter tous les fichiers d'entrée
    cmd.extend([str(f) for f in input_files])
    
    # Options de compilation
    cmd.extend([
        "-o", str(output_file),
        "--pdf-engine=xelatex",
        "--standalone",
    ])
    
    if use_toc:
        cmd.append("--toc")
    
    # Exécuter Pandoc
    print(f"Compilation de {len(input_files)} fichier(s) vers {output_file}...")
    print(f"Commande: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"✓ PDF généré : {output_file}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Erreur lors de la compilation :")
        print(e.stderr)
        return False
    except FileNotFoundError:
        print("✗ Erreur : Pandoc n'est pas installé.")
        print("Installation : brew install pandoc")
        print("Et XeLaTeX : brew install --cask basictex")
        print("Puis : sudo tlmgr update --self && sudo tlmgr install collection-fontsrecommended")
        return False


def compile_epub(
    input_files: List[Path],
    output_file: Path,
    title: str,
    author: str = "Thomas",
    use_toc: bool = False
) -> bool:
    """Compile les fichiers markdown en EPUB avec Pandoc."""
    
    # Créer le répertoire de sortie
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Construire la commande Pandoc
    cmd = [
        "pandoc",
    ]
    
    # Ajouter tous les fichiers d'entrée
    cmd.extend([str(f) for f in input_files])
    
    # Options de compilation EPUB
    cmd.extend([
        "-o", str(output_file),
        "--standalone",
        f"--metadata=title:{title}",
        f"--metadata=author:{author}",
        "--metadata=lang:fr-FR",
    ])
    
    if use_toc:
        cmd.append("--toc")
    
    # Exécuter Pandoc
    print(f"Compilation de {len(input_files)} fichier(s) vers {output_file}...")
    print(f"Commande: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"✓ EPUB généré : {output_file}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Erreur lors de la compilation EPUB :")
        print(e.stderr)
        return False
    except FileNotFoundError:
        print("✗ Erreur : Pandoc n'est pas installé.")
        print("Installation : brew install pandoc")
        return False


def compile_all_chapters(chapters: List[Path]) -> bool:
    """Compile tous les chapitres en un seul PDF et EPUB."""
    # Compilation PDF
    pdf_file = OUTPUT_DIR / "alternate-eidon-complet.pdf"
    pdf_success = compile_pdf(
        chapters,
        pdf_file,
        "Alternate Eidon",
        use_toc=True
    )
    
    # Compilation EPUB
    epub_file = OUTPUT_DIR / "alternate-eidon-complet.epub"
    epub_success = compile_epub(
        chapters,
        epub_file,
        "Alternate Eidon",
        use_toc=True
    )
    
    return pdf_success and epub_success


def compile_separate_chapters(chapters: List[Path]) -> bool:
    """Compile chaque chapitre en PDF et EPUB séparés."""
    success = True
    for chapter in chapters:
        chapter_name = chapter.stem  # Ex: "chapitre-01"
        
        # Extraire le numéro de chapitre pour le titre
        chapter_num = chapter_name.split("-")[-1]
        title = f"Alternate Eidon - Chapitre {chapter_num}"
        
        # Compilation PDF
        pdf_file = OUTPUT_DIR / f"{chapter_name}.pdf"
        pdf_result = compile_pdf(
            [chapter],
            pdf_file,
            title,
            use_toc=False
        )
        
        # Compilation EPUB
        epub_file = OUTPUT_DIR / f"{chapter_name}.epub"
        epub_result = compile_epub(
            [chapter],
            epub_file,
            title,
            use_toc=False
        )
        
        success = success and pdf_result and epub_result
    
    return success


def compile_specific_chapter(chapter_num: int, chapters: List[Path]) -> bool:
    """Compile un chapitre spécifique en PDF et EPUB."""
    # Chercher le chapitre correspondant
    chapter_file = None
    for chapter in chapters:
        if f"chapitre-{chapter_num:02d}" in chapter.name:
            chapter_file = chapter
            break
    
    if chapter_file is None:
        print(f"✗ Chapitre {chapter_num} non trouvé.")
        return False
    
    title = f"Alternate Eidon - Chapitre {chapter_num}"
    
    # Compilation PDF
    pdf_file = OUTPUT_DIR / f"chapitre-{chapter_num:02d}.pdf"
    pdf_success = compile_pdf(
        [chapter_file],
        pdf_file,
        title,
        use_toc=False
    )
    
    # Compilation EPUB
    epub_file = OUTPUT_DIR / f"chapitre-{chapter_num:02d}.epub"
    epub_success = compile_epub(
        [chapter_file],
        epub_file,
        title,
        use_toc=False
    )
    
    return pdf_success and epub_success


def main():
    parser = argparse.ArgumentParser(
        description="Compile les chapitres markdown en PDF et EPUB format livre roman français."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--all",
        action="store_true",
        help="Compile tous les chapitres en un seul PDF et EPUB"
    )
    group.add_argument(
        "--separate",
        action="store_true",
        help="Compile chaque chapitre en PDF et EPUB séparés"
    )
    group.add_argument(
        "--chapter",
        type=int,
        metavar="N",
        help="Compile uniquement le chapitre N en PDF et EPUB"
    )
    
    args = parser.parse_args()
    
    # Vérifier que le répertoire des chapitres existe
    if not CHAPTERS_DIR.exists():
        print(f"✗ Erreur : Le répertoire {CHAPTERS_DIR} n'existe pas.")
        return 1
    
    # Récupérer les chapitres
    chapters = get_chapters(CHAPTERS_DIR)
    if not chapters:
        print(f"✗ Aucun chapitre trouvé dans {CHAPTERS_DIR}")
        return 1
    
    print(f"Chapitres trouvés : {len(chapters)}")
    for chapter in chapters:
        print(f"  - {chapter.name}")
    print()
    
    # Exécuter la compilation appropriée
    if args.all:
        success = compile_all_chapters(chapters)
    elif args.separate:
        success = compile_separate_chapters(chapters)
    else:  # args.chapter
        success = compile_specific_chapter(args.chapter, chapters)
    
    return 0 if success else 1


if __name__ == "__main__":
    exit(main())
