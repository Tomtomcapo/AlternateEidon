---
description: "Prompt dédié à la création et modification des personnages (entities de type character)."
tools: ['read/readFile', 'edit/createDirectory', 'edit/createFile', 'edit/editFiles', 'search/fileSearch', 'search/listDirectory', 'search/searchResults', 'search/textSearch', 'agent']
---

# Écriture et modification de personnages

> **Fichier prompt dédié** à la création et modification des entités de type `character`.

---

## Prérequis

Avant toute création ou modification :
1. **Consulter `SPECIFICATION.md`** pour le standard Timeliner
2. **Consulter `meta/schemas/character.yaml`** pour le schéma des personnages
3. **Vérifier les personnages liés** pour éviter les contradictions

---

## Structure d'un personnage

```
characters/[nom-personnage]/
├── _index.md              # Fichier de base (état initial)
├── [timestamp].md         # Fichiers delta (évolutions)
├── _writing-guide.md      # Guide d'écriture (optionnel)
└── _img/                  # Images du personnage
```

---

## Sections standard

Utiliser le préfixe `@` pour les sections définies dans le schéma :

| Section | Description |
|---------|-------------|
| `@identity` | Vue d'ensemble, rôle dans l'univers, one-line description |
| `@physical-description` | Apparence physique (`@general`, `@face`, `@clothes`, `@distinguishing-features`) |
| `@personality` | Traits de caractère (`@core-traits`, `@strengths`, `@flaws`, `@fears-desires`, `@behavior-social`) |
| `@abilities` | Compétences et pouvoirs (`@combat`, `@powers`, `@social-intellectual`) |
| `@background` | Histoire et origines |
| `@relationships` | Relations avec d'autres entités |

---

## Template : Nouveau personnage

```markdown
---
name: [Nom]
existence:
  start: "[année]"
  end: unknown
timeline: simulation-era
tags:
  - [tag1]
  - [tag2]
attributes:
  race: [Humain | Eidon]
  writing_level: "[1-4 | Γ]"
  aka: "[Alias optionnel]"
---

# @identity

[Description brève du personnage et de son rôle dans l'univers]

## One-Line Description

> "[Citation ou phrase caractéristique]"

# @physical-description

## @general
[Silhouette, posture, impression générale]

## @face
[Visage, yeux, cheveux]

## @clothes
[Tenue habituelle]

## @distinguishing-features
[Cicatrices, taches de naissance, traits uniques]

# @personality

## @core-traits
[Traits de caractère fondamentaux]

## @strengths
[Forces du personnage]

## @flaws
[Faiblesses et défauts]

## @fears-desires
[Peurs profondes et désirs]

## @behavior-social
[Comportement en société, tics, manies]

# @abilities

## @combat
[Compétences au combat]

## @powers
[Pouvoirs spéciaux si applicable]

## @social-intellectual
[Compétences sociales et intellectuelles]

# @background

[Histoire et origines détaillées]

# @relationships

- [[entity]] `type` — Description de la relation
```

---

## Template : Fichier delta personnage

```markdown
---
timestamp: "[année]"
summary: "[Résumé du changement]"
---

# @[section modifiée]

[Nouveau contenu de la section — remplace entièrement la section précédente]
```

---

## Niveaux d'écriture

| Niveau | Description | Exemples | Profondeur attendue |
|--------|-------------|----------|---------------------|
| **1** | Eidons originels | Maelith, Jadeus, Altert | Maximum — toutes sections détaillées |
| **2** | Humains avec arc majeur | Craith | Élevée — background et personnalité complets |
| **3** | Protagonistes | Leias | Standard — sections principales |
| **4** | Secondaires | Anna, Nelia | Essentiel — identity et relationships |
| **Γ** | Gamma (système) | Gamma | Maximum — cas unique |

---

## Guide d'écriture (`_writing-guide.md`)

Pour les personnages de niveau 1-3, créer un guide d'écriture compagnon :

```markdown
# Guide d'écriture — [Nom]

## Philosophie centrale
[Ce qui définit le personnage en une phrase]

## Préférences linguistiques
### Ce qu'il/elle fait
- [Patterns de dialogue]

### Ce qu'il/elle NE fait PAS
- Ne pas : [Anti-patterns]

## Comportements caractéristiques
[Tics, manies, réactions typiques]

## Évolution selon les arcs
[Comment le personnage change au fil du temps]
```

---

## Règles de cohérence

### Avant d'écrire
- [ ] Lire le `_index.md` complet du personnage
- [ ] Consulter le `_writing-guide.md` s'il existe
- [ ] Vérifier les relations avec les autres personnages
- [ ] Identifier la période chronologique concernée

### Pendant l'écriture
- [ ] Maintenir la voix et le ton du personnage
- [ ] Respecter les traits de personnalité établis
- [ ] Utiliser les références croisées `[[entity]]`
- [ ] Ne pas contredire le background existant

### Après l'écriture
- [ ] Vérifier la cohérence avec le canon
- [ ] S'assurer que le frontmatter est complet
- [ ] Valider les références vers des entités existantes

---

## Relations typées

Utiliser les types de relations entre backticks :

**Personnelles** : `spouse`, `parent`, `child`, `sibling`, `friend`, `rival`, `enemy`, `lover`

**Professionnelles** : `employer`, `employee`, `ally`, `mentor`, `student`, `colleague`

**Exemple** :
```markdown
# @relationships

- [[characters/gamma]] `ally` `friend` — Compagnon de voyage depuis l'Arc 1
- [[characters/tress]] `enemy` — Tyran responsable de la mort de son père
- [[characters/meldon]] `parent` — Père décédé, source de ses compétences de survie
```

---

*Pour toute question sur le format, consulter `SPECIFICATION.md`.*
