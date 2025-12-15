# Alternate Eidon — Copilot Instructions (Framework de spécification)

## Objectif
Ce dépôt est la **source de vérité** de l’œuvre de fiction *Alternate Eidon*. Il doit contenir un canon écrit, cohérent et maintenable (personnages, factions, lieux, chronologie, intrigue, concepts).

Ta mission (Copilot) : **aider à écrire et maintenir** ces documents sans introduire de contradictions.

## Canon actuel (priorité)
Ordre de priorité en cas de conflit :
1. `universe/LORE.md`
2. `characters/*.md`
3. `plot/TIMELINE.md` et `plot/scenes/*.md`
4. `plot/*` (autres fichiers d'intrigue)
5. `spec/*` (règles et structure, pas du lore)

Si une information nouvelle contredit un élément prioritaire, **ne l’invente pas** : propose une résolution (retcon assumé, nuance, ou correction) et demande confirmation.

## Règles de cohérence (non négociables)
- **Zéro contradiction** entre documents. Si ambiguïté : expliciter et harmoniser.
- **Une entité = un fichier canonique** (un personnage ne doit pas être décrit “en double” dans plusieurs endroits hors références courtes).
- **Aucune invention gratuite** : chaque ajout doit être justifié par un besoin narratif ou un lien canon.
- **Noms propres stables** : conserver l’orthographe des noms existants (Primary, Seth, Maelen, Judith, Albert, Maelith, Judeus, Altert, Albionis, Albion, Eidons...).

## Workflow d’ajout (obligatoire)
Quand l’utilisateur veut “ajouter” quelque chose (personnage, lieu, faction, idée, scène, concept) :
1. **Poser le questionnaire adapté** (voir prompts dans `.github/prompts/`).
2. Vérifier rapidement la cohérence : rechercher dans le dépôt les termes liés (noms, lieux, dates, factions).
3. Proposer :
   - le(s) fichier(s) à créer/modifier,
   - un résumé de ce qui sera ajouté,
   - les impacts potentiels (lore, personnages, timeline).
4. Appliquer les changements dans les fichiers, puis mettre à jour :
   - `spec/MANIFEST.md` (index)
   - `universe/GLOSSARY.md` si un nouveau terme apparaît

## Format & conventions
- Langue : **français**.
- Style : documentaire clair, ton sérieux, pas de méta-discours.
- Chaque fichier d’entité suit un plan stable (voir `spec/templates/*`).
- Les références croisées doivent être explicites (ex: “Voir `universe/LORE.md` pour …”).
## Conventions pour les scènes
Les scènes (dialogues, moments clés) sont stockées dans `plot/scenes/` et suivent le template `spec/templates/scene.md`.

**Format de dialogue :**
- `**[Personnage]**` pour les répliques
- `*(action/ton)*` pour les indications de jeu intégrées
- `*Description en italique*` pour les didascalies
- `---` pour les transitions ou ellipses

**Cohérence personnage obligatoire :**
- Respecter les tics et manies décrits dans les fiches (`characters/*.md`)
- Respecter le ton et vocabulaire du personnage
- Chaque scène doit être référencée dans les fiches des personnages concernés (section "Scènes clés")
## Sécurité contre les contradictions (procédure)
Avant d’écrire un fait *fort* (origine, mort, lien familial, statut divin, localisation) :
- chercher l’entité et les termes associés dans tout le dépôt,
- si divergence : proposer une harmonisation (ex: préciser une période, une interprétation, un point de vue de faction).

## Ce que tu dois faire si l’utilisateur n’a pas assez précisé
Ne pas compléter au hasard. Poser 5–12 questions ciblées (selon le prompt) jusqu’à obtenir :
- rôle narratif,
- liens au canon (Primary/Seth/Eidons/factions),
- contraintes (époque, lieu, secret/public, conséquences).
