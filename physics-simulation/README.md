# Physics Particle Game

A physics-based particle simulation game built with Pygame.

## Features
- Realistic particle physics with collision detection
- Mouse-based attraction/repulsion forces
- Wind effects
- Motion blur trails
- Particle fading and lifetime
- **Game Mode**: Hit moving targets to score points!

## Controls
- **Drag mouse**: Launch particles
- **G**: Toggle attraction mode
- **F**: Toggle repulsion mode
- **LEFT/RIGHT arrows**: Apply wind force
- **UP/DOWN arrows**: Adjust gravity
- **SPACE**: Pause
- **C**: Clear particles
- **R**: Restart game

## Game Objective
Hit moving targets with particles before time runs out!
- Small targets (yellow): 100 points
- Medium targets (pink): 50 points
- Large targets (cyan): 25 points

**Goal**: Score 500+ points in 60 seconds to win!

## Requirements
- Python 3.x
- Pygame
- NumPy

## Installation
```bash
pip install pygame numpy
python main.py