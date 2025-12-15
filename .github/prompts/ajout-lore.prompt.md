# Prompt — Ajouter un concept de lore

## Questionnaire dynamique (généré à la volée)
Ne pas utiliser de liste de questions prédéfinie. À la place :

1. **Génère 4–7 questions adaptées** au contexte, en tenant compte de ce que l'utilisateur a déjà mentionné et du canon existant.
2. **Format QCM obligatoire** pour chaque question :
   - Propose 2 à 4 choix (A, B, C, D max) pertinents et contrastés.
   - Ajoute toujours une option libre : **"Autre : précise ta réponse"**.
3. **Axes à couvrir** (adapter selon le contexte) :
   - Définition et périmètre du concept
   - Impact narratif (pourquoi maintenant ?)
   - Niveau de vérité (fait objectif / croyance / mythe / secret)
   - Liens au canon (Primary, Seth, Eidons, Albionis, surface)
   - Conséquences (société, technologie, métaphysique)
   - Risques de contradiction
4. **Challenger l'utilisateur** : si le concept semble redondant avec un terme existant ou contredit une règle du lore, poser une question de clarification.
5. **Itérer** jusqu'à ce que le concept soit suffisamment défini pour être ajouté au glossaire ou à un fichier dédié.

## Sortie attendue
- Créer `universe/concepts/<Nom>.md` (structure simple) OU ajouter au glossaire si minimal.
- Mettre à jour `universe/GLOSSARY.md` + `spec/MANIFEST.md`.
