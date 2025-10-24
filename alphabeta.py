"""Module contains AlphaBetaNode class and ConnectFour class that implements it,
as well as the alpha-beta pruning algorithm functions."""



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

        # Rivit
        for row in range(board_size):
            for col in range(board_size - win_length + 1):
                start = row * board_size + col
                line = board[start:start + win_length]
                lines.append(line)

        # Sarakkeet
        for col in range(board_size):
            for row in range(board_size - win_length + 1):
                line = ''
                for i in range(win_length):
                    line += board[(row + i) * board_size + col]
                lines.append(line)

        # Vinot oikealle (↘)
        for row in range(board_size - win_length + 1):
            for col in range(board_size - win_length + 1):
                line = ''
                for i in range(win_length):
                    line += board[(row + i) * board_size + (col + i)]
                lines.append(line)

        # Vinot vasemmalle (↙)
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
                tilanne = self.state[:i] + merkki + self.state[i+1:]
                lapset.append(ConnectFour(tilanne, seuraava_vuoro))
        return lapset

    def value(self):
        """
        Current score of the game (0, 1, -1)
        :return: int
        """
        # Implement me
        if self.is_end_state():
            if self.won('o'):
                return -1
            elif self.won('x'):
                return 1
            else:
                return 0
        
def max_value(node, alpha, beta):
    """
    Returns (value, best_child_state) for maximizing player (x).
    """
    if node.is_end_state():
        return node.value(), node
    v = -float('inf')
    best_state = None
    for child in node.generate_children():
        val, _ = min_value(child, alpha, beta)
        if val > v:
            v = val
            best_state = child
        alpha = max(alpha, v)
        if alpha >= beta:
            break  # beta-cutoff
    return v, best_state

def min_value(node, alpha, beta):
    """
    Returns (value, best_child_state) for minimizing player (o).
    """
    if node.is_end_state():
        return node.value(), node
    v = float('inf')
    best_state = None
    for child in node.generate_children():
        val, _ = max_value(child, alpha, beta)
        if val < v:
            v = val
            best_state = child
        beta = min(beta, v)
        if beta <= alpha:
            break  # alpha-cutoff
    return v, best_state

def alpha_beta_value(node, alpha=-float('inf'), beta=float('inf')):
    """
    Wrapper: returns (value, best_child_state) depending on whose turn it is.
    """
    if node.is_max_node():
        return max_value(node, alpha, beta)
    else:
        return min_value(node, alpha, beta)