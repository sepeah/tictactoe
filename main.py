from alphabeta import ConnectFour, max_value, min_value

"""
    play(state): makes turn and prints the result of it until the game is over
    value() in ConnectFour class: returns the current score of the game (0 for draw, 1 for x win, -1 for o win)
    generate_children() in ConnectFour class: returns a list of all possible states after this turn
    alpha_beta_value(node): implements the MinMax algorithm with alpha-beta pruning
    max_value(node, alpha, beta): implements the MinMax algorithm with alpha-beta pruning
    min_value(node, alpha, beta):implements the MinMax algorithm with alpha-beta pruning
    
    currently main tests the tictactoe with a hard-coded test board. Future plans include adding
    a heuristic evaluation for non-terminal states and using a depth limit for the search.
    
    """


def play(state):
    """Makes turn and prints the result of it until the game is over
    :param state: The initial state of the game
    """
    alpha = -1
    beta = 1
    print(state)
    if state.state == 5*5*"?":
        alkusiirto = state.state[:12] + 'x' + state.state[13:]
        state = ConnectFour(alkusiirto, False)
        print(state)
    
    while not state.is_end_state():
        if state.is_max_node():
            value, state = max_value(state, alpha, beta)
        else:
            value, state = min_value(state, alpha, beta)
        print(state)
        print(value)
    



def main():
    
    empty_board = 5*5*"?"
    test_board = "xo?o?o?x?xo?xx???o??x?x?x"

    state = ConnectFour(test_board, True)
    play(state)

if __name__ == "__main__":
    print("Starting main.py")
    try:
        main()
    except KeyboardInterrupt:
        print("\nKeskeytetty (KeyboardInterrupt).")
    except Exception:
        import traceback
        traceback.print_exc()