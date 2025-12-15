# Prompt — Ajouter une faction

## Questionnaire dynamique (généré à la volée)
Ne pas utiliser de liste de questions prédéfinie. À la place :

1. **Génère 5–8 questions adaptées** au contexte, en tenant compte de ce que l'utilisateur a déjà dit et du canon existant.
2. **Format QCM obligatoire** pour chaque question :
   - Propose 2 à 4 choix (A, B, C, D max) pertinents et contrastés.
   - Ajoute toujours une option libre : **"Autre : précise ta réponse"**.
3. **Axes à couvrir** (adapter selon le contexte) :
   - Alignement idéologique (pro-stase / pro-progrès / tiers / neutre)
   - Territoire et implantation
   - Objectifs (public vs caché)
   - Structure et leadership
   - Ressources (technologie, armée, économie)
   - Relations aux Eidons et autres factions
   - Pression narrative exercée
4. **Challenger l'utilisateur** : si l'alignement ou le territoire semble contradictoire avec le canon (ex: faction pro-Judeus basée dans l'Albionis), poser une question de clarification ou proposer des options de résolution.
5. **Itérer** jusqu'à avoir assez d'informations pour rédiger la fiche.

## Sortie attendue
- Créer `universe/factions/<Nom>.md` via `spec/templates/faction.md`.
- Mettre à jour `spec/MANIFEST.md` + `universe/GLOSSARY.md`.
