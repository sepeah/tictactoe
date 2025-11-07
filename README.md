# TicTacToe AI – 5x5 Edition

This is a Python-based TicTacToe project developed by **Sepe Ahtosalo**. Contributions are welcome!

## 🧠 Background

The original version was created as part of the *Introduction to AI* course at the University of Helsinki 
in 2025. It implemented a basic MinMax algorithm for a standard 3×3 board.

## 🎯 Current Version

The game has been expanded to a **5×5 board**, with the objective of connecting **4 in a row**. This 
increases the complexity and depth of the game tree significantly, making it an altogether more complex problem to be solved by this type of algorithm.

### ✅ Features
- MinMax algorithm for decision-making
- Alpha-beta pruning to reduce search space
- Move generation favours centerboard for efficiency
- Time-out allows for early game moves to be generated
- A depth-limited fast check used as a fallback after time-out

## 🚧 Challenges

Despite pruning, the search tree remains large, especially from an empty board (a staggering 25! = 1551121004 3330985984 000000 nodes). Time-limited depth-first search and centerboard-first child generation are far from an ideal solution in early game, but at about move 14 the algorithm starts to work better.
Changes being considered:

- Implementing a **heuristic evaluation function** to complement terminal state scoring (`-1`, `0`, `1`)
- a depth limited or breadth first search for early board states

A pygame version with graphics and gameplay against the engine is in the works.

## 📦 How to Run

Clone the repository and run the main script to generate a game from with play(state). 
Use nextmove(state) to create a single move. See the commented-out section in main.
To change the game situation edit hardcoded game state test_board.
To change the time used to search for a move edit the parameter in nextmove(state, timeout=5.0)

```bash
python main.py
