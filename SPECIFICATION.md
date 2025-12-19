# Timeliner Standard Specification

**Version:** 0.2.0-draft  
**Status:** Draft  
**Last Updated:** 2024-12-19

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
14. [Examples](#14-examples)

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
│       └── location.yaml
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

# Relationships

- [[sarah]] — Wife (since Year 42)
- [[old-tavern]] — Favorite hangout
```

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

### 8.5 Recommended Section Names

Entity type schemas MAY define recommended section names. These are suggestions, not requirements. Authors are free to use any section names.

*(Section schemas will be defined in future versions of this specification)*

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

Relationships between entities are expressed in Markdown sections, allowing them to evolve over time like any other property.

### 12.1 Forward References

When entity A references entity B, this creates a **forward reference**:

```markdown
# Relationships

- [[sarah]] — Wife (since Year 42)
- [[old-tavern]] — Favorite hangout
```

### 12.2 Bidirectional Relationship Tracking

The Timeliner Standard does **not** require relationships to be manually duplicated. Instead, tooling SHOULD compute **backlinks** automatically.

**Principle**: Write relationships once, compute the reverse.

#### How it Works

1. Jack's file contains: `- [[sarah]] — Wife (since Year 42)`
2. Tooling scans all files and builds a reference index
3. When viewing Sarah's file, tooling shows: "Referenced by: [[jack]] (Relationships section)"

#### Implementation Recommendations

| Approach | Description | Pros | Cons |
|----------|-------------|------|------|
| **Runtime computation** | Calculate backlinks on-demand | Always accurate | Slower for large universes |
| **Index file** | Generate `.timeliner/backlinks.json` | Fast queries | Requires rebuild on changes |
| **Hybrid** | Index + invalidation on file change | Best of both | More complex |

**Recommended**: Hybrid approach with file watching.

### 12.3 Relationship Context

Backlinks SHOULD include context to be useful:

```yaml
# Computed backlinks for sarah/_index.md
backlinks:
  - source: "characters/jack/_index.md"
    section: "Relationships"
    context: "[[sarah]] — Wife (since Year 42)"
    timestamp: null  # From base file
    
  - source: "characters/jack/845-civil-war.md"  
    section: "Relationships"
    context: "[[sarah]] — Wife (married 2019)"
    timestamp: "Year 845"
    
  - source: "events/the-wedding/_index.md"
    section: "Participants"
    context: "[[sarah]] — Bride"
    timestamp: "Year 842"
```

### 12.4 Typed Relationships (Optional)

Authors MAY use a structured format for machine-parseable relationships:

```markdown
# Relationships

- [[sarah]] `spouse` — Married in Year 42
- [[theron-blackwood]] `ally` `friend` — Met during the war
- [[duke-varren]] `enemy` — Nemesis
- [[old-tavern]] `frequents` — Favorite drinking spot
```

The backtick-wrapped terms are **relationship types** that tooling can use for filtering and visualization.

Standard relationship types (suggestions, not requirements):
- **Personal**: `spouse`, `parent`, `child`, `sibling`, `friend`, `rival`, `enemy`, `lover`
- **Professional**: `employer`, `employee`, `ally`, `mentor`, `student`, `colleague`
- **Spatial**: `located-in`, `frequents`, `owns`, `created`
- **Membership**: `member-of`, `leader-of`, `founder-of`

### 12.5 Relationship Evolution

Relationships change over time. Each delta can update the Relationships section:

**Base file (Year 819):**
```markdown
# Relationships
- [[sarah]] `friend` — Childhood friend
```

**Delta (Year 842):**
```markdown
# Relationships
- [[sarah]] `spouse` — Married this year
- [[theron-blackwood]] `lover` — Secret relationship
```

**Delta (Year 845):**
```markdown
# Relationships
- [[sarah]] `spouse` — Supporting each other through the war
- [[theron-blackwood]] `spouse` `ally` — Now public; fights at her side
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

## 14. Examples

### 14.1 Complete Character Example

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

# Relationships

- [[sarah]] — Childhood friend
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

# Relationships

- [[sarah]] — Childhood friend (hasn't seen her in years)
- [[sergeant-morris]] — Commanding officer
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

# Relationships

- [[sarah]] — Wife (married 2019)
- [[old-tavern]] — Favorite place to drink alone
```

### 14.2 Location Example

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

### 14.3 Timeline Example

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

### 14.4 Event Example

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

---

## Appendix A: Reserved Keywords

| Keyword | Context | Meaning |
|---------|---------|---------|
| `eternal` | existence.start/end | No beginning/end |
| `unknown` | existence.end | Undefined or mysterious |
| `UT:` | cross-reference | Universal Tick prefix |

## Appendix B: File Naming Summary

| File Type | Valid Names | Resolution Order |
|-----------|-------------|------------------|
| Base file | `_index.md`, `index.md` | `_index.md` first |
| Delta file | Any `.md` filename | By YAML timestamp |
| Timeline | `*.yaml` in `/meta/timelines/` | — |
| Schema | `*.yaml` in `/meta/schemas/` | — |

## Appendix C: Future Considerations

The following features are being considered for future versions:

- Entity type schemas with recommended sections
- Validation tooling
- Query language for searching across time
- Multi-universe support (crossovers)
- Branching timelines (alternate realities)

---

## License

This specification is released under [TBD — Creative Commons recommended].

---

*This is a living document. Contributions and feedback are welcome.*
