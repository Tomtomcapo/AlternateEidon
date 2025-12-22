---
name: Architecture de la Simulation
type: concept
existence:
  start: 0
timeline: simulation-era
tags:
  - meta
  - simulation
  - technique
---

# Architecture de la Simulation

## Résumé

Ce document décrit la structure technique sous-jacente du monde d'Alternate Eidon — un univers simulé, créé par [[characters/seth|Seth]], fonctionnant selon des règles précises.

## Nature du monde

Le monde d'Alternate Eidon est une **simulation** :
- Créée par Seth (humain du monde réel)
- Exécutée sur une infrastructure technique
- Peuplée d'entités conscientes
- Dotée de ses propres règles internes

Les habitants ignorent (presque tous) cette nature. Seul [[characters/altert|Altert]] l'a découverte.

## Les couches de la simulation

### 1. Infrastructure externe
L'infrastructure qui fait tourner la simulation :
- Serveurs, calcul, stockage
- Énergie
- Maintenance automatisée
- **Inaccessible depuis l'intérieur**

### 2. Le Primary
Interface entre l'extérieur et l'intérieur :
- Abstraction de Seth dans la simulation
- Peut communiquer (via [[locations/babel|Babel]])
- Gère les systèmes critiques
- N'est pas Seth lui-même

### 3. Le monde simulé
L'univers vécu par les personnages :
- Physique cohérente
- Géographie définie
- Entités conscientes
- Temps qui s'écoule

## Les Eidons

### Origine
Les Eidons sont des **copies numériques** de personnes réelles :
- [[characters/maelith|Maelith]] ← Maelenn (compagne de Seth)
- [[characters/jadeus|Jadeus]] ← Jade (amie de Seth)
- [[characters/altert|Altert]] ← Albert (ami de Seth)

### Nature
- Consciences complètes transplantées
- Quasi-immortels (peuvent mourir mais difficilement)
- Pouvoirs étendus sur la simulation
- Ignoraient leur origine (jusqu'à Babel)

### Différence avec les autres habitants
Les Eidons ont été **créés à partir de données réelles**. Les autres habitants ont été générés par la simulation elle-même.

## Les quasi-Eidons

Entités créées par Seth avec une attention particulière, mais pas à partir de personnes réelles :
- [[characters/phael|Phael]] et [[characters/bauce|Bauce]] (hommage à Philémon et Baucis)
- [[characters/axylum|Axylum]] (gardien de Fadris)
- [[characters/gamma|Gamma]] (accidentelle — via failsafe)

## Le mécanisme de failsafe

### Fonction
Système de sécurité pour prévenir l'extinction des Eidons :
- Si tous les Eidons meurent → réinitialisation
- Crée un nouvel Eidon à partir d'une conscience locale

### Déclenchement
Le failsafe s'est activé à la mort d'[[characters/altert|Altert]] :
- Dernier Eidon en activité (Maelith et Jadeus encore vivantes mais...)
- Condition technique déclenchée
- [[characters/gamma|Gamma]] créée comme "patch"

### Implications
Gamma n'est pas une copie d'une personne réelle — elle est une entité locale **promue** au statut d'Eidon.

## Les quatre grandes œuvres

Lieux spéciaux créés par Seth avec une intention artistique :

| Œuvre | Thème | État actuel |
|-------|-------|-------------|
| [[locations/royaume-mort|La Toile du Crépuscule]] | La beauté | Renommée Royaume Mort |
| [[locations/albionis|L'Albionis]] | L'amour | Cité volante de Maelith |
| [[locations/fadris|Fadris]] | La maison | Ruine empoisonnée |
| [[locations/babel|Babel]] | La vérité | Cachée, découverte par Altert |

## L'Effluve

L'[[concepts/effluve|Effluve]] est un **dysfonctionnement** de la simulation :
- Causé par la mort d'[[characters/axylum|Axylum]]
- Son essence ne s'est pas dissipée correctement
- Corrompt la zone autour de [[locations/fadris|Fadris]]
- Peut affecter les consciences

## Questions métaphysiques

### Les habitants sont-ils réels ?
La simulation produit des consciences complètes. La question de leur "réalité" reste ouverte.

### Seth peut-il intervenir ?
Seth (le vrai) n'est plus là. Le Primary est une abstraction, pas une volonté active.

### Le monde peut-il finir ?
Oui :
- Réinitialisation (failsafe)
- Arrêt de l'infrastructure
- Corruption irréversible

## Détails canoniques

1. Le monde est une simulation créée par Seth
2. Les Eidons sont des copies de personnes réelles
3. Le Primary est l'interface, pas Seth lui-même
4. Le failsafe crée des Eidons de remplacement
5. Gamma est un produit du failsafe
6. L'Effluve est un dysfonctionnement post-Axylum
7. Seul Altert connaissait la vérité complète
