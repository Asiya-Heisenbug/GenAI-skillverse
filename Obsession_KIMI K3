# OBSESSION: THE CHASE

### 3D Horror Survival Chase Game

**OBSESSION: THE CHASE** is a 3D horror survival game inspired by the horror-thriller concept of *Obsession*. The player controls a character named **Bear**, who must run through a dark environment while being pursued by **Nikki**, a hostile antagonist.

The primary objective is simple:

> **RUN. ESCAPE. SURVIVE.**

The game combines 3D graphics, enemy AI, player movement, health mechanics, atmospheric lighting, sound effects, and increasing difficulty to create a tense horror-chase experience.

---

## ⚠️ Disclaimer

This project is a **fan-made, non-commercial game project** created for educational and experimental purposes.

The characters and concepts inspired by *Obsession* belong to their respective copyright holders. This project is not affiliated with, endorsed by, or officially connected to the movie or its creators.

---

# 1. Project Overview

The game places the player in control of **Bear**, who is being relentlessly chased by **Nikki**.

Nikki follows the player through a dark 3D environment while carrying a saw. The player must continuously move forward and maintain enough distance from Nikki to survive.

If Nikki gets too close, the player's health begins to decrease.

The player must therefore:

* Run through the environment.
* Avoid Nikki.
* Maintain distance from the enemy.
* React to audio and visual warning effects.
* Survive for as long as possible.
* Avoid allowing the health bar to reach zero.

---

# 2. Game Objective

The main objective is to survive the chase.

The player starts with a full health bar and must escape Nikki for as long as possible.

### Survival System

When Nikki is far away:

**Health remains stable.**

When Nikki approaches the player:

**Damage begins to increase.**

When Nikki gets extremely close:

**Rapid health loss occurs.**

When health reaches zero:

**GAME OVER**

This creates a continuous risk/reward system where the player must prioritize distance and movement.

---

# 3. Main Characters

## Bear — Player Character

Bear is the playable character.

The player controls Bear using keyboard movement controls.

### Controls

| Key   | Action        |
| ----- | ------------- |
| W / ↑ | Move Forward  |
| S / ↓ | Move Backward |
| A / ← | Move Left     |
| D / → | Move Right    |
| Mouse | Look Around   |

The player must use these controls to navigate the environment and escape Nikki.

---

## Nikki — Enemy Character

Nikki acts as the main enemy of the game.

Her purpose is to continuously pursue Bear.

The enemy system is designed around a simple chase mechanic:

**Detect Player → Follow Player → Reduce Distance → Attack/Damage**

Nikki becomes increasingly dangerous as the game progresses.

Her presence is reinforced using:

* Dark visual design
* Red lighting
* Enemy animations
* Saw effects
* Horror audio
* Chase sounds
* Screen effects
* Proximity-based damage

---

# 4. Core Gameplay Mechanics

## 4.1 Player Movement

The player can move around the 3D environment using WASD or arrow keys.

Movement is designed to make the player feel as though they are actively escaping from an approaching enemy.

---

## 4.2 Enemy Chase AI

Nikki continuously tracks the player's position.

The basic enemy behaviour is:

```text
Player moves
      ↓
Nikki detects player
      ↓
Nikki calculates direction
      ↓
Nikki moves toward player
      ↓
Distance decreases
      ↓
Player takes damage
```

The chase system creates constant pressure on the player.

---

# 5. Health System

A health bar represents the player's current survival state.

The player begins with maximum health.

For example:

```text
HEALTH
████████████████████ 100%
```

As Nikki approaches:

```text
HEALTH
██████████░░░░░░░░░░ 50%
```

At critical health:

```text
HEALTH
██░░░░░░░░░░░░░░░░░░ 10%
```

When health reaches zero:

```text
0 HP
   ↓
GAME OVER
```

The health system gives the player immediate feedback about how dangerous the current situation is.

---

# 6. Proximity Damage

One of the main mechanics is distance-based damage.

The game continuously calculates the distance between Bear and Nikki.

Conceptually:

```text
Distance > Safe Distance
        ↓
     No Damage

Distance < Warning Distance
        ↓
    Small Damage

Distance < Attack Distance
        ↓
    Heavy Damage

Health <= 0
        ↓
     GAME OVER
```

This means the player cannot simply stand still.

The closer Nikki gets, the more dangerous the situation becomes.

---

# 7. Horror Effects

To create a horror atmosphere, the game uses several visual effects.

### Environmental Effects

* Dark corridor/environment
* Flickering lights
* Red lighting
* Shadows
* Atmospheric particles
* Dark textures
* Horror-themed environment design

### Player Damage Effects

When the player takes damage:

* Screen flashes red.
* Camera shake can occur.
* Blood/damage vignette appears.
* Health decreases.

These effects communicate danger without requiring the player to constantly look at the health bar.

---

# 8. Audio System

Audio is an important part of the horror experience.

Nikki's presence is reinforced through repeated voice/audio cues, including the phrase:

**"I love you."**

The audio becomes part of the psychological horror atmosphere while the player is being chased.

Additional possible audio elements include:

* Footsteps
* Saw sounds
* Chase music
* Environmental ambience
* Warning sounds
* Damage sounds
* Game-over audio

---

# 9. Difficulty System

The game can progressively become more difficult as the player survives longer.

For example:

```text
Game Start
   ↓
Normal Nikki Speed
   ↓
Player Survives
   ↓
Nikki Speed Increases
   ↓
Player Survives Longer
   ↓
Nikki Becomes More Aggressive
   ↓
Maximum Difficulty
```

This prevents the game from becoming predictable and encourages the player to survive for a higher score/time.

---

# 10. 3D Environment

The game is designed as a fully 3D horror environment.

The environment focuses on creating a dark and claustrophobic atmosphere.

Important environmental elements include:

* 3D corridor
* Dark walls
* Flickering lights
* Red emergency lighting
* Atmospheric particles
* Horror decorations
* Long chase paths
* Limited visibility

The environment is intentionally designed to make the player feel vulnerable while being pursued.

---

# 11. Camera System

The game uses a 3D camera that follows the player.

The camera provides an over-the-shoulder/third-person perspective, allowing the player to see both the environment and the approaching enemy.

Camera effects can also be used during dangerous situations.

### Damage Camera Effects

When Nikki gets close:

```text
Nikki approaches
      ↓
Damage detected
      ↓
Camera shake
      ↓
Red screen effect
      ↓
Health decreases
```

---

# 12. Technology Stack

The project uses web-based 3D technologies.

### Frontend

* HTML
* CSS
* JavaScript

### 3D Engine

* Three.js
* WebGL

### Game Systems

* JavaScript game loop
* Collision/distance detection
* Keyboard input handling
* Camera controls
* Health management
* Enemy movement
* Audio management

---

# 13. Three.js

**Three.js** is used to create and render the 3D game environment inside the browser.

It handles major components such as:

* 3D scenes
* Cameras
* Lighting
* Meshes
* Materials
* Animations
* Rendering
* 3D positioning

The basic architecture is:

```text
Three.js Scene
      │
      ├── Camera
      ├── Lights
      ├── Environment
      ├── Bear
      ├── Nikki
      ├── Saw
      └── Effects
```

---

# 14. Game Loop

The game continuously updates using a game loop.

Conceptually:

```text
START GAME
    ↓
Read Keyboard Input
    ↓
Move Bear
    ↓
Update Nikki AI
    ↓
Calculate Distance
    ↓
Check Health
    ↓
Update Effects
    ↓
Render 3D Scene
    ↓
Repeat
```

This loop runs continuously while the game is active.

---

# 15. Game States

The game contains several possible states.

### Start Screen

The player sees the game title and starts the game.

```text
OBSESSION: THE CHASE

[ ENTER THE NIGHTMARE ]
```

### Playing

The player controls Bear and attempts to escape Nikki.

### Critical Health

The player receives strong visual/audio feedback when health becomes low.

### Game Over

When health reaches zero, the chase ends and the game displays the game-over screen.

---

# 16. User Interface

The interface contains important gameplay information.

### Main UI Elements

* Health bar
* Game timer
* Survival distance
* Start button
* Game-over screen
* Restart button
* Damage indicators

Example:

```text
┌───────────────────────────────┐
│ HEALTH: ████████████░░  75%   │
│ SURVIVAL TIME: 01:24          │
└───────────────────────────────┘
```

---

# 17. Game Flow

The complete gameplay flow is:

```text
              START
                │
                ▼
       ENTER THE NIGHTMARE
                │
                ▼
          Spawn Bear
                │
                ▼
          Spawn Nikki
                │
                ▼
        Begin Chase
                │
                ▼
       Player Runs Away
                │
                ▼
       Update Enemy AI
                │
                ▼
       Calculate Distance
                │
        ┌───────┴────────┐
        │                │
      SAFE            TOO CLOSE
        │                │
        ▼                ▼
   Keep Running      Lose Health
                         │
                         ▼
                 Is Health > 0?
                    │       │
                   YES      NO
                    │       │
                    ▼       ▼
               Continue   GAME OVER
                Chase
```

---

# 18. Key Features

### 🎮 Gameplay

* Fully 3D horror chase
* Third-person player movement
* Enemy pursuit system
* WASD/arrow-key controls
* Survival gameplay

### 👁️ Horror

* Dark environment
* Horror atmosphere
* Flickering lights
* Red lighting
* Enemy chase
* Saw-based enemy design
* Audio cues
* Screen damage effects

### ❤️ Health

* Real-time health bar
* Distance-based damage
* Critical-health state
* Game-over condition

### 🤖 Enemy AI

* Player tracking
* Continuous pursuit
* Dynamic movement
* Increasing difficulty

---

# 19. Project Architecture

A possible project structure is:

```text
OBSESSION-THE-CHASE/
│
├── index.html
├── style.css
├── game.js
│
├── assets/
│   ├── models/
│   │   ├── bear/
│   │   └── nikki/
│   │
│   ├── textures/
│   │
│   ├── sounds/
│   │   ├── chase.mp3
│   │   ├── footsteps.mp3
│   │   ├── saw.mp3
│   │   └── voice.mp3
│   │
│   └── environment/
│
├── README.md
└── LICENSE
```

---

# 20. Challenges Faced

During development, several technical challenges can occur.

### 1. 3D Performance

Rendering a complete 3D environment in a browser can be demanding.

Optimization is required for:

* Number of objects
* Lighting
* Shadows
* Texture sizes
* Particle effects

### 2. Enemy Movement

The enemy must continuously follow the player without behaving unnaturally.

### 3. Distance Detection

The game needs accurate distance calculations to determine when the player should receive damage.

### 4. Horror Atmosphere

Lighting, audio, environment design, and camera effects must work together to create tension without making the scene impossible to navigate.

### 5. Game State Management

The game needs to correctly transition between:

```text
START → PLAYING → CRITICAL → GAME OVER
```

---

# 21. Future Improvements

Possible future additions include:

* Multiple levels
* More detailed enemy animations
* Advanced pathfinding
* Randomized chase routes
* Stamina system
* Hiding mechanics
* Doors and obstacles
* Safe zones
* Multiple endings
* Collectible items
* More enemy behaviours
* Better 3D character models
* Spatial audio
* Controller support
* Mobile controls
* Online leaderboard
* Procedurally generated environments

---

# 22. Learning Outcomes

This project demonstrates practical understanding of:

* JavaScript
* HTML/CSS
* Three.js
* WebGL
* 3D graphics
* Game loops
* Keyboard input
* Camera systems
* Collision/distance detection
* Enemy AI concepts
* Health systems
* Audio integration
* UI development
* Game-state management

The project also demonstrates how multiple programming concepts can be combined to create an interactive real-time application.

---

# 23. Conclusion

**OBSESSION: THE CHASE** is a 3D browser-based horror survival game focused on continuous enemy pursuit.

The player controls Bear and must survive while Nikki follows them through a dark environment. The combination of enemy AI, health mechanics, 3D graphics, audio, lighting, and visual effects creates a tense survival experience.

The project demonstrates how **Three.js, JavaScript, HTML, CSS, game logic, and multimedia assets** can be combined to develop an interactive 3D game directly in a web browser.

The main gameplay philosophy is simple:

> **Don't stop running.**
>
> **Don't let Nikki get close.**
>
> **Survive the chase.**

---

## Project Type



**Category:** 3D Horror / Survival / Chase Game
**Platform:** Web Browser
**Engine:** Three.js
**Language:** JavaScript
**Rendering:** WebGL
**Status:** Development / Experimental Fan Project
**Purpose:** Educational and Game Development Project
