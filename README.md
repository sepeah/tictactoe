# TicTacToe AI – 5x5 Edition

This is a Python-based TicTacToe project developed by **Sepe Ahtosalo**. Contributions are welcome!

## 🧠 Background

The original version was created as part of the *Introduction to AI* course at the University of Helsinki 
in 2025. It implemented a basic MinMax algorithm for a standard 3×3 board.

## 🎯 Current Version

The game has been expanded to a **5×5 board**, with the objective of connecting **4 in a row**. This 
increases the complexity and depth of the game tree significantly.

### ✅ Features
- MinMax algorithm for decision-making
- Alpha-beta pruning to reduce search space
- End-game search depth reaches 9 with 13 empty cells in reasonable time

## 🚧 Challenges

Despite pruning, the search tree remains large, especially from an empty board. To improve performance 
and enable full-game play, the following enhancements are under consideration:

- Implementing a **heuristic evaluation function** to complement terminal state scoring (`-1`, `0`, `1`)
- **Restricting child node generation** to cells adjacent to existing moves (`x` or `o`)

## 📦 How to Run

Clone the repository and run the main script:

```bash
python main.py
