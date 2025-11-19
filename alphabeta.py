"""Module contains AlphaBetaNode class and ConnectFour class that implements it,
as well as the alpha-beta pruning algorithm functions. Time-out handling with a 
simple fallback to check obvious winning and blocking moves"""

import time

class AlphaBetaNode(object):
    def __init__(self):
        pass

    def generate_children(self):
        pass

    def is_max_node(self):
        pass

    def is_end_state(self):
        pass

    def value(self):
        pass



class ConnectFour(AlphaBetaNode):
    """Class contains current state of the game and implements AlphaBetaNode methods
    :attr state: Current state of the board (str), is it crosses turn (Boolean)
    """

    def __init__(self, state, crosses_turn):
        super().__init__()
        self.state = state
        self.crosses_turn = crosses_turn

    def is_end_state(self):
        return ('?' not in self.state) or self.won('x') or self.won('o')

    def won(self, c):
        board_size = 5
        win_length = 4
        board = self.state
        lines = []

        # Rows
        for row in range(board_size):
            for col in range(board_size - win_length + 1):
                start = row * board_size + col
                line = board[start:start + win_length]
                lines.append(line)

        # columns
        for col in range(board_size):
            for row in range(board_size - win_length + 1):
                line = ''
                for i in range(win_length):
                    line += board[(row + i) * board_size + col]
                lines.append(line)

        # diagonal right (↘)
        for row in range(board_size - win_length + 1):
            for col in range(board_size - win_length + 1):
                line = ''
                for i in range(win_length):
                    line += board[(row + i) * board_size + (col + i)]
                lines.append(line)

        # diagonal left (↙)
        for row in range(board_size - win_length + 1):
            for col in range(win_length - 1, board_size):
                line = ''
                for i in range(win_length):
                    line += board[(row + i) * board_size + (col - i)]
                lines.append(line)

        return c * win_length in lines

    def __str__(self):
        board_size = 5
        output = ''
        for i in range(board_size):
            row = self.state[i * board_size:(i + 1) * board_size]
            output += '|' + '|'.join(row) + '|\n'
        return output

    def is_max_node(self):
        return bool(self.crosses_turn)

    def generate_children(self):
        """
        Generates list of all possible states after this turn
        :return: list of ConnectFour objects
        """
        lapset = []
        if self.crosses_turn:
            merkki = 'x'
        else:
            merkki = 'o'
        
        seuraava_vuoro = not self.crosses_turn

        for i, char in enumerate(self.state):
                if char == '?':
                    # Manhattan distance from center (index 12 = row 2, column 2)
                    r, c = divmod(i, 5)
                    distance = abs(r - 2) + abs(c - 2)
                    
                    tilanne = self.state[:i] + merkki + self.state[i+1:]
                    child = ConnectFour(tilanne, seuraava_vuoro)
                    lapset.append((distance, child))
    
        # sorts children by distance to center
        lapset.sort(key=lambda x: x[0])
        return [move[1] for move in lapset]

    """
    original version

        for i, char in enumerate(self.state):
            if char == '?':
                tilanne = self.state[:i] + merkki + self.state[i+1:]
                lapset.append(ConnectFour(tilanne, seuraava_vuoro))
        return lapset
    """
    def value(self):
        """
        Current score of the game (0, 1, -1)
        :return: int
        """
        if self.is_end_state():
            if self.won('o'):
                return -1
            elif self.won('x'):
                return 1
            else:
                return 0

""" Global variables for timeouts and tracking search stats"""
search_start_time = 0
max_search_time = 0
timeout_occurred = False

nodes_visited = 0
nodes_pruned = 0

def check_timeout():
    """Function to check if search time exceeded"""
    global timeout_occurred
    if time.time() - search_start_time > max_search_time:
        timeout_occurred = True
        raise TimeoutError("Search timeout")


def max_value(node, alpha, beta):
    """
    Returns (value, best_child_state) for maximizing player (x).
    """
    global nodes_visited, nodes_pruned
    
    check_timeout()
    
    if node.is_end_state():
        nodes_visited += 1
        return node.value(), node
    v = -float('inf')
    best_state = None
    for child in node.generate_children():
        try:
            val, _ = min_value(child, alpha, beta)
            if val > v:
                v = val
                best_state = child
            alpha = max(alpha, v)
            if alpha >= beta:
                nodes_pruned += 1
                break  # beta-cutoff
            
        except TimeoutError:
            # In case of timeout, return the best found so far or the most central possible move
            if best_state is None and node.generate_children():
                best_state = node.generate_children()[0]
            break
    return v, best_state

def min_value(node, alpha, beta):
    """
    Returns (value, best_child_state) for minimizing player (o).
    """
    global nodes_visited, nodes_pruned

    check_timeout()

    if node.is_end_state():
        nodes_visited += 1
        return node.value(), node
    v = float('inf')
    best_state = None
    for child in node.generate_children():
        try:
            val, _ = max_value(child, alpha, beta)
            if val < v:
                v = val
                best_state = child
            beta = min(beta, v)
            if beta <= alpha:
                nodes_pruned += 1
                break  # alpha-cutoff
            
        except TimeoutError:
            # In case of timeout, return the best found so far or the most central possible move 
            if best_state is None and node.generate_children():
                best_state = node.generate_children()[0]
            break   
    return v, best_state

def timeout_fallback(node):
    """Fast analysis in case of time-out. Spots obvious winning and blocking moves"""
    marker = 'x' if node.crosses_turn else 'o'
    opponent = 'o' if node.crosses_turn else 'x'
    next_turn = not node.crosses_turn

    # 1. Check for immediate winning moves
    for i, char in enumerate(node.state):
        if char == '?':
            test_state = node.state[:i] + marker + node.state[i+1:]
            test_child = ConnectFour(test_state, next_turn)
            if test_child.won(marker):
                print("Timeout fallback found the winning move!")
                return test_child
    # 2. Check for blocking opponent's winning moves
    for i, char in enumerate(node.state):
        if char == '?':
            # Test if opponent would win at this position
            opponent_test_state = node.state[:i] + opponent + node.state[i+1:]
            opponent_test_child = ConnectFour(opponent_test_state, node.crosses_turn)
            if opponent_test_child.won(opponent):
                # Block the opponent by playing there ourselves
                print("Timeout fallback: Blocking opponent's winning move!")
                blocking_state = node.state[:i] + marker + node.state[i+1:]
                return ConnectFour(blocking_state, next_turn)
    # 3. return none, if none found
    print("no obvious moves in depth 2")
    return None



def alpha_beta_value(node, timeout=3.0, alpha=-float('inf'), beta=float('inf')):
    """
    Wrapper: returns (value, best_child_state) depending on whose turn it is.
    """
    global search_start_time, max_search_time, timeout_occurred, nodes_visited, nodes_pruned

    search_start_time = time.time()
    max_search_time = timeout
    timeout_occurred = False

    nodes_visited = 0
    nodes_pruned = 0

    if node.is_max_node():
        result = max_value(node, alpha, beta)
    else:
        result = min_value(node, alpha, beta)
    
    if timeout_occurred:
        print("Timeout occurred - checking for tactical moves")
        tactical_move = timeout_fallback(node)
        if tactical_move:
            result = (0, tactical_move)  # Use obvious move
        else:
            # Use whatever alpha-beta found before timeout or the first move in list
            value, best_state = result
            if best_state is None:
                children = node.generate_children()
                result = (0, children[0] if children else node)
    
    elapsed_time = time.time() - search_start_time
    status = " (timed out)" if timeout_occurred else ""
    print(f"AlphaBeta stats - nodes_visited: {nodes_visited}, nodes_pruned: {nodes_pruned}, time: {elapsed_time:.2f}s{status}")
    return result