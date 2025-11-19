from alphabeta import ConnectFour, alpha_beta_value

"""
    play(state): makes turn and prints the result of it until the game is over
    value() in ConnectFour class: returns the current score of the game (0 for draw, 1 for x win, -1 for o win)
    generate_children() in ConnectFour class: returns a list of all possible states after this turn
    alpha_beta_value(node): implements the MinMax algorithm with alpha-beta pruning
    max_value(node, alpha, beta): implements the MinMax algorithm with alpha-beta pruning
    min_value(node, alpha, beta):implements the MinMax algorithm with alpha-beta pruning
    
    nextmove(state): determines the next move for the current player and prints it with stats
    for visited nodes and pruned nodes.


    currently main tests the tictactoe with a hard-coded test board. Future plans include adding
    a heuristic evaluation for non-terminal states and using a depth limit for the search.
    
    """


def play(state):
    """Makes turn and prints the result of it until the game is over
    :param state: The initial state of the game
    """
    print(state)
    if state.state == 5*5*"?":
        middlefirst = state.state[:12] + 'x' + state.state[13:]
        state = ConnectFour(middlefirst, False)
        print(state)
    
    while not state.is_end_state():
        state, value = nextmove(state)
        print(state)
        print(value)
    

def nextmove(state, timeout=5.0):
    """Determines the next move for the current player."""
    alpha = -float('inf')
    beta = float('inf')
    value, new_state = alpha_beta_value(state, timeout=timeout, alpha=alpha, beta=beta)
    return new_state, value

def main():
    
    empty_board = 5*5*"?"
    test_board = "??x??x?xo??oxx??xo?ox?oxo"
    state = ConnectFour(test_board, True)
    """
    print("\nNext move:\n")
    (newstate, newvalue) = nextmove(state)
    print(newstate, newvalue)
    """

    play(state)


if __name__ == "__main__":
    print("Starting main.py")
    try:
        main()
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt")
    except Exception:
        import traceback
        traceback.print_exc()

"""


    "
    oxx??
    oox0?
    ?oxx?
    ?xo?o
    ??xx?
    "



"""