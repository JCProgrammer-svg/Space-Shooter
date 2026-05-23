# Space Shooter — 2-Player Local PvP Game

A fast-paced two-player space combat game built with Python and Pygame. Both players control polygon-shaped spaceships on opposite sides of a split screen, trying to deplete each other's health bar by landing shots.

---

## Description

Space Shooter is a local multiplayer game where two players face off in real time on the same keyboard. Each player pilots a uniquely shaped and colored spaceship, fires projectiles in multiple directions, and maneuvers across their half of the screen. The game ends when one player's health bar is fully depleted — displaying a Game Over screen with the winner's name.

---

## Features

- **2-Player Local Multiplayer** — Both players share the same keyboard; no network required.
- **Split-Screen Arena** — A white dividing line separates the two sides of the 1200×700 battlefield.
- **Multi-Directional Shooting** — Each player can fire in three directions: straight, diagonal up, and diagonal down.
- **Shot Cooldown System** — Each firing direction has an independent cooldown (400ms) to prevent spamming.
- **Health Bar System** — Visual health bars at the top of the screen shrink as players take hits.
- **Boundary Enforcement** — Players are constrained to their respective halves and cannot move off-screen.
- **Collision Detection** — Custom polygon-based hit detection determines when bullets strike a ship.
- **Game Over Screen** — Announces the winner when a player's health reaches zero, with a 3-second display before closing.
- **30 FPS Gameplay Loop** — Smooth, consistent frame-rate via Pygame's clock.

---

## Controls

| Action | Player 1 (Purple) | Player 2 (Teal) |
|---|---|---|
| Move Up | `W` | `↑` |
| Move Down | `S` | `↓` |
| Move Left | `A` | `←` |
| Move Right | `D` | `→` |
| Fire Straight | `F` | `J` |
| Fire Diagonal Up | `R` | `I` |
| Fire Diagonal Down | `C` | `M` |

---

## Technologies

| Technology | Purpose |
|---|---|
| **Python 3** | Core programming language |
| **Pygame** | Game loop, rendering, input handling, collision, and timing |

---

## Getting Started

**Prerequisites:** Python 3 and Pygame must be installed.

```bash
pip install pygame
python space_shooter_new.py
```

---

## Project Structure

```
space_shooter_new.py   # Single-file game — all logic, rendering, and game loop
```

---

## Notes

- The game window is fixed at **1200 × 700 pixels**.
- Player 1 starts on the **left half**; Player 2 starts on the **right half**.
- Bullets that leave the screen boundaries are automatically removed.
- Health is represented by the width of the red polygon bar at the top of each side.
