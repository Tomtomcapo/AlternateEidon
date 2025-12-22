---
description: "Prompt dédié à la création et modification des lieux (entities de type location)."
tools: ['read/readFile', 'edit/createDirectory', 'edit/createFile', 'search/fileSearch', 'search/listDirectory', 'search/searchResults', 'search/textSearch', 'web/fetch']
---

# Écriture et modification de lieux

> **Fichier prompt dédié** à la création et modification des entités de type `location`.

---

## Prérequis

Avant toute création ou modification :
1. **Consulter `SPECIFICATION.md`** pour le standard Timeliner
2. **Vérifier les lieux et personnages liés** pour éviter les contradictions
3. **Situer le lieu dans la chronologie** (existence, changements majeurs)

---

## Structure d'un lieu

```
locations/[nom-lieu]/
├── _index.md              # Fichier de base (état initial)
├── [timestamp].md         # Fichiers delta (évolutions)
└── _img/                  # Images du lieu
```

---

## Sections suggérées

| Section | Description |
|---------|-------------|
| **Identité** | Nom, type, attributs de base, régime |
| **Origine** | Fondation, créateur, contexte historique |
| **Atmosphère** | Paysages, caractère, direction artistique |
| **Gouvernement** | Structure politique, dirigeants |
| **Rapport aux Eidons** | Relations avec les entités divines |
| **Lieux notables** | Sous-lieux importants |
| **Connaissance** | Ce que savent les différentes factions |

---

## Template : Nouveau lieu

```markdown
---
name: [Nom du lieu]
type: location
existence:
  start: [année de création/fondation]
  end: [année de destruction | unknown]
timeline: simulation-era
tags:
  - [nation | ville | bâtiment | région]
  - [tag thématique]
---

# [Nom du lieu] — [Sous-titre évocateur]

## Identité

**[Nom]** est [description en une phrase].

### Attributs de base
- **Type** : [Nation | Ville | Bâtiment | Région | Île]
- **Régime** : [Type de gouvernement si applicable]
- **Fondateur** : [[characters/fondateur]] ([année])
- **Dirigeant actuel** : [[characters/dirigeant]] | Vacant
- **Territoire** : [Description géographique]

## Origine

[Histoire de la fondation et contexte]

### La vision du fondateur
[Objectifs originels du lieu]

### La construction
[Comment le lieu a été créé/développé]

## Atmosphère

### Paysages
[Description visuelle de l'environnement]

### Caractère
[Ambiance, ton, impression générale]

### Direction artistique
**Couleurs dominantes** :
- [Couleur 1] — [symbolisme]
- [Couleur 2] — [symbolisme]

**Inspirations visuelles** :
- [Référence architecturale/culturelle]

## Gouvernement

### Structure
[Organisation politique]

### Enjeux actuels
[Conflits, tensions, défis]

## Rapport aux Eidons

### [Nom de l'Eidon]
[Relation du lieu avec cet Eidon]

## Lieux notables

### [Sous-lieu 1]
[Description brève]

### [Sous-lieu 2]
[Description brève]

## Connaissance

| Qui | Ce qu'ils savent |
|-----|------------------|
| [Faction/Personnage] | [Niveau de connaissance] |

## Importance narrative

[Rôle du lieu dans l'histoire]
```

---

## Template : Fichier delta lieu

```markdown
---
timestamp: "[année]"
summary: "[Résumé du changement — ex: destruction, changement de régime]"
---

# [Section modifiée]

[Nouveau contenu de la section — remplace entièrement la section précédente]
```

---

## Types de lieux

| Type | Description | Exemples |
|------|-------------|----------|
| **Nation** | Entité politique avec territoire | Eldora, Royaume Mort, Olivor |
| **Ville** | Centre urbain | Mortem-Onell |
| **Région** | Zone géographique | Extrême-Est, Terres du Sud |
| **Île** | Territoire insulaire | Fadris, Albionis |
| **Bâtiment** | Structure spécifique | Babel (inachevé) |
| **Concept spatial** | Lieu métaphorique | Silentes |

---

## Atmosphères par lieu canonique

| Lieu | Couleurs | Ton | Inspiration |
|------|----------|-----|-------------|
| **Eldora** | Vert, or, blanc | Lumineux mais fragile | Europe classique |
| **Royaume Mort** | Rouge sang, noir | Sombre, pénitent | Gothique |
| **Albionis** | Bleu, argent | Éthéré, mélancolique | Île mystique |
| **Fadris** | Corrompues (post-Axylum) | Dangereux, nostalgique | Paradis perdu |
| **Olivor** | Terre, ocre | Oppressif, résistant | Terres arides |

---

## Liens avec les Quatre Grandes Œuvres

Seth a créé quatre lieux majeurs chargés de sens personnel :

1. **La Toile du Crépuscule** (devenue Royaume Mort) — La beauté artistique
2. **L'Albionis** — La lettre d'amour à Maelenn
3. **Fadris** — La maison, le paradis perdu
4. **Babel** — L'humanité (inachevée)

Lors de l'écriture de ces lieux, maintenir leur signification symbolique.

---

## Règles de cohérence

### Avant d'écrire
- [ ] Vérifier si le lieu existe déjà
- [ ] Identifier les personnages associés
- [ ] Situer le lieu géographiquement
- [ ] Déterminer la période chronologique

### Pendant l'écriture
- [ ] Maintenir la cohérence atmosphérique
- [ ] Utiliser les références croisées `[[entity]]`
- [ ] Respecter les relations établies avec les Eidons
- [ ] Ne pas contredire les événements historiques

### Après l'écriture
- [ ] Vérifier le frontmatter
- [ ] Valider les références vers des entités existantes
- [ ] S'assurer de la cohérence chronologique

---

## Évolution des lieux

Les lieux évoluent au fil du temps. Utiliser les fichiers delta pour :
- Changements de régime politique
- Destructions ou reconstructions
- Modifications atmosphériques (ex: végétation rouge du Royaume Mort)
- Événements majeurs affectant le lieu

**Exemple** : Le Royaume Mort après le massacre (~700)
```markdown
---
timestamp: "700"
summary: "Renommage après le massacre de la Toile du Crépuscule"
---

# Identité

**Regnum Mortuum** (Royaume Mort) — anciennement la Toile du Crépuscule.

## Atmosphère

### Paysages
La végétation est désormais **rouge sang**. Les arbres, les fleurs, l'herbe — tout porte la couleur du massacre.
```

---

*Pour toute question sur le format, consulter `SPECIFICATION.md`.*
