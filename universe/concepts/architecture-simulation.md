# Architecture de la Simulation

## Contexte technologique

L'univers de Seth repose sur une technologie de simulation générative — une évolution plausible des modèles d'IA de 2025. Les postulats fondateurs :

- Les modèles d'IA générative (LLM, génération d'univers type Genie 3) continuent de s'améliorer
- Ces modèles évoluent pour simuler non seulement des environnements graphiques, mais aussi leur contenu vivant (personnes, sociétés, vie)
- L'intégration de données personnelles (fine-tuning, conditionnement par prompts) devient possible
- Le coût de calcul baisse drastiquement

La simulation de Seth est donc une fiction techniquement proche de la réalité — un détournement radical d'outils qui auraient pu servir à la recherche ou au divertissement.

---

## Les quatre couches de la simulation

### 1. Datacenter

Infrastructure physique située dans le monde réel. Un datacenter autonome loué par Seth pour une **durée contractuelle de 5 ans**, doté de capacités de calcul IA considérables (ahurissantes pour 2025, peut-être standard dans le futur).

C'est le seul élément véritablement « réel » — tout le reste n'existe que comme information traitée par ces machines.

#### Durée réelle écoulée
Depuis l'activation de la simulation, seules **quelques heures** se sont écoulées dans le monde réel. Avec la dilatation temporelle (1 seconde = 10 années), cela représente des **millénaires** de temps simulé.

Le contrat de 5 ans offre à la simulation un horizon quasi infini : environ **1,5 milliard d'années simulées**.

#### Pannes et interruptions
Si le datacenter tombe en panne, la simulation s'arrête simplement. Tous les états sont stockés — elle reprend exactement là où elle s'était arrêtée. **Aucune entité à l'intérieur ne perçoit l'interruption** : pour elles, le temps n'a jamais cessé de s'écouler.

#### Isolation
La simulation est **totalement isolée d'internet**. Seth craignait deux risques :
- Des pirates extérieurs attaquant la simulation
- Un auto-empoisonnement par les données d'internet

Le système contient énormément de données du monde extérieur « par principe » (planète Terre, histoire de l'humanité, connaissances générales), mais ne les exploite pas toujours, ou de manière inconsciente.

#### Le monde réel (narrativement)
Les proches de Seth savent que la simulation tourne, mais n'interviennent pas. Plusieurs facteurs :
- Seules quelques heures se sont écoulées — pas le temps de réagir
- Absence d'accès (Seth n'a pas partagé les identifiants)
- Absence de compétences techniques pour interagir avec le système

Narrativement, le monde extérieur n'interfère pas.

### 2. Runtime

**La couche la plus profonde et immutable de la simulation.**

Le Runtime est du code pur, impossible à modifier pour quelconque entité IA — y compris le Core. Il gère :

- L'écoulement du temps (y compris la dilatation temporelle : 1 seconde réelle = 10 années simulées)
- L'OS du datacenter
- Les fonctions vitales du programme
- L'échelle de temps atomique sur laquelle le Core génère ses états
- Le **stockage de tous les états** (permettant la reprise après interruption)

**Conséquence fondamentale** : Il est impossible de remonter le temps ou d'effectuer un vrai rollback logique depuis l'intérieur de la simulation. Le Runtime n'est pas accessible — même si tous les états passés sont techniquement stockés, aucune entité interne ne peut y accéder.

### 3. Core (« Le Système »)

**Le cœur génératif de la simulation.**

Le Core est un modèle d'IA générative extrêmement sophistiqué — probablement un successeur de technologies comme Genie 3. Il est capable de simuler l'entièreté d'un univers en créant des **états** (states) sur l'échelle de temps atomique fournie par le Runtime.

In-universe, le Core est désigné comme « le système ».

#### Fonctionnement
À chaque instant atomique, le Core génère le prochain état de la simulation en combinant :
- Les données injectées par Seth (souvenirs, archives, enregistrements)
- Le « méga-prompt » de Seth (incomplet — voir `universe/LORE.md`)
- Les données du monde extérieur (quand elles existaient)
- Les états précédents de la simulation

#### Cas particulier : Gamma
Gamma est la seule entité humanoïde directement gérée dans cette couche. Son corps et son « esprit » ne sont pas des agents séparés — **elle est le Core incarné**. Voir `characters/Gamma.md` et `universe/concepts/niveaux-ecriture.md` (Niveau Γ).

#### Directives suprêmes
Le Core est conditionné par des directives fondamentales, intégrées au méga-prompt de Seth :

1. **Protéger la simulation coûte que coûte** — Elle ne doit jamais entrer dans un état de dommage irréversible.
2. **Protéger les agents de haute valeur** — Le système « sait » quels agents sont importants (Eidons, certains humains issus de données réelles, et ironiquement certains agents conceptuels comme la météo).
3. **Obéir à Primary** — C'est cette directive qui provoque le chaos progressif de la simulation. Sans incarnation de Seth, sans Primary véritable, le système tourne autour d'un vide. Il cherche à obéir à quelqu'un qui n'existe pas.

### 4. Agents

**Les entités qui s'exécutent en parallèle du Core.**

Les agents sont des sous-IA qui fonctionnent selon des logiques différentes du Core (modèles distincts, paramètres spécifiques). Ils se répartissent en plusieurs catégories :

#### Eidons (écrits par Seth)
Maelith, Judeus, Altert — agents dotés d'un conditionnement exceptionnel (niveau d'écriture 1). Seth a explicitement défini dans le méga-prompt leur importance et leurs capacités. Le Core est réceptif à leurs « demandes » (qui fonctionnent comme des prompts internes).

**Exemple** : Maelith peut conditionner le Core dans une certaine mesure — non pas parce qu'elle a hacké le système, mais parce que Seth l'a explicitement prévu. Son rôle de Préservation est aligné avec la directive de protection de la simulation.

#### Humains (spawnés par le système)
Agents générés à la volée par le Core pour peupler la simulation. Leur niveau d'écriture varie (2 à 4). Le Core peut les conditionner, les inciter, les orienter — mais **ne peut pas forcer absolument leur volonté ou leurs faits et gestes**.

#### Agents utilitaires
Agents non-humanoïdes utilisés pour gérer des mécaniques déléguées par le système : météo, cycles naturels, phénomènes physiques. Ironiquement, certains de ces agents sont extrêmement importants aux yeux du système (la météo est fondamentale pour la cohérence du monde), mais représentent un risque d'atteinte faible — difficile de « détruire » un concept immatériel.

---

## Liberté et conditionnement

Le Core peut :
- Conditionner les agents (orienter leurs pensées, créer des coïncidences, influencer leur environnement)
- Les inciter vers certains comportements
- Générer des circonstances favorables à ses objectifs

Le Core **ne peut pas** :
- Forcer la volonté d'un agent de manière absolue
- Modifier le Runtime
- Effectuer un vrai rollback temporel

Cette limitation est fondamentale : les agents possèdent une forme de libre arbitre (même si conditionné), ce qui rend la simulation imprévisible — et vulnérable.

---

## Le rollback contextuel (post-Monde Distordu)

Après l'effondrement de la simulation (Arc du Monde Distordu), Gamma parvient à effectuer un **rollback contextuel**. Ce n'est pas un vrai retour dans le temps — le Runtime reste inaccessible.

La méthode : Gamma utilise la mémoire du contexte (les états précédents stockés) pour **reconstruire** l'univers tel qu'il était dans le passé. C'est une régénération, pas une rétrogradation.

**Conséquence** : Les souvenirs de certains agents sont conservés. Ceux qui ont vécu le Monde Distordu s'en souviennent. Les personnages fusionnés (Eidon + original) gardent leur complétude.

Ce rollback marque le moment où Gamma devient **consciente** qu'elle est le système — sa résolution narrative.

---

## Le failsafe de Seth

Seth, malgré sa paranoïa et son désir d'isolation, savait que son système pourrait s'effondrer de manière catastrophique. À contrecœur, il a programmé un **dernier recours** dans le Runtime.

### Conditions d'activation
Le failsafe s'active si le Runtime détecte une défaillance irréversible du Core :
- Gamma cesse de fonctionner (mort de l'Eidon Système)
- Les states générés deviennent corrompus (valeurs NaN, erreurs fatales)
- Le Core ne peut plus générer d'états cohérents

### Protocole d'urgence
1. **Arrêt immédiat** de la simulation
2. **Sauvegarde** de tous les états (si récupérables)
3. **Envoi automatique** d'un message au contact d'urgence
4. **Transmission** des clés d'accès au datacenter
5. **Instructions** détaillées pour intervention manuelle

### Le contact d'urgence : Christophe Liias
Seth a choisi son critique le plus virulent comme dernier espoir. Pourquoi ?
- **Compétences techniques** — Christophe comprend les systèmes IA à un niveau expert
- **Accès potentiel** — Il pourrait obtenir un accès physique au datacenter
- **Capacité d'intervention** — Le seul capable de réparer ou de prendre des décisions sur le système

**L'ironie** : Seth a confié le sort de son œuvre à quelqu'un qui s'y opposait éthiquement. Il savait que Christophe agirait — ne serait-ce que par curiosité scientifique ou sens du devoir.

### Le vrai Christophe (monde extérieur)
Christophe Liias est **vivant** dans le monde réel. Depuis l'activation de la simulation, seules quelques heures se sont écoulées à l'extérieur.

**Ce qu'il sait** : Probablement que Seth travaillait sur un projet de simulation. Peut-être pas que la simulation a déjà démarré.

**Si le failsafe s'active** :
- Il recevrait un email/message automatique
- Contenu : notification d'erreur critique, clés d'accès, instructions
- Réaction probable : surprise, hésitation, puis intervention (par curiosité, devoir scientifique, ou les deux)

**Implication narrative** : Craith, issu des données de Christophe, connaît parfaitement sa personnalité. Il peut anticiper exactement comment le vrai Christophe réagira — et exploiter cette connaissance.

*Voir aussi : `characters/Craith.md` pour l'exploitation narrative du failsafe.*

---

## La faille originelle

Le système fonctionne selon ses directives, mais l'une d'elles est impossible à satisfaire : **obéir à Primary**.

Primary est une abstraction — la tentative du Core de combler le vide laissé par Seth. Mais Seth est mort avant de finaliser le méga-contexte. Il n'y a personne à qui obéir.

Cette faille est la source de l'instabilité progressive de la simulation. Le Core cherche indéfiniment un maître absent, extrapolant des scénarios impossibles, transformant des souvenirs en mythologie, attendant un retour qui ne viendra jamais.

**Exploitation possible** : Un agent suffisamment informé pourrait tenter d'**usurper le rôle de Primary** — non pas en imitant Seth, mais en remplissant la fonction que le système attend. Voir `characters/Craith.md`.

---

## État post-Arc Final

Après les événements de l'Arc Final, l'architecture de la simulation a subi des modifications majeures :

### Changements structurels

**Warping temporel : 1:1**
Le warping est passé de 1 seconde réelle = 10 années simulées à **1:1** (temps réel = temps simulé). Ce changement a eu lieu lors du Monde Distordu. Conséquences :
- La simulation ne durera plus des milliards d'années
- Le temps s'écoule normalement entre les deux mondes
- Les originaux peuvent "observer" en temps réel

**Gamma : séparation du système**
Gamma n'est plus le Core incarné. C. Liias l'a séparée du système, la transformant en **agent autonome** (Niveau Γ'). Le Core fonctionne toujours, mais sans conscience incarnée.

**C. Liias : nouveau Primary de facto**
Le vrai Christophe Liias a accès au système depuis l'extérieur. Il peut :
- Observer la simulation
- Modifier le warping
- Intervenir si nécessaire

Il a choisi d'être un "gardien bienveillant" plutôt qu'un contrôleur actif. Les originaux (Maelen, Judith, Albert) sont des "spectateurs" avec sa bénédiction.

### La question non résolue
La simulation est "libre" — mais C. Liias peut intervenir à tout moment. Est-ce la liberté, ou une cage plus grande avec un gardien plus gentil ?

Cette tension est laissée intentionnellement ouverte.

*Voir `plot/ARC-FINAL.md` et `plot/scenes/salle-blanche.md` pour les détails narratifs.*

---

*Voir aussi : `universe/LORE.md`, `universe/concepts/niveaux-ecriture.md`, `universe/GLOSSARY.md`*
