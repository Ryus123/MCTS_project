# MCTS for *Order and Chaos*

## Overview

This project explores the application of various Monte Carlo Tree Search (MCTS) algorithms to the asymmetric two-player game *Order and Chaos*. The **Order** player aims to create a line of five identical symbols (X or O), while **Chaos** tries to prevent this from happening.
Tested algorithms include:
- UCT  
- RAVE / GRAVE  
- Enhanced Playouts  
- NRPA  
- NMCS  
- Sarsa-UCT (a reinforcement learning approach)

## Game Description

- Played on a 6x6 board (36 cells).
- Both players can play either X or O on each turn.
- Order’s goal: create a line of five identical symbols.
- Chaos’s goal: prevent any such line.

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/Ryus123/MCTS_project.git
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Launch the notebook:
   ```bash
   jupyter notebook MCTS_for_Order_&_Chaos.ipynb
