# 🐍 Snake AI — Autonomous Snake Game Using BFS

An intelligent Snake Game built with **Python and Pygame** where the snake plays automatically using **Breadth-First Search (BFS) pathfinding** and safety checks to avoid trapping itself.

The AI searches for the shortest path to food, checks whether the move is reasonably safe, follows its tail when necessary, and chooses moves that preserve the maximum reachable space.

## ✨ Features

- 🤖 **Autonomous AI:** The snake plays without manual directional controls.
- 🧠 **BFS Pathfinding:** Finds the shortest available path to the food.
- 🛡️ **Safety Check:** Checks whether the snake can still reach its tail after pursuing food.
- 🐍 **Tail Chasing:** Attempts to follow its tail when the food route is unsafe.
- 🌐 **Space Exploration:** Evaluates reachable space to choose an alternative move.
- 🍎 **Random Food Generation:** Food spawns at an unoccupied grid position.
- 🎨 **Modern Visuals:** Dark background, checkerboard grid, colorful snake, and food animation.
- 📊 **Live Statistics:** Displays snake length, best length, and total games.
- ⚡ **Adjustable Speed:** Increase or decrease the game speed while playing.

## 🛠️ Technologies Used

- Python 3
- Pygame
- `collections.deque` for BFS queues
- `random` for food generation

## 🧠 How the AI Works

The AI uses three decision-making strategies:

1. **Find Food:** Uses BFS to calculate the shortest path to the food.
2. **Check Safety:** Simulates the proposed path and checks tail accessibility before choosing the food route.
3. **Chase Tail:** If the food route fails the safety check, the snake attempts to follow its tail.
4. **Find Open Space:** If neither path is available, the AI evaluates reachable space and selects a move with the most open area.

> Note: The safety check is a heuristic, not a mathematical guarantee that the snake can never get trapped.

## 📦 Installation

### 1. Install Python

Download Python from [python.org](https://www.python.org/downloads/).

### 2. Install Pygame

Open your terminal or PowerShell and run:

```bash
python -m pip install pygame
```

If you use Python 3.11 specifically:

```bash
py -3.11 -m pip install pygame
```

### 3. Download or Clone the Repository

```bash
git clone https://github.com/suman9834/snake_game.git
```

Move into the project directory:

```bash
cd snake_game
```

### 4. Run the Game

Save the Python code as `snake_ai.py` and run:

```bash
python snake_ai.py
```

## 🎮 Controls

| Key | Action |
|---|---|
| ⬆️ UP Arrow | Increase game speed |
| ⬇️ DOWN Arrow | Decrease game speed |
| ❌ Close Window | Exit the game |

The snake automatically decides where to move. No manual movement controls are required.

## 📂 Project Structure

```text
snake_game/
│
├── snake_ai.py      # Main game and AI logic
├── README.md        # Project documentation
└── requirements.txt # Dependencies (optional)
```

### requirements.txt

```text
pygame
```

Install all dependencies with:

```bash
python -m pip install -r requirements.txt
```

## 🔍 Core Algorithms

| Algorithm / Technique | Purpose |
|---|---|
| Breadth-First Search (BFS) | Finds the shortest path |
| Graph Traversal | Explores available grid cells |
| Reachability Analysis | Estimates open space |
| Tail Accessibility Check | Helps avoid unsafe food routes |
| Random Sampling | Places food on free cells |

## 🎯 Learning Objectives

This project demonstrates practical applications of:

- Artificial intelligence and pathfinding
- Graph traversal algorithms
- Game development with Pygame
- Grid-based movement and collision avoidance
- Decision-making and safety heuristics
- Real-time rendering and event handling

## 🚀 Future Improvements

- [ ] Add A* pathfinding and compare it with BFS.
- [ ] Improve safety checks using simulated future moves.
- [ ] Add a score history and high-score saving.
- [ ] Display the AI's planned path.
- [ ] Add difficulty levels and configurable grid sizes.
- [ ] Implement reinforcement learning for autonomous gameplay.

## 👨‍💻 Author

**Suman Kumar**

B.Tech CSE (AI & Data Science) | AI/ML Enthusiast | Python Developer

- GitHub: [suman9834](https://github.com/suman9834)
- LeetCode: [sumankumar211](https://leetcode.com/u/sumankumar211/)

## ⭐ Support

If you find this project interesting, give the repository a ⭐ on GitHub and share your feedback!

---

*Built with Python, Pygame, BFS Pathfinding, and a little AI intelligence. 🐍🤖*
