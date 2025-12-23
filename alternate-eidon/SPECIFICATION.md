# Timeliner Standard Specification

**Version:** 0.2.0-draft  
**Status:** Draft  
**Last Updated:** 2024-12-22

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Philosophy](#2-philosophy)
3. [Core Concepts](#3-core-concepts)
4. [File Structure](#4-file-structure)
5. [Entity Files](#5-entity-files)
6. [YAML Frontmatter](#6-yaml-frontmatter)
7. [Timelines & Universal Tick](#7-timelines--universal-tick)
8. [Sections](#8-sections)
9. [Cross-References](#9-cross-references)
10. [The Universe Entity](#10-the-universe-entity)
11. [Events](#11-events)
12. [Relationships](#12-relationships)
13. [Images](#13-images)
14. [Custom Attributes](#14-custom-attributes)
15. [Section Schemas](#15-section-schemas)
16. [Content Reference Directives](#16-content-reference-directives)
17. [Author Directives](#17-author-directives)
18. [Examples](#18-examples)

---

## 1. Introduction

The **Timeliner Standard** is an open standard for **time-based world building** using Markdown files. It enables authors, game designers, screenwriters, and other creators to document fictional universes where every concept evolves over time.

### 1.1 Goals

- **Human-readable**: All content is standard Markdown, editable with any text editor
- **Time-aware**: Every entity can change throughout the timeline
- **Tool-friendly**: Structured enough for powerful tooling (search, visualization, validation)
- **Flexible**: Supports arbitrary calendar systems and naming conventions
- **Version-controlled**: Works seamlessly with Git and other VCS

### 1.2 Spec Version Declaration

Universes SHOULD declare the specification version they follow:

```yaml
timeliner_version: "0.1.0"
```

---

## 2. Philosophy

### 2.1 Everything Evolves

In fiction, nothing is static. Characters grow, locations change, items are created and destroyed. The Timeliner Standard treats **change as the fundamental unit** of world building.

### 2.2 Entities, Not Documents

Each concept in your universe is an **entity** represented by a folder containing:
- One **base file** (the starting state)
- Zero or more **delta files** (changes over time)

### 2.3 Time is Universal

All timelines in a universe map to a single **Universal Tick (UT)** — an arbitrary integer that enables correlation across different calendar systems.

### 2.4 Markdown First

Content is written in standard Markdown. YAML frontmatter is used sparingly for metadata that cannot be expressed in prose.

---

## 3. Core Concepts

### 3.1 Entity

An **entity** is any concept in your fictional universe:
- Characters (people, creatures, AI)
- Locations (places, buildings, planets)
- Items (objects, artifacts, weapons)
- Events (battles, ceremonies, discoveries) — see [Section 11](#11-events)
- Factions (organizations, nations, species)
- Relationships (connections between entities) — see [Section 12](#12-relationships)
- Concepts (magic systems, technologies, laws)
- Custom types defined by the author

### 3.2 Entity Folder

Each entity is a **folder** containing Markdown files:

```
characters/jack/
├── _index.md          # Base file (starting state)
├── 001-birth.md       # Delta file
├── the-accident.md    # Delta file
└── redemption.md      # Delta file
```

### 3.3 Entity Type

Entity type is **inferred from the folder path**:
- `/universe/characters/jack/` → type: `character`
- `/universe/locations/old-tavern/` → type: `location`
- `/universe/items/excalibur/` → type: `item`
- `/universe/events/the-great-war/` → type: `event`
- `/universe/relationships/jack--sarah/` → type: `relationship`

### 3.4 Base File

The **base file** contains the entity's initial state — its properties at the moment it first exists or becomes relevant to the story.

### 3.5 Delta File

A **delta file** contains changes to the entity at a specific point in time. Only modified sections need to be included; unchanged sections are inherited from the previous state.

---

## 4. File Structure

### 4.1 Universe Root

```
universe/
├── _index.md                    # Universe entity (root)
├── meta/
│   ├── timelines/
│   │   ├── gregorian.yaml
│   │   └── great-war-era.yaml
│   └── schemas/                 # Optional: entity type schemas
│       ├── character.yaml
│       ├── location.yaml
│       └── relationship-types.yaml  # Relationship type definitions
├── characters/
│   ├── jack/
│   │   ├── _index.md
│   │   └── *.md
│   └── sarah/
│       └── ...
├── locations/
│   └── old-tavern/
│       └── ...
├── items/
│   └── excalibur/
│       └── ...
├── relationships/               # Relationship entities
│   ├── jack--sarah/
│   │   ├── _index.md
│   │   └── *.md
│   └── valdris-empire--imperial-palace/
│       └── ...
└── [custom-type]/
    └── ...
```

### 4.2 Base File Naming

The base file MUST be named using one of these conventions (in priority order):

1. `_index.md` (preferred)
2. `index.md` (fallback)

If both exist, `_index.md` takes precedence.

### 4.3 Delta File Naming

Delta filenames are **arbitrary**. Authors choose names that are meaningful to them:

```
# All valid delta filenames:
001.md
002-the-accident.md
year-47.md
the-day-everything-changed.md
childhood-memories.md
```

**Ordering is determined by YAML frontmatter**, not filenames.

### 4.4 File Extension

All entity files use the standard `.md` extension.

---

## 5. Entity Files

### 5.1 Base File Structure

```markdown
---
# YAML frontmatter (optional, for metadata)
name: "Jack Vals"
existence:
  start: "1995-06-09"
  end: unknown
---

# Introduction

Jack is a former soldier turned mercenary.

# Physical description

Jack is tall with broad shoulders and a weathered face.

## Hair

Short, dark brown, usually unkempt.

## Distinguishing features

A scar runs across his left eyebrow.

# Personality

Jack is reserved but fiercely loyal to those he trusts.

# Notable Connections

His most important relationships are with [[sarah]] (see [[jack--sarah]]) 
and his time at the [[old-tavern]].
```

> **Note:** Formal relationships between entities are defined in relationship 
> entities (see [Section 12](#12-relationships)). Inline wiki-links create 
> backlinks but are not the source of truth for relationships.

### 5.2 Delta File Structure

```markdown
---
timestamp: "Year 47"
---

# Physical description

## Distinguishing features

A scar runs across his left eyebrow. His left arm is now prosthetic.

# Personality

Jack has become bitter and withdrawn after the accident.
```

### 5.3 Inheritance Rules

When resolving an entity's state at a given timestamp:

1. Start with the base file
2. Apply delta files in chronological order (by Universal Tick)
3. For each delta:
   - Sections present in the delta **replace** the corresponding section entirely
   - Sections NOT present in the delta **remain unchanged**
   - Nested sections follow the same rules at their level

---

## 6. YAML Frontmatter

### 6.1 Base File Frontmatter

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `name` | No | string | Display name of the entity |
| `existence` | No | object | When the entity exists (see 6.3) |
| `timeline` | No | string | Default timeline for this entity's delta files |
| `tags` | No | array | Search tags |
| `timeliner_version` | No* | string | Spec version (*required for universe root) |

### 6.2 Delta File Frontmatter

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `timestamp` | Yes | string | When this change occurs |
| `timeline` | No | string | Timeline for this timestamp (inherits from base if omitted) |
| `summary` | No | string | Brief description of changes |
| `tags` | No | array | Additional search tags |

### 6.3 Existence Object

The `existence` field defines when an entity exists in the universe:

```yaml
existence:
  start: "1995-06-09"    # or "eternal" or "unknown"
  end: "2077-03-14"      # or "eternal" or "unknown"
```

**Special values:**
- `eternal` — The entity exists from/until the beginning/end of time
- `unknown` — The boundary is undefined or mysterious

**Examples:**

```yaml
# Mortal character
existence:
  start: "1995-06-09"
  end: "2077-03-14"

# Still alive (end unknown)
existence:
  start: "1995-06-09"
  end: unknown

# God that can be killed
existence:
  start: eternal
  end: "Year 847"

# Curse that lasts forever once cast
existence:
  start: "Year 100"
  end: eternal

# Fully eternal (primordial entity)
existence:
  start: eternal
  end: eternal
```

### 6.4 Timeline Inheritance

Timeline resolution follows this cascade:

1. **Delta file** `timeline` field (if specified)
2. **Base file** `timeline` field (if specified)
3. **Universe root** `default_timeline` field

---

## 7. Timelines & Universal Tick

### 7.1 Universal Tick (UT)

The **Universal Tick** is an arbitrary integer that provides a total ordering for all events across all timelines. Every timestamp in every timeline maps to a UT value.

This enables:
- Sorting events from different calendars
- Cross-timeline references
- Tool-based timeline visualization

### 7.2 Timeline Definition Files

Timelines are defined in `/universe/meta/timelines/`:

```yaml
# /universe/meta/timelines/gregorian.yaml
id: gregorian
name: "Gregorian Calendar"
description: "Standard Earth calendar"
display_format: "{year}-{month}-{day}"

tick_mapping:
  type: formula
  formula: "(year * 10000) + (month * 100) + day"
  
epoch:
  reference: "Year 1 AD"
  tick: 10101
```

```yaml
# /universe/meta/timelines/great-war-era.yaml
id: great-war-era
name: "Great War Era"
description: "Years counted from the end of the Great War"
display_format: "Year {year} after the Great War"

tick_mapping:
  type: formula
  formula: "year * 1000"

epoch:
  reference: "The Great War ended"
  tick: 50000000

# Optional: explicit mappings for special events
explicit_events:
  "The Long Night": 50023500
  "Before the War": -1
```

### 7.3 Tick Mapping Types

| Type | Use Case | Description |
|------|----------|-------------|
| `formula` | Regular calendars | Mathematical conversion to UT |
| `explicit` | Narrative events | Lookup table of named moments |
| `hybrid` | Mixed | Formula with explicit overrides |

### 7.4 Timeline File Schema

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `id` | Yes | string | Unique identifier |
| `name` | Yes | string | Display name |
| `description` | No | string | Explanation of the calendar |
| `display_format` | Yes | string | How timestamps are displayed |
| `tick_mapping` | Yes | object | How to convert to UT |
| `epoch` | No | object | Reference point |
| `explicit_events` | No | object | Named timestamps → UT mappings |

---

## 8. Sections

### 8.1 Section Identification

Sections are identified by their **heading text**. This is case-sensitive and must match exactly.

```markdown
# Physical description    ← Section identifier: "Physical description"

Content here.

## Hair                   ← Subsection identifier: "Hair"

Brown and curly.
```

### 8.2 Section Replacement

When a delta file includes a section, it **completely replaces** that section from the previous state.

**Base file:**
```markdown
# Physical description
Jack is tall.

## Hair
Brown.

## Eyes
Blue.
```

**Delta file:**
```markdown
# Physical description
## Hair
Grey now.
```

**Result:** The entire `# Physical description` section is replaced. The entity now only has the `## Hair` subsection under Physical description. `## Eyes` is gone.

### 8.3 Granular Subsection Updates

To update only a subsection while preserving siblings, include the parent section with all children you want to keep:

**Delta file (preserves Eyes):**
```markdown
# Physical description
## Hair
Grey now.

## Eyes
Blue.
```

### 8.4 Section Deletion

To indicate a section no longer exists, include it with **empty content**:

```markdown
# Left arm

```

This signals that the "Left arm" section has been removed (e.g., the character lost their arm).

### 8.5 Schema Sections

Entity type schemas MAY define section templates that authors can reference using the `@` prefix syntax. See [Section 15: Section Schemas](#15-section-schemas) for the complete specification.

**Quick example:**

```markdown
# @introduction

This references the "introduction" section from the schema.

# Custom Section

This is a free-form section (no @ prefix).
```

---

## 9. Cross-References

### 9.1 Basic Reference

Reference another entity using wiki-style links:

```markdown
Jack met [[sarah]] at the [[old-tavern]].
```

### 9.2 Reference with Display Text

```markdown
Jack met [[sarah|his future wife]] at the tavern.
```

### 9.3 Time-Specific Reference

Reference an entity at a specific point in time:

```markdown
# Using the current file's timeline
Jack remembered [[sarah#Year 42]] fondly.

# Using a specific timeline's timestamp
The records show [[sarah#1999-06-15]].

# Using Universal Tick (for precision/edge cases)
The exact moment: [[sarah#UT:50042000]].
```

### 9.4 Reference Resolution

1. `[[entity]]` — Links to the entity's base file
2. `[[entity#timestamp]]` — Links to the entity's state at that timestamp
3. `[[entity#UT:value]]` — Links to the entity's state at that Universal Tick

The timestamp is parsed according to the referencing file's timeline context.

---

## 10. The Universe Entity

### 10.1 Universe as Entity

The **universe itself** is an entity that can evolve over time. It is defined at the root:

```
universe/
├── _index.md           # Universe base file
├── age-of-magic.md     # Universe delta
├── the-cataclysm.md    # Universe delta
├── age-of-stars.md     # Universe delta
└── ...
```

### 10.2 Universe Base File

```markdown
---
timeliner_version: "0.1.0"
name: "The Chronicles of Eldoria"
default_timeline: eldoria-calendar
existence:
  start: eternal
  end: eternal
---

# Introduction

Eldoria is a world of magic and mystery.

# Fundamental Laws

Magic flows through all living things.

# Cosmology

Three moons orbit the world.
```

### 10.3 Universe Delta Files

```markdown
---
timestamp: "The Cataclysm"
summary: "Magic dies, technology rises"
---

# Fundamental Laws

Magic no longer exists. The old ways are forgotten.
Technology has taken its place.

# Cosmology

Only two moons remain. The third was shattered.
```

### 10.4 Universe Metadata

The universe root file contains configuration for the entire project:

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `timeliner_version` | Yes | string | Specification version |
| `name` | Yes | string | Universe name |
| `default_timeline` | No | string | Default timeline ID |
| `existence` | No | object | Universe lifespan |

---

## 11. Events

Events are **first-class entities** that represent significant occurrences in your universe. Unlike other entities that exist continuously over a time range, events are anchored to specific moments or periods.

### 11.1 Event vs. Delta

- A **delta** represents a change to an existing entity
- An **event** is a standalone entity that describes what happened

Events and deltas often work together: an event describes *what* happened, while deltas on other entities describe the *consequences*.

### 11.2 Event Structure

```
events/
├── the-great-war/
│   ├── _index.md           # Event overview
│   ├── opening-battle.md   # Sub-event or phase
│   └── armistice.md        # Sub-event or phase
├── the-sundering/
│   └── _index.md
└── coronation-of-kira/
    └── _index.md
```

### 11.3 Event Base File

```markdown
---
name: "The Great War"
timeline: imperial-calendar
event_type: war                    # Optional: battle, ceremony, discovery, etc.
timestamp:
  start: "Year 840"
  end: "Year 847"
tags: [war, empire, conflict]
---

# Introduction

The Great War was a seven-year civil conflict that tore the Empire apart.

# Cause

Duke Varren's rebellion against Empress [[kira-valdris]].

# Key Participants

- [[kira-valdris]] — Empress, defender of the throne
- [[duke-varren]] — Rebel leader
- [[circle-of-magi]] — Secretly supported the rebellion
- [[theron-blackwood]] — Battle-mage for the Empress

# Key Locations

- [[imperial-palace]] — Seat of imperial power
- [[ashenmoor-tower]] — Site of the final battle

# Timeline

- **Year 840** — Duke Varren declares independence
- **Year 842** — Kira crowned Empress after her father's death
- **Year 844** — Marcus Ashford assassinated
- **Year 845** — Open warfare begins
- **Year 847** — The Sundering ends the war

# Outcome

The war ended not with victory, but with [[the-sundering]] — a catastrophe that destroyed magic itself.

# Consequences

- Death of [[kira-valdris]]
- Collapse of the [[empire-of-valdris]]
- End of magic
- Rise of the [[new-valdris-republic]]
```

### 11.4 Event Timestamp

Events use a special timestamp format with `start` and `end`:

```yaml
# Point-in-time event (ceremony, discovery)
timestamp:
  start: "Year 842"
  end: "Year 842"      # Same as start for instantaneous events

# Duration event (war, reign, journey)
timestamp:
  start: "Year 840"
  end: "Year 847"

# Ongoing event (no known end)
timestamp:
  start: "Year 850"
  end: unknown
```

### 11.5 Event Deltas

Events can have deltas for phases or sub-events:

```markdown
---
timestamp: "Year 845"
summary: "The war escalates to open conflict"
---

# Introduction

The political maneuvering ended. Real warfare began.

# Key Battles

- The Siege of Thornhold
- The Battle of Red Fields
- The Burning of Ashford Manor
```

### 11.6 Referencing Events

Events are referenced like any other entity:

```markdown
Jack fought in [[the-great-war]].
The [[the-sundering|Sundering]] changed everything.
She was born during [[coronation-of-kira#Year 842]].
```

---

## 12. Relationships

Relationships are **first-class entities** that define connections between other entities. Each relationship is a standalone entity folder that can evolve over time, providing a single source of truth for how two entities relate to each other.

### 12.1 Philosophy

Relationships in the Timeliner Standard follow these principles:

- **Single source of truth**: Each relationship between two entities is defined in exactly one place
- **Bidirectional by default**: One relationship entity captures both perspectives
- **Asymmetry support**: Different entities can perceive the relationship differently
- **Time evolution**: Relationships change over time using the standard delta pattern
- **Schema-defined types**: Relationship types are defined by the author in schemas
- **Strength quantification**: Each bond can have a strength value (0.0 - 1.0)

### 12.2 Relationship Structure

Relationships live in the `/relationships/` folder:

```
relationships/
├── jack--sarah/
│   ├── _index.md           # Base relationship state
│   ├── 842-marriage.md     # Delta: they got married
│   └── 845-war-strain.md   # Delta: war strains the relationship
├── kira-valdris--theron-blackwood/
│   ├── _index.md
│   └── 847-death.md
└── valdris-empire--imperial-palace/
    └── _index.md           # Location is capital of faction
```

### 12.3 Folder Naming Convention

Relationship folders SHOULD be named using one of these conventions:

| Convention | Example | Use Case |
|------------|---------|----------|
| **Alphabetical IDs** | `jack--sarah/` | Default (jack < sarah alphabetically) |
| **Meaningful name** | `jack-and-sarah/` | When clarity is preferred |
| **Descriptive** | `valdris-capital/` | For non-character relationships |

The double-dash (`--`) separator clearly distinguishes relationship folders from regular entity names.

### 12.4 Relationship Base File

```markdown
---
name: "Jack & Sarah"
timeline: imperial-calendar

participants:
  a: "[[jack]]"
  b: "[[sarah]]"

existence:
  start: "Year 820"
  end: unknown

bonds:
  # Symmetric bond (same in both directions)
  - type: childhood-friend
    strength: 0.9

tags: [friendship, romance]
---

# Introduction

Jack and Sarah grew up together in the merchant district of the capital.

# History

They first met at age 5 when Sarah's family moved next door.

# Significant Moments

- **Year 820** — First meeting as children
- **Year 835** — Jack leaves for military service
```

### 12.5 Participants

Every relationship MUST define exactly two participants:

```yaml
participants:
  a: "[[jack]]"           # First participant
  b: "[[sarah]]"          # Second participant
```

The labels `a` and `b` are used to define directional bonds (see 12.7). The assignment is arbitrary but should be consistent within the relationship.

### 12.6 Bonds

Bonds define the actual relationship types between participants. A relationship can have multiple bonds.

#### Bond Structure

```yaml
bonds:
  - type: friend          # Required: relationship type ID
    strength: 0.8         # Optional: 0.0 to 1.0 (default: 1.0)
    # Directionality (one of the following):
    symmetric: true       # Same in both directions
    from: a               # Directed: A → B only
    from: b               # Directed: B → A only
```

#### Symmetric Bonds

Symmetric bonds apply equally in both directions:

```yaml
bonds:
  - type: spouse
    symmetric: true
    strength: 1.0
    
  - type: rival
    symmetric: true
    strength: 0.7
```

#### Directed Bonds

Directed bonds only apply in one direction:

```yaml
bonds:
  - type: mentor
    from: a              # Jack is Sarah's mentor
    strength: 0.9
    
  - type: student
    from: b              # Sarah is Jack's student
    strength: 0.9
```

#### Asymmetric Strength

When both participants have the same bond type but different intensities:

```yaml
bonds:
  - type: friend
    symmetric: true
    strength:
      a: 1.0             # Jack sees Sarah as his best friend
      b: 0.6             # Sarah sees Jack as a good friend
```

### 12.7 Relationship Type Schema

Relationship types are defined in `/meta/schemas/relationship-types.yaml`:

```yaml
# /meta/schemas/relationship-types.yaml
id: relationship-types
name: "Relationship Types"
description: "Defines available relationship types and their properties"

types:
  # === Personal Relationships ===
  spouse:
    label: "Spouse"
    description: "Married partners"
    default_symmetric: true
    inverse: null            # Same in both directions
    valid_between:
      - [character, character]
  
  parent:
    label: "Parent"
    description: "Biological or adoptive parent"
    default_symmetric: false
    inverse: child           # A is parent → B is child
    valid_between:
      - [character, character]
  
  child:
    label: "Child"
    description: "Biological or adoptive child"
    default_symmetric: false
    inverse: parent
    valid_between:
      - [character, character]
  
  friend:
    label: "Friend"
    description: "Friendship bond"
    default_symmetric: true
    valid_between:
      - [character, character]
  
  rival:
    label: "Rival"
    description: "Competitive relationship"
    default_symmetric: true
    valid_between:
      - [character, character]
      - [faction, faction]
  
  enemy:
    label: "Enemy"
    description: "Hostile relationship"
    default_symmetric: true
    valid_between:
      - [character, character]
      - [faction, faction]
  
  mentor:
    label: "Mentor"
    description: "Teacher or guide"
    default_symmetric: false
    inverse: student
    valid_between:
      - [character, character]
  
  student:
    label: "Student"
    description: "Learner or protégé"
    default_symmetric: false
    inverse: mentor
    valid_between:
      - [character, character]
  
  lover:
    label: "Lover"
    description: "Romantic relationship"
    default_symmetric: true
    valid_between:
      - [character, character]
  
  # === Professional Relationships ===
  employer:
    label: "Employer"
    default_symmetric: false
    inverse: employee
    valid_between:
      - [character, character]
      - [faction, character]
  
  employee:
    label: "Employee"
    default_symmetric: false
    inverse: employer
    valid_between:
      - [character, character]
      - [character, faction]
  
  ally:
    label: "Ally"
    description: "Allied in purpose"
    default_symmetric: true
    valid_between:
      - [character, character]
      - [faction, faction]
      - [character, faction]
  
  # === Spatial Relationships ===
  capital:
    label: "Capital of"
    description: "Administrative center"
    default_symmetric: false
    inverse: has-capital
    valid_between:
      - [location, faction]
  
  has-capital:
    label: "Has capital"
    default_symmetric: false
    inverse: capital
    valid_between:
      - [faction, location]
  
  located-in:
    label: "Located in"
    description: "Physical containment"
    default_symmetric: false
    inverse: contains
    valid_between:
      - [location, location]
      - [item, location]
  
  contains:
    label: "Contains"
    default_symmetric: false
    inverse: located-in
    valid_between:
      - [location, location]
      - [location, item]
  
  # === Membership Relationships ===
  member-of:
    label: "Member of"
    default_symmetric: false
    inverse: has-member
    valid_between:
      - [character, faction]
  
  has-member:
    label: "Has member"
    default_symmetric: false
    inverse: member-of
    valid_between:
      - [faction, character]
  
  leader-of:
    label: "Leader of"
    default_symmetric: false
    inverse: led-by
    valid_between:
      - [character, faction]
  
  led-by:
    label: "Led by"
    default_symmetric: false
    inverse: leader-of
    valid_between:
      - [faction, character]
  
  # === Ownership ===
  owns:
    label: "Owns"
    default_symmetric: false
    inverse: owned-by
    valid_between:
      - [character, item]
      - [character, location]
      - [faction, location]
  
  owned-by:
    label: "Owned by"
    default_symmetric: false
    inverse: owns
    valid_between:
      - [item, character]
      - [location, character]
      - [location, faction]
```

### 12.8 Relationship Type Schema Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `id` | Yes | string | Schema identifier (must be `relationship-types`) |
| `name` | Yes | string | Human-readable name |
| `description` | No | string | Schema description |
| `types` | Yes | object | Map of type ID → type definition |

**Per-type fields:**

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `label` | Yes | string | Display name |
| `description` | No | string | Tooltip/help text |
| `default_symmetric` | No | boolean | Default symmetry (default: `true`) |
| `inverse` | No | string | ID of the inverse relationship type |
| `valid_between` | No | array | Valid entity type pairs `[[typeA, typeB], ...]` |

### 12.9 Relationship Delta Files

Relationships evolve over time using delta files:

**Delta file (`842-marriage.md`):**
```yaml
---
timestamp: "Year 842"
summary: "Jack and Sarah get married"

bonds:
  - type: spouse
    symmetric: true
    strength: 1.0
    
  - type: friend
    symmetric: true
    strength:
      a: 1.0
      b: 0.9
---

# Introduction

@prev

They married in a small ceremony during the siege of Thornhold.

# Significant Moments

@prev

- **Year 842** — Married during wartime
```

**Delta file (`845-war-strain.md`):**
```yaml
---
timestamp: "Year 845"
summary: "War strains their relationship"

bonds:
  - type: spouse
    symmetric: true
    strength: 0.6          # Strained but intact
    
  - type: protector
    from: a                # Jack protects Sarah
    strength: 0.9
    
  - type: resentment
    from: b                # Sarah resents Jack's absences
    strength: 0.4
---

# Introduction

@prev

The prolonged war has created distance between them.
```

### 12.10 Bond Inheritance Rules

| Scenario | Behavior |
|----------|----------|
| Bond type present in delta | **Replaces** that bond entirely |
| Bond type absent in delta | **Inherits** from previous state |
| Bond with `strength: null` | **Removes** that bond |
| Empty `bonds: []` array | **Removes all** bonds |

**Example: Removing a bond**
```yaml
---
timestamp: "Year 850"
bonds:
  - type: spouse
    symmetric: true
    strength: null         # Divorced — bond removed
    
  - type: friend
    symmetric: true
    strength: 0.5          # Remain friends
---
```

### 12.11 Relationship Frontmatter Reference

**Base file:**

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `name` | No | string | Display name for the relationship |
| `participants` | Yes | object | The two entities in the relationship |
| `participants.a` | Yes | string | Reference to first entity |
| `participants.b` | Yes | string | Reference to second entity |
| `bonds` | No | array | List of bond definitions |
| `existence` | No | object | When the relationship exists |
| `timeline` | No | string | Default timeline for delta files |
| `tags` | No | array | Search tags |

**Delta file:**

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `timestamp` | Yes | string | When this change occurs |
| `summary` | No | string | Brief description of changes |
| `bonds` | No | array | Bond updates (replaces matching types) |
| `timeline` | No | string | Timeline for this timestamp |

### 12.12 Querying Relationships

Tooling SHOULD provide methods to query relationships:

```
# Get all relationships for an entity
timeliner relationships jack

# Get specific relationship types
timeliner relationships jack --type=spouse

# Get relationships at a specific time
timeliner relationships jack --at="Year 845"

# Get relationship between two specific entities
timeliner relationship jack sarah

# Get all enemies of a faction
timeliner relationships valdris-empire --type=enemy
```

### 12.13 Relationship Graph

Relationship entities enable powerful graph visualizations:

- **Social networks**: Show all character relationships
- **Political maps**: Show faction alliances and rivalries
- **Timeline views**: Show how relationships evolve
- **Filtered views**: Show only specific relationship types

Tooling SHOULD compute relationship graphs by:
1. Scanning all entities in `/relationships/`
2. Building edges based on `participants` and `bonds`
3. Applying time filters to show state at specific timestamps

### 12.14 Inverse Relationships

When a relationship type has an `inverse` defined, tooling SHOULD automatically infer the inverse:

**Relationship file:**
```yaml
participants:
  a: "[[marcus-ashford]]"
  b: "[[kira-valdris]]"

bonds:
  - type: parent
    from: a              # Marcus is Kira's parent
    strength: 1.0
```

**Tooling inference:**
- Marcus → Kira: `parent` (strength: 1.0)
- Kira → Marcus: `child` (strength: 1.0) — automatically inferred from inverse

### 12.15 Cross-Entity References (Backlinks)

Entity files MAY include relationship references in their content using standard wiki-links. These create **backlinks** but are NOT the source of truth for the relationship.

```markdown
# In characters/jack/_index.md

# Relationships

See my relationship with [[sarah]] in [[jack--sarah]].
```

Tooling SHOULD:
- Display relationships from `/relationships/` folder in entity views
- Show computed backlinks separately from formal relationships
- Allow navigation from entity to its relationship entities

### 12.16 Complete Relationship Example

**File:** `/relationships/kira-valdris--theron-blackwood/_index.md`
```yaml
---
name: "Kira & Theron"
timeline: imperial-calendar

participants:
  a: "[[kira-valdris]]"
  b: "[[theron-blackwood]]"

existence:
  start: "Year 840"
  end: "Year 847"

bonds:
  - type: ally
    symmetric: true
    strength: 0.7
    
  - type: employer
    from: a
    strength: 1.0

tags: [romance, politics, tragedy]
---

# Introduction

The relationship between Empress Kira and her court mage Theron began as a political alliance but grew into something deeper.

# History

Theron was assigned to the imperial court in Year 840, initially as a spy for the [[circle-of-magi]]. Over time, his loyalty shifted entirely to Kira.

# Significant Moments

- **Year 840** — Theron arrives at court
- **Year 842** — Becomes Kira's primary advisor after her coronation
- **Year 844** — Secret romantic relationship begins
- **Year 847** — Both die together at Ashenmoor Tower
```

**File:** `/relationships/kira-valdris--theron-blackwood/844-romance.md`
```yaml
---
timestamp: "Year 844"
summary: "Romance begins in secret"

bonds:
  - type: ally
    symmetric: true
    strength: 0.9
    
  - type: lover
    symmetric: true
    strength:
      a: 0.8
      b: 1.0            # Theron loves her more deeply
    
  - type: employer
    from: a
    strength: 1.0
    
  - type: protector
    from: b
    strength: 1.0
---

# Introduction

@prev

Their alliance has deepened into a secret romance, hidden from the court.
```

**File:** `/relationships/kira-valdris--theron-blackwood/847-death.md`
```yaml
---
timestamp: "Year 847"
summary: "Final moments together"

bonds:
  - type: lover
    symmetric: true
    strength: 1.0         # United in death
    
  - type: ally
    symmetric: true
    strength: 1.0
---

# Introduction

@prev

In their final moments at Ashenmoor Tower, they faced the Sundering together.
```

---

## 13. Images

Images add visual richness to entities. The Timeliner Standard supports both entity-local images and shared assets, with the ability for an entity's main image to change over time.

### 13.1 Image Storage Locations

Images can be stored in two locations:

| Location | Path | Purpose |
|----------|------|---------|
| **Entity-local** | `entity/_img/` or `entity/img/` | Images specific to one entity |
| **Shared assets** | `universe/assets/` | Reusable images across entities |

**Resolution order for local folders:**
1. `_img/` (preferred, sorts first in filesystem)
2. `img/` (fallback if `_img/` doesn't exist)

### 13.2 Folder Structure

```
universe/
├── _index.md
├── assets/                          # Shared assets library
│   ├── portraits/
│   │   ├── kira-young.jpg
│   │   └── kira-empress.jpg
│   ├── locations/
│   │   └── imperial-palace.jpg
│   ├── symbols/
│   │   └── valdris-crest.png
│   └── maps/
│       └── empire-year-840.svg
├── characters/
│   └── kira-valdris/
│       ├── _index.md
│       ├── 842-coronation.md
│       └── _img/                    # Entity-local images
│           ├── personal-diary-sketch.jpg
│           └── death-scene.png
├── locations/
│   └── imperial-palace/
│       ├── _index.md
│       └── img/                     # Also valid (fallback)
│           └── throne-room.jpg
```

### 13.3 Main Image in Frontmatter

Each entity can have a **main image** that represents it visually (e.g., a character portrait, location photograph, item illustration).

#### Simple String Form

```yaml
---
name: "Kira Valdris III"
image: portrait-young.jpg
---
```

#### Object Form with Caption

```yaml
---
name: "Kira Valdris III"
image:
  src: portrait-young.jpg
  caption: "Portrait commissioned by her father, Year 835"
---
```

### 13.4 Image Path Resolution

| Syntax | Resolves To |
|--------|-------------|
| `image.jpg` | `entity/_img/image.jpg` or `entity/img/image.jpg` |
| `./image.jpg` | Same as above (explicit relative) |
| `@assets/path/image.jpg` | `universe/assets/path/image.jpg` |
| `https://...` | External URL (used as-is) |
| `http://...` | External URL (used as-is) |

**Examples:**

```yaml
# Local image (in entity's _img or img folder)
image: portrait.jpg

# Shared asset
image: "@assets/portraits/kira-official.jpg"

# External URL
image: "https://example.com/images/kira-portrait.jpg"

# With caption
image:
  src: "@assets/portraits/kira-official.jpg"
  caption: "Official imperial portrait, Year 842"
```

### 13.5 Time-Varying Main Image

An entity's main image can change over time through delta files. Each delta file can override the `image` field:

**Base file (`_index.md`):**
```yaml
---
name: "Kira Valdris III"
image:
  src: "@assets/portraits/kira-young.jpg"
  caption: "As a young princess"
---
```

**Delta file (`842-coronation.md`):**
```yaml
---
timestamp: "Year 842"
summary: "Coronation as Empress"
image:
  src: "@assets/portraits/kira-empress.jpg"
  caption: "Imperial coronation portrait"
---
```

**Delta file (`847-death.md`):**
```yaml
---
timestamp: "Year 847"
summary: "The Sundering"
image:
  src: death-scene.png
  caption: "Final moments at Ashenmoor Tower"
---
```

When resolving an entity's state at a given timestamp, the main image is determined by the most recent delta that includes an `image` field.

### 13.6 Inline Images in Markdown

Standard Markdown image syntax is supported anywhere in entity content, using the same path resolution rules:

```markdown
# The Coronation

![Kira receiving the crown](@assets/portraits/kira-empress.jpg)

The ceremony took place in the [[imperial-palace]].

![A sketch from her personal diary](personal-diary-sketch.jpg)

The official crest of House Valdris:
![Valdris Crest](@assets/symbols/valdris-crest.png)
```

### 13.7 Image Schema

**Simple form:**
```yaml
image: "path/to/image.jpg"
```

**Object form:**
```yaml
image:
  src: "path/to/image.jpg"    # Required: image path
  caption: "Description"       # Optional: image caption/description
```

### 13.8 YAML Frontmatter Update

The `image` field is added to both base and delta file frontmatter:

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `image` | No | string \| object | Main image for the entity |

When `image` is an object:

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `src` | Yes | string | Path to the image file |
| `caption` | No | string | Image caption or description |

---

## 14. Custom Attributes

Custom attributes allow authors to define structured metadata for entities beyond the built-in fields. Attributes are ideal for properties that should be displayed prominently (e.g., in an Entity Viewer) and that may evolve over time.

### 14.1 Overview

Attributes are key-value pairs stored in YAML frontmatter. They complement Markdown sections:

| Use Case | Recommended Approach |
|----------|---------------------|
| Short, structured data (race, blood type, title) | **Attributes** |
| Long-form prose (personality, background) | **Markdown sections** |
| Lists of related entities | **Relationships section** |

### 14.2 Basic Syntax

Attributes are defined in the `attributes` field of the YAML frontmatter:

```yaml
---
name: "Kira Valdris III"
timeline: imperial-calendar
existence:
  start: "Year 819"
  end: "Year 847"
tags: [protagonist, empress]

attributes:
  race: Human
  blood_type: "A+"
  faction: "[[empire-of-valdris]]"
  magical_affinity: Lightning
  title: Princess
---
```

### 14.3 Attribute Values

Attribute values can be:

| Type | Example | Description |
|------|---------|-------------|
| String | `race: Human` | Plain text |
| Number | `age: 28` | Numeric value |
| Boolean | `is_alive: true` | True/false |
| Reference | `faction: "[[empire-of-valdris]]"` | Link to another entity |
| Array | `titles: [Princess, Archmage]` | Multiple values |

**Note:** Nested objects are not supported. Keep attributes flat.

```yaml
# ✅ Valid
attributes:
  height: "5'9\""
  weight: "140 lbs"
  eye_color: Violet

# ❌ Invalid (no nesting)
attributes:
  physical:
    height: "5'9\""
    weight: "140 lbs"
```

### 14.4 Time Evolution

Attributes evolve over time through delta files, following the same inheritance rules as other frontmatter fields.

**Base file (`_index.md`):**
```yaml
---
name: "Kira Valdris III"
attributes:
  title: Princess
  faction: "[[empire-of-valdris]]"
  status: Healthy
---
```

**Delta file (`842-coronation.md`):**
```yaml
---
timestamp: "Year 842"
attributes:
  title: Empress of Valdris
---
```

**Resolved state at Year 842:**
- `title`: "Empress of Valdris" (updated)
- `faction`: "[[empire-of-valdris]]" (inherited)
- `status`: "Healthy" (inherited)

### 14.5 Attribute Inheritance Rules

| Delta contains... | Behavior |
|-------------------|----------|
| Attribute with value | **Replaces** that attribute |
| Attribute with `null` | **Removes** that attribute |
| Attribute absent | **Inherits** from previous state |

**Example: Removing an attribute**
```yaml
---
timestamp: "Year 847"
attributes:
  faction: null      # No longer affiliated (empire collapsed)
  status: Deceased
---
```

### 14.6 Attribute Schemas (Optional)

For richer tooling support, authors can define attribute schemas per entity type in `/meta/schemas/`. Schemas are optional but provide:

- Display labels for attribute keys
- Type validation
- Suggested values (autocomplete)
- Display ordering
- Grouping for UI

#### 14.6.1 Schema File Structure

```yaml
# /meta/schemas/character.yaml
id: character
name: "Character"
description: "A person, creature, or AI in the universe"

attributes:
  race:
    label: "Race"
    type: string
    description: "Species or race of the character"
    order: 1
    values: [Human, Elf, Dwarf, Orc, Other]  # Suggested values
  
  blood_type:
    label: "Blood Type"
    type: string
    order: 2
    values: [A+, A-, B+, B-, AB+, AB-, O+, O-]
  
  faction:
    label: "Faction"
    type: reference
    description: "Primary allegiance or affiliation"
    order: 3
  
  title:
    label: "Title"
    type: string
    order: 4
  
  magical_affinity:
    label: "Magical Affinity"
    type: string
    description: "Primary magical element or school"
    group: "Abilities"
    order: 10
```

#### 14.6.2 Schema Field Reference

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `id` | Yes | string | Entity type identifier (matches folder name) |
| `name` | Yes | string | Human-readable type name |
| `description` | No | string | Description of this entity type |
| `attributes` | No | object | Attribute definitions |

**Per-attribute fields:**

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `label` | No | string | Display name (defaults to humanized key) |
| `type` | No | string | Value type: `string`, `number`, `boolean`, `reference`, `array` |
| `description` | No | string | Tooltip/help text |
| `order` | No | number | Display order (lower = first) |
| `group` | No | string | Group name for UI organization |
| `values` | No | array | Suggested/allowed values |

#### 14.6.3 Display Name Resolution

When displaying attributes, tooling resolves display names in this order:

1. **Schema label** — If the attribute key matches a schema definition, use its `label`
2. **Humanized key** — Otherwise, convert the key to title case (e.g., `blood_type` → "Blood Type")

This allows:
- Schemas to provide polished labels for common attributes
- Ad-hoc attributes to work without schema changes

### 14.7 Unique Entity Attributes

Entities can have attributes not defined in the schema. These "unique attributes" work identically to schema-defined ones:

```yaml
---
name: "Theron Blackwood"
attributes:
  race: Human
  faction: "[[circle-of-magi]]"
  demonic_pact: "Soul-bound to Azaroth"  # Unique to this character
---
```

The `demonic_pact` attribute will display as "Demonic Pact" (humanized) since it's not in the schema.

### 14.8 YAML Frontmatter Update

The `attributes` field is added to both base and delta file frontmatter:

**Base file:**

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `attributes` | No | object | Custom attributes as key-value pairs |

**Delta file:**

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `attributes` | No | object | Attribute updates (set value or `null` to remove) |

### 14.9 Complete Example

**Schema (`/meta/schemas/character.yaml`):**
```yaml
id: character
name: "Character"

attributes:
  race:
    label: "Race"
    type: string
    order: 1
  title:
    label: "Title"
    type: string
    order: 2
  faction:
    label: "Faction"
    type: reference
    order: 3
```

**Base file (`/characters/kira-valdris/_index.md`):**
```yaml
---
name: "Kira Valdris III"
timeline: imperial-calendar
existence:
  start: "Year 819"
  end: "Year 847"

attributes:
  race: Human
  title: Princess
  faction: "[[empire-of-valdris]]"
  blood_type: "A+"
---

# Introduction

Kira Valdris III is the heir to the throne...
```

**Delta (`/characters/kira-valdris/842-coronation.md`):**
```yaml
---
timestamp: "Year 842"
summary: "Crowned Empress"

attributes:
  title: Empress of Valdris
---

# Introduction

Kira Valdris III now rules the empire...
```

**Delta (`/characters/kira-valdris/847-death.md`):**
```yaml
---
timestamp: "Year 847"
summary: "Death in the Sundering"

attributes:
  faction: null
  status: Deceased
---

# Introduction

Kira Valdris III died at the epicenter of the Sundering...
```

**Resolved state at Year 847:**

| Attribute | Display Label | Value |
|-----------|---------------|-------|
| race | Race | Human |
| title | Title | Empress of Valdris |
| faction | Faction | *(removed)* |
| blood_type | Blood Type | A+ |
| status | Status | Deceased |

---

## 15. Section Schemas

Section schemas allow authors to define reusable section templates for entity types. Using the `@` prefix syntax, authors reference schema-defined sections that are rendered with consistent labels across all entities of the same type.

### 15.1 Overview

Sections complement attributes:

| Use Case | Recommended Approach |
|----------|---------------------|
| Short, structured data (race, blood type, title) | **Attributes** (YAML frontmatter) |
| Long-form prose (personality, background) | **Sections** (Markdown) |
| Consistent section structure across entities | **Schema Sections** (with `@` prefix) |

### 15.2 The `@` Prefix Syntax

To reference a schema-defined section, use the `@` prefix followed by the section ID:

```markdown
# @introduction

Content for the introduction section...

## @full-name

Kira Valdris III

# Custom Section

Free-form section without schema reference.
```

**Rendering behavior:**

| Raw Markdown | Rendered Display |
|--------------|------------------|
| `# @introduction` | **Introduction** (H1) |
| `## @full-name` | **Full Name** (H2) |
| `# Custom Section` | **Custom Section** (H1) |

The `@` prefix indicates a schema reference. The section ID is looked up in the entity type's schema, and the `label` is displayed instead of the ID.

### 15.3 Section ID Format

Section IDs must follow these rules:

- Start with a lowercase letter
- Contain only lowercase letters, numbers, and hyphens
- Pattern: `[a-z][a-z0-9-]*`

**Valid IDs:**
```
introduction
full-name
physical-description
abilities-combat
year-847-aftermath
```

**Invalid IDs:**
```
Introduction        # Uppercase not allowed
full_name           # Underscore not allowed
123-start           # Must start with letter
-invalid            # Must start with letter
```

### 15.4 Syntax Rules

The `@` prefix must immediately follow the space after the heading markers:

```markdown
# @identity              ✓ Valid
## @physical-description ✓ Valid
### @hair                ✓ Valid

#@identity               ✗ Invalid (no space after #)
# @ identity             ✗ Invalid (space after @)
# @Identity              ✗ Invalid (uppercase)
# @identity - Details    ✗ Invalid (extra text after ID)
```

### 15.5 Author-Controlled Heading Level

The author controls the heading level using standard Markdown `#` syntax. The schema defines *what* sections exist, not *how* they are structured:

```markdown
# @identity

## @full-name
Kira Valdris III

## @titles
Princess, Empress of Valdris

## @aliases
The Lightning Empress, The Reformer

# @physical-description

## @general
A striking woman in her mid-twenties...

## @hair
Long, raven-black hair...
```

This allows flexibility — the same section ID can be used at different levels in different entities if needed.

### 15.6 Schema Definition

Sections are defined in entity type schemas alongside attributes:

```yaml
# /meta/schemas/character.yaml
id: character
name: "Character"
description: "A person, creature, or sentient being"

attributes:
  race:
    label: "Race"
    type: string
    order: 1
  # ... other attributes ...

sections:
  introduction:
    label: "Introduction"
    description: "Brief overview of the character"
    order: 1
    
  identity:
    label: "Identity"
    description: "Names, titles, and identifying information"
    order: 10
    
  full-name:
    label: "Full Name"
    description: "Complete legal or formal name"
    order: 11
    
  titles:
    label: "Titles"
    description: "Ranks, positions, honorifics"
    order: 12
    
  aliases:
    label: "Aliases"
    description: "Nicknames, pseudonyms, epithets"
    order: 13
    
  physical-description:
    label: "Physical description"
    description: "Physical appearance and characteristics"
    order: 20
    
  general:
    label: "General"
    description: "Overall appearance"
    order: 21
    
  hair:
    label: "Hair"
    order: 22
    
  eyes:
    label: "Eyes"
    order: 23
    
  distinguishing-features:
    label: "Distinguishing features"
    description: "Scars, birthmarks, unique traits"
    order: 24
    
  personality:
    label: "Personality"
    description: "Character traits and temperament"
    order: 30
    
  abilities:
    label: "Abilities"
    description: "Skills, powers, and capabilities"
    order: 40
    
  magic:
    label: "Magic"
    order: 41
    
  combat:
    label: "Combat"
    order: 42
    
  background:
    label: "Background"
    description: "History and origin story"
    order: 50
    
  relationships:
    label: "Relationships"
    description: "Connections to other entities"
    order: 60
    
  goals:
    label: "Goals"
    description: "Motivations and objectives"
    order: 70
```

### 15.7 Section Schema Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `label` | Yes | string | Display name shown in rendered output |
| `description` | No | string | Help text / tooltip for tooling |
| `order` | No | number | Display order hint (lower = first) |

### 15.8 Mixed Schema and Custom Sections

Documents can freely mix schema sections and custom sections:

```markdown
---
name: "Kira Valdris III"
---

# @introduction

Kira Valdris III is the young Empress...

# @physical-description

## @hair
Long, raven-black hair...

## @eyes
Violet eyes...

# Secret Plans

This is a **custom section** — not prefixed with @, 
so it displays exactly as written.

# @relationships

- [[marcus-ashford]] — Uncle and advisor
- [[theron-blackwood]] — Court mage

# Notes for Future Chapters

Another custom section for author notes.
```

**Rendering:**
- Schema sections (`# @introduction`, `# @physical-description`, etc.) display their schema labels
- Custom sections (`# Secret Plans`, `# Notes for Future Chapters`) display as-is

### 15.9 Unknown Section IDs

If a section ID is not found in the schema, tooling SHOULD report an error or warning:

```markdown
# @introducton
```

```
⚠ Error: Unknown section ID "introducton" in character schema.
  Did you mean "introduction"?
```

This catches typos and ensures all `@`-prefixed sections are valid schema references.

### 15.10 Delta Files with Schema Sections

Schema sections work identically in delta files. The `@` prefix is used the same way:

```markdown
---
timestamp: "Year 842"
summary: "Coronation as Empress"
---

# @introduction

Kira Valdris III now rules as Empress of Valdris...

# @personality

Kira has grown more confident in her role as ruler...
```

The `# @personality` section in the delta **replaces** the `# @personality` section from the base file (or previous deltas), following standard section inheritance rules.

### 15.11 Subsection Updates

To update a specific subsection while preserving siblings, include the parent section with all children you want to keep:

**Base file:**
```markdown
# @physical-description

## @hair
Long, raven-black hair...

## @eyes
Violet eyes...

## @distinguishing-features
A small birthmark on her left wrist.
```

**Delta (updates only hair, preserves others):**
```markdown
---
timestamp: "Year 847"
---

# @physical-description

## @hair
Now streaked with grey from the stress of war.

## @eyes
Violet eyes...

## @distinguishing-features
A small birthmark on her left wrist. New scars from battle.
```

### 15.12 Section Ordering

The `order` field in the schema provides a **hint** for tooling (e.g., autocomplete suggestions, outline views). However, the actual document order is determined by the author's Markdown file.

Tooling MAY:
- Sort autocomplete suggestions by `order`
- Display an outline view sorted by `order`
- Warn if document order differs significantly from schema order

Tooling SHOULD NOT:
- Automatically reorder sections in the source file
- Require sections to appear in schema order

### 15.13 Complete Example

**Schema (`/meta/schemas/character.yaml`):**
```yaml
id: character
name: "Character"

attributes:
  race:
    label: "Race"
    type: string
  title:
    label: "Title"
    type: string

sections:
  introduction:
    label: "Introduction"
    order: 1
  physical-description:
    label: "Physical description"
    order: 10
  hair:
    label: "Hair"
    order: 11
  eyes:
    label: "Eyes"
    order: 12
  personality:
    label: "Personality"
    order: 20
  relationships:
    label: "Relationships"
    order: 30
```

**Entity file (`/characters/kira-valdris/_index.md`):**
```markdown
---
name: "Kira Valdris III"
timeline: imperial-calendar
existence:
  start: "Year 819"
  end: "Year 847"

attributes:
  race: Human
  title: Princess
---

# @introduction

Kira Valdris III is the young heir to the throne of the Valdris Empire.
A powerful mage and idealistic reformer, she dreams of a more just world.

# @physical-description

## @hair

Long, raven-black hair worn in elaborate braids woven with silver threads —
a traditional Valdris royal style.

## @eyes

Violet eyes — a mark of strong magical lineage in the Valdris bloodline.

# @personality

Kira is idealistic but not naive. She genuinely believes in justice and
equality, though she understands the political realities that constrain her.

# Secret Fears

She secretly fears she is not worthy of the crown.

# @relationships

- [[marcus-ashford]] `uncle` — Lord Commander of the Imperial Guard
- [[theron-blackwood]] `lover` — Court mage and secret love interest
- [[duke-varren]] `enemy` — Powerful noble who opposes her reforms
```

**Rendered display:**

> ## Introduction
> 
> Kira Valdris III is the young heir to the throne of the Valdris Empire.
> A powerful mage and idealistic reformer, she dreams of a more just world.
> 
> ## Physical description
> 
> ### Hair
> 
> Long, raven-black hair worn in elaborate braids woven with silver threads —
> a traditional Valdris royal style.
> 
> ### Eyes
> 
> Violet eyes — a mark of strong magical lineage in the Valdris bloodline.
> 
> ## Personality
> 
> Kira is idealistic but not naive...
> 
> ## Secret Fears
> 
> She secretly fears she is not worthy of the crown.
> 
> ## Relationships
> 
> - Marcus Ashford (uncle) — Lord Commander of the Imperial Guard
> - ...

---

## 16. Content Reference Directives

Content reference directives allow delta files to **build upon** previous content rather than replacing it entirely. This reduces duplication and makes it easier to add incremental changes to existing sections.

### 16.1 Overview

By default, sections in delta files **completely replace** the corresponding section from the previous state. Content reference directives provide a way to include previous content within the new section.

| Problem | Solution |
|---------|----------|
| Must copy all previous content to add a paragraph | Use `@prev` to include previous content |
| Duplicated content across delta files | Reference previous state dynamically |
| Maintenance burden when updating shared text | Single source of truth |

### 16.2 The `@prev` Directive

The `@prev` directive inserts the previous content of the current section at the directive's location.

**Syntax:**
```markdown
@prev
```

The directive must appear on its own line within a section.

### 16.3 Basic Usage

**Base file (`_index.md`):**
```markdown
# Physical description

## Hair

Long, raven-black hair worn in elaborate braids woven with silver threads — a traditional Valdris royal style.
```

**Delta file (`845-civil-war.md`):**
```markdown
---
timestamp: "Year 845"
---

# Physical description

## Hair

@prev

Cut shorter for practicality. The silver threads are gone.
```

**Resolved state at Year 845:**
```markdown
# Physical description

## Hair

Long, raven-black hair worn in elaborate braids woven with silver threads — a traditional Valdris royal style.

Cut shorter for practicality. The silver threads are gone.
```

### 16.4 Placement Flexibility

The `@prev` directive can appear anywhere within a section, allowing authors to prepend, append, or insert content around the previous state:

**Prepending content:**
```markdown
# Personality

*After the war, everything changed.*

@prev
```

**Appending content:**
```markdown
# Personality

@prev

She has also become more ruthless.
```

**Surrounding content:**
```markdown
# Personality

*How she used to be:*

@prev

*How she is now:*

Cold, calculating, and merciless.
```

### 16.5 Multiple `@prev` Directives

Multiple `@prev` directives in the same section are allowed. Each resolves independently to the same previous content:

```markdown
# Battle Record

## Summary

@prev

## Detailed Analysis

The above summary (@prev) shows a pattern of aggressive tactics.
```

**Note:** The second `@prev` in inline context is **not valid** — `@prev` must be on its own line. For inline references, see [Section 16.8](#168-future-extensions).

### 16.6 Behavior Rules

| Scenario | Behavior |
|----------|----------|
| `@prev` in base file | **Error** — no previous state exists |
| `@prev` for section that didn't exist previously | **Empty** — renders as blank (no content inserted) |
| `@prev` outside any section | **Error** — must be inside a section |
| Whitespace around `@prev` | **Trimmed** — `  @prev  ` is valid |
| `@prev` with other text on same line | **Invalid** — must be alone on the line |
| Nested resolution (previous content contains `@prev`) | **Not recursive** — directives in resolved content are not processed |

### 16.7 Chained Deltas

When multiple deltas use `@prev`, content accumulates naturally:

**Base (`_index.md`):**
```markdown
# History

Born in Year 819.
```

**Delta 1 (`842-coronation.md`):**
```markdown
---
timestamp: "Year 842"
---

# History

@prev

Crowned Empress in Year 842.
```

**Delta 2 (`845-war.md`):**
```markdown
---
timestamp: "Year 845"
---

# History

@prev

Led armies against Duke Varren's rebellion.
```

**Resolved at Year 845:**
```markdown
# History

Born in Year 819.

Crowned Empress in Year 842.

Led armies against Duke Varren's rebellion.
```

### 16.8 Syntax Specification

The `@prev` directive follows these syntax rules:

```
directive     = "@prev"
directive-line = [ whitespace ] directive [ whitespace ] newline
```

**Valid:**
```markdown
@prev
  @prev
@prev  
```

**Invalid:**
```markdown
@PREV              # Case-sensitive (must be lowercase)
@ prev             # No space after @
@prev content      # No content on same line
Some text @prev    # Must be alone on line
```

### 16.9 Interaction with Schema Sections

The `@prev` directive works identically with schema-prefixed sections (`@section-id`):

```markdown
# @physical-description

## @hair

@prev

Now streaked with grey from stress.
```

The `@prev` directive references the previous content of the `@hair` section, regardless of whether it uses the schema prefix.

### 16.10 Error Handling

Tooling SHOULD provide clear error messages for invalid usage:

| Error | Example | Message |
|-------|---------|---------|
| `@prev` in base file | Using `@prev` in `_index.md` | `Error: @prev cannot be used in base files (no previous state exists)` |
| `@prev` outside section | `@prev` before any heading | `Error: @prev must appear within a section` |
| Invalid syntax | `@prev:invalid` | `Error: Unknown directive "@prev:invalid". Did you mean "@prev"?` |

### 16.11 Complete Example

**Base file (`/characters/kira-valdris/_index.md`):**
```markdown
---
name: "Kira Valdris III"
timeline: imperial-calendar
existence:
  start: "Year 819"
  end: "Year 847"
---

# @introduction

Kira Valdris III is the young Empress of the Valdris Empire, ascending to the throne at just 23 years old.

# @personality

Kira is idealistic but not naive. She genuinely believes in justice and equality.

- **Compassionate** — Cares deeply for common people
- **Strategic** — Plays the political game masterfully
- **Stubborn** — Once she commits to a path, she rarely wavers
```

**Delta file (`845-civil-war.md`):**
```markdown
---
timestamp: "Year 845"
summary: "Civil war transforms her"
---

# @introduction

@prev

She is now an empress at war, leading her armies personally against Duke Varren's rebellion.

# @personality

@prev

War has added new dimensions to her character:

- **Ruthless** — Does what must be done without hesitation
- **Haunted** — The weight of deaths she's ordered is crushing
```

**Resolved state at Year 845:**

> ## Introduction
> 
> Kira Valdris III is the young Empress of the Valdris Empire, ascending to the throne at just 23 years old.
> 
> She is now an empress at war, leading her armies personally against Duke Varren's rebellion.
> 
> ## Personality
> 
> Kira is idealistic but not naive. She genuinely believes in justice and equality.
> 
> - **Compassionate** — Cares deeply for common people
> - **Strategic** — Plays the political game masterfully
> - **Stubborn** — Once she commits to a path, she rarely wavers
> 
> War has added new dimensions to her character:
> 
> - **Ruthless** — Does what must be done without hesitation
> - **Haunted** — The weight of deaths she's ordered is crushing

---

## 17. Author Directives

Author directives provide metadata about content state and reader experience. They allow authors to mark incomplete content and hide spoilers from readers.

### 17.1 Overview

Author directives are block-level markers that wrap content:

| Directive | Purpose |
|-----------|--------|
| `@wip` / `@/wip` | Mark content as work-in-progress |
| `@spoiler` / `@/spoiler` | Mark content as containing spoilers |

These directives follow the same syntax patterns as content reference directives but use opening and closing tags to wrap content blocks.

### 17.2 Work-in-Progress (`@wip`)

The `@wip` directive marks content as incomplete or under development. This helps authors track what needs attention and allows tooling to filter or highlight unfinished work.

#### 17.2.1 Basic Syntax

```markdown
@wip
Content that is still being developed.
@/wip
```

The opening `@wip` and closing `@/wip` must each appear on their own line.

#### 17.2.2 Usage Examples

**Placeholder content:**
```markdown
# @background

@wip
TODO: Write the character's childhood backstory.
Need to research medieval education systems first.
@/wip

Born in a small village in the eastern provinces.
```

**Incomplete section:**
```markdown
# @physical-description

Tall with broad shoulders and a weathered face.

## @distinguishing-features

@wip
Need to decide on scars and tattoos.
Maybe a birthmark?
@/wip
```

**Author notes:**
```markdown
# @relationships

- [[sarah]] `spouse` — Married in Year 842

@wip
TODO: Add relationship with mentor character.
Also need to establish rivalry with Duke Varren.
@/wip
```

#### 17.2.3 Behavior

| Scenario | Behavior |
|----------|----------|
| Nested `@wip` blocks | **Allowed** — inner blocks are independent |
| `@wip` without closing `@/wip` | **Error** — must have matching close tag |
| `@/wip` without opening `@wip` | **Error** — must have matching open tag |
| Whitespace around directive | **Trimmed** — `  @wip  ` is valid |
| Directive with other text on line | **Invalid** — must be alone on the line |

Tooling SHOULD:
- Display WiP indicators visually (icons, highlights, different background)
- Provide filtering to show/hide WiP content
- Aggregate WiP blocks for progress tracking
- Preserve WiP content in output (it's author-facing, not reader-facing)

### 17.3 Spoilers (`@spoiler`)

The `@spoiler` directive marks content that reveals plot points readers may not have encountered yet. This allows tooling to hide, blur, or collapse spoiler content.

#### 17.3.1 Basic Syntax

```markdown
@spoiler
Content that contains spoilers.
@/spoiler
```

The opening `@spoiler` and closing `@/spoiler` must each appear on their own line.

#### 17.3.2 Usage Examples

**Hidden plot point:**
```markdown
# @introduction

Kira Valdris III is the young Empress of the Valdris Empire.

@spoiler
She dies at the age of 28 during the Sundering, sacrificing herself
to prevent an even greater catastrophe.
@/spoiler
```

**Secret relationship:**
```markdown
# @relationships

- [[marcus-ashford]] `uncle` — Lord Commander of the Imperial Guard
- [[theron-blackwood]] `ally` — Court mage

@spoiler
- [[theron-blackwood]] `lover` — Secret romantic relationship
- [[duke-varren]] — Secretly her half-brother
@/spoiler
```

**Twist revelation:**
```markdown
# @background

Theron Blackwood serves as court mage to the Empress.

@spoiler
He is actually a double agent working for the Circle of Magi.
His loyalty to Kira eventually overcomes his original mission,
and he sacrifices himself to save her during the Sundering.
@/spoiler
```

#### 17.3.3 Multiple Spoiler Blocks

A single file can contain multiple spoiler blocks:

```markdown
# @introduction

Senna is a young apprentice mage.

@spoiler
She survives the Sundering and witnesses Kira's death.
@/spoiler

# @background

Born to a merchant family in the capital.

@spoiler
She eventually becomes the First Consul of the New Valdris Republic,
shaping the post-magic world for decades.
@/spoiler
```

#### 17.3.4 Behavior

| Scenario | Behavior |
|----------|----------|
| Nested `@spoiler` blocks | **Allowed** — inner blocks are independent |
| `@spoiler` without closing `@/spoiler` | **Error** — must have matching close tag |
| `@/spoiler` without opening `@spoiler` | **Error** — must have matching open tag |
| Whitespace around directive | **Trimmed** — `  @spoiler  ` is valid |
| Directive with other text on line | **Invalid** — must be alone on the line |

Tooling SHOULD:
- Blur, collapse, or hide spoiler content by default
- Allow readers to reveal spoilers selectively (click to reveal)
- Provide global spoiler preferences (show all / hide all)
- Visually distinguish spoiler regions when revealed

### 17.4 Combining Directives

Author directives can be combined with each other and with content reference directives:

**WiP inside spoiler:**
```markdown
@spoiler
@wip
Need to write the actual death scene.
@/wip

Kira dies during the Sundering.
@/spoiler
```

**Spoiler with `@prev`:**
```markdown
# @background

@prev

@spoiler
Years later, it was revealed that he had orchestrated the entire conflict.
@/spoiler
```

### 17.5 Syntax Specification

Author directives follow these syntax rules:

```
wip-open      = "@wip"
wip-close     = "@/wip"
spoiler-open  = "@spoiler"
spoiler-close = "@/spoiler"

directive-line = [ whitespace ] directive [ whitespace ] newline
```

**Valid:**
```markdown
@wip
  @wip
@spoiler
  @/spoiler
```

**Invalid:**
```markdown
@WIP               # Case-sensitive (must be lowercase)
@ wip              # No space after @
@wip content       # No content on same line
Some text @spoiler # Must be alone on line
@/Spoiler          # Case-sensitive
```

### 17.6 Error Handling

Tooling SHOULD provide clear error messages for invalid usage:

| Error | Example | Message |
|-------|---------|--------|
| Unclosed block | `@wip` without `@/wip` | `Error: Unclosed @wip block starting at line X` |
| Unexpected close | `@/spoiler` without `@spoiler` | `Error: Unexpected @/spoiler at line X (no matching @spoiler)` |
| Invalid syntax | `@wip:note` | `Error: Unknown directive "@wip:note". Did you mean "@wip"?` |
| Mismatched tags | `@wip` closed with `@/spoiler` | `Error: Expected @/wip but found @/spoiler at line X` |

---

## 18. Examples

### 18.1 Complete Character Example

**File:** `/universe/characters/jack/_index.md`
```markdown
---
name: "Jack Vals"
timeline: gregorian
existence:
  start: "1995-06-09"
  end: unknown
tags: [protagonist, soldier, mercenary]
---

# Introduction

Jack Vals is a former soldier who became a mercenary after the Great War.

# Physical description

Jack is tall with broad shoulders and a weathered face.

## Hair

Short, dark brown.

## Distinguishing features

None yet.

# Personality

Jack is optimistic and trusting.

# Key Connections

See relationships: [[jack--sarah]], [[jack--sergeant-morris]]
```

**File:** `/universe/characters/jack/2015-the-war.md`
```markdown
---
timestamp: "2015-03-01"
summary: "Jack joins the military"
---

# Introduction

Jack Vals is a soldier fighting in the Great War.

# Physical description

## Distinguishing features

A fresh scar across his left eyebrow from combat.

# Personality

Jack has become hardened by war but maintains hope.
```

**File:** `/universe/characters/jack/2020-aftermath.md`
```markdown
---
timestamp: "2020-06-15"
summary: "Post-war Jack"
---

# Introduction

Jack Vals is a former soldier turned mercenary, haunted by his past.

# Physical description

## Hair

Short, dark brown with streaks of grey.

## Distinguishing features

A scar across his left eyebrow. His left arm is prosthetic.

# Personality

Jack has become bitter and withdrawn. He trusts no one.

# Key Connections

He spends most of his time at the [[old-tavern]].
```

### 18.2 Location Example

**File:** `/universe/locations/old-tavern/_index.md`
```markdown
---
name: "The Old Tavern"
existence:
  start: "1875"
  end: unknown
---

# Introduction

A weathered establishment at the crossroads of two major trade routes.

# Description

A two-story wooden building with a thatched roof. Warm light spills from its windows.

# History

Built in 1875 by a retired adventurer.

# Notable features

- A massive fireplace
- Walls covered with trophies and maps
- A secret basement
```

### 18.3 Timeline Example

**File:** `/universe/meta/timelines/eldoria-calendar.yaml`
```yaml
id: eldoria-calendar
name: "Eldorian Calendar"
description: "Calendar used in the Kingdom of Eldoria, counting from the First Dawn"
display_format: "Year {year} of the {age} Age"

tick_mapping:
  type: formula
  formula: "(age * 10000) + year"

explicit_events:
  "The First Dawn": 0
  "The Cataclysm": 30000
  "Before Time": -1

epoch:
  reference: "The First Dawn"
  tick: 0
```

### 18.4 Event Example

**File:** `/universe/events/the-sundering/_index.md`
```markdown
---
name: "The Sundering"
timeline: imperial-calendar
event_type: catastrophe
timestamp:
  start: "Year 847"
  end: "Year 847"
tags: [catastrophe, magic, world-changing]
---

# Introduction

The Sundering was the catastrophic moment when magic died. In a single instant, the ley lines went dark, the Veil collapsed, and the red moon Maloch shattered in the sky.

# Cause

[[duke-varren]] attempted to weaponize the [[heart-of-aethon]] against [[kira-valdris]]. The Empress intervened, causing the artifact to shatter.

# Key Participants

- [[kira-valdris]] — Died at the epicenter
- [[duke-varren]] — Died at the epicenter  
- [[theron-blackwood]] — Died at the epicenter
- [[senna]] — Survivor, witnessed from afar

# Location

[[ashenmoor-tower]] — Completely destroyed

# Consequences

- All magic ceased to function
- Millions died worldwide as magical infrastructure failed
- The [[circle-of-magi]] was destroyed
- The [[empire-of-valdris]] collapsed
- Eventually led to the [[new-valdris-republic]]
```

### 18.5 Relationship Example

**File:** `/universe/relationships/jack--sarah/_index.md`
```markdown
---
name: "Jack & Sarah"
timeline: gregorian

participants:
  a: "[[jack]]"
  b: "[[sarah]]"

existence:
  start: "1995-06-09"
  end: unknown

bonds:
  - type: childhood-friend
    symmetric: true
    strength: 0.9

tags: [friendship, romance]
---

# Introduction

Jack and Sarah grew up together on the same street in Portland.

# History

They first met at age 5 when Jack's family moved next door to Sarah's.

# Significant Moments

- **1995** — First meeting
- **2010** — Jack leaves for military service
```

**File:** `/universe/relationships/jack--sarah/2019-marriage.md`
```markdown
---
timestamp: "2019-08-15"
summary: "Jack and Sarah get married"

bonds:
  - type: spouse
    symmetric: true
    strength: 1.0
    
  - type: friend
    symmetric: true
    strength:
      a: 1.0
      b: 0.95
---

# Introduction

@prev

After Jack returned from the war, they reconnected and married in a small ceremony.

# Significant Moments

@prev

- **2019** — Married in Portland
```

**File:** `/universe/relationships/jack--sarah/2020-strain.md`
```markdown
---
timestamp: "2020-06-15"
summary: "Jack's trauma strains the marriage"

bonds:
  - type: spouse
    symmetric: true
    strength: 0.7
    
  - type: friend
    symmetric: true
    strength:
      a: 0.9
      b: 0.6          # Sarah struggles with Jack's withdrawal
    
  - type: caretaker
    from: b           # Sarah cares for Jack
    strength: 0.8
---

# Introduction

@prev

Jack's PTSD and emotional withdrawal are creating distance in their marriage.
```

### 18.6 Relationship Type Schema Example

**File:** `/universe/meta/schemas/relationship-types.yaml`
```yaml
id: relationship-types
name: "Relationship Types"
description: "Custom relationship types for The Chronicles universe"

types:
  # Family relationships
  parent:
    label: "Parent"
    default_symmetric: false
    inverse: child
    valid_between:
      - [character, character]
  
  child:
    label: "Child"
    default_symmetric: false
    inverse: parent
    valid_between:
      - [character, character]
  
  sibling:
    label: "Sibling"
    default_symmetric: true
    valid_between:
      - [character, character]
  
  # Romantic relationships
  spouse:
    label: "Spouse"
    default_symmetric: true
    valid_between:
      - [character, character]
  
  lover:
    label: "Lover"
    default_symmetric: true
    valid_between:
      - [character, character]
  
  # Social relationships
  friend:
    label: "Friend"
    default_symmetric: true
    valid_between:
      - [character, character]
  
  childhood-friend:
    label: "Childhood Friend"
    description: "Friends since childhood"
    default_symmetric: true
    valid_between:
      - [character, character]
  
  rival:
    label: "Rival"
    default_symmetric: true
    valid_between:
      - [character, character]
  
  enemy:
    label: "Enemy"
    default_symmetric: true
    valid_between:
      - [character, character]
      - [faction, faction]
  
  # Professional relationships
  mentor:
    label: "Mentor"
    default_symmetric: false
    inverse: student
    valid_between:
      - [character, character]
  
  student:
    label: "Student"
    default_symmetric: false
    inverse: mentor
    valid_between:
      - [character, character]
  
  employer:
    label: "Employer"
    default_symmetric: false
    inverse: employee
    valid_between:
      - [character, character]
      - [faction, character]
  
  employee:
    label: "Employee"
    default_symmetric: false
    inverse: employer
    valid_between:
      - [character, character]
      - [character, faction]
  
  # Care relationships
  caretaker:
    label: "Caretaker"
    description: "Someone who provides care"
    default_symmetric: false
    inverse: dependent
    valid_between:
      - [character, character]
  
  dependent:
    label: "Dependent"
    description: "Someone who receives care"
    default_symmetric: false
    inverse: caretaker
    valid_between:
      - [character, character]
  
  # Location relationships
  capital:
    label: "Capital of"
    default_symmetric: false
    inverse: has-capital
    valid_between:
      - [location, faction]
  
  located-in:
    label: "Located in"
    default_symmetric: false
    inverse: contains
    valid_between:
      - [location, location]
      - [item, location]
```

---

## Appendix A: Reserved Keywords

| Keyword | Context | Meaning |
|---------|---------|---------|
| `eternal` | existence.start/end | No beginning/end |
| `unknown` | existence.end | Undefined or mysterious |
| `UT:` | cross-reference | Universal Tick prefix |
| `@prev` | directive | Include previous section content |
| `@wip` / `@/wip` | directive | Mark work-in-progress content |
| `@spoiler` / `@/spoiler` | directive | Mark spoiler content |

## Appendix B: File Naming Summary

| File Type | Valid Names | Resolution Order |
|-----------|-------------|------------------|
| Base file | `_index.md`, `index.md` | `_index.md` first |
| Delta file | Any `.md` filename | By YAML timestamp |
| Timeline | `*.yaml` in `/meta/timelines/` | — |
| Schema | `*.yaml` in `/meta/schemas/` | — |
| Relationship folder | `entityA--entityB/`, `meaningful-name/` | — |
| Relationship types | `relationship-types.yaml` in `/meta/schemas/` | — |

## Appendix C: Future Considerations

The following features are being considered for future versions:

- Validation tooling
- Query language for searching across time
- Multi-universe support (crossovers)
- Branching timelines (alternate realities)

---

## License

This specification is released under [TBD — Creative Commons recommended].

---

*This is a living document. Contributions and feedback are welcome.*
