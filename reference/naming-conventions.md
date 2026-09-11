# Project Naming Convention

## Chapter / episode identity

The overall voyage is **Chapter 1 — First Voyage**, divided into numbered YouTube episodes:

`CH01-EP01 — Lisbon: The Departure`  
`CH01-EP02 — Atlantic: Into the Unknown`

Use zero-padded IDs for sorting and continuity: `CH01-EP03`, `CH01-EP04`, etc.

## Media names

- Episode video: `Vasco-Da-Gama-CH01-EP02-v1.mp4`
- Thumbnail: `CH01-EP02-thumbnail-v1.png`
- Scene motion clip: `CH01-EP02-S01-motion-v1.mp4`
- Blueprint: `CH01-EP02-blueprint.md`
- Prompt pack: `CH01-EP02-image-to-video.md`
- Review: `CH01-EP02-review.md`

Existing locked filenames remain unchanged for compatibility within their episode folders.

## Chapter & Episode Directory Architecture

All assets belonging to an episode are unified in its dedicated chapter/episode directory:

```
chapters/
└── chapter-01-first-voyage/
    ├── episode-01-lisbon/
    │   ├── README.md                          # Episode overview & historical scope
    │   ├── scenes/                            # Scene records (CH01-S01 to S08)
    │   ├── prompts/                           # Image and image-to-video prompt packs
    │   ├── storyboards/                       # Storyboard & continuity sheets
    │   ├── images/                            # Canonical stills, variants & thumbnail
    │   ├── videos/                            # Master episode video & scene motion clips
    │   └── production/                        # Blueprint, YouTube package, locks & reviews
    │       ├── locks/                         # Immutable lock manifests
    │       └── reviews/                       # Per-scene review files
    ├── episode-02-atlantic/
    ├── episode-03-cape/
    ...
    └── episode-11-lisbon-return/
```

Series-wide assets remain at the root level:
- `reference/`: Global characters, ships, geography, timeline, and visual bible
- `production/`: Master film compilation, shorts packages, approval log, and `tools/`
- `images/maps/`: Master portolan chart
- `videos/maps/`: Master voyage overview route map

