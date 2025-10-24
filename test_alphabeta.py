import unittest
from alphabeta import ConnectFour

"""Unit tests for ConnectFour class methods."""

class TestConnectFour(unittest.TestCase):
    def test_won_horizontal(self):
        state = 'xxxx?' + ('?' * 20)
        node = ConnectFour(state, False)
        self.assertTrue(node.won('x'))

    def test_won_vertical(self):
        lst = ['?'] * 25
        for idx in (0, 5, 10, 15):  # kolumni 0, rivit 0-3
            lst[idx] = 'o'
        node = ConnectFour(''.join(lst), False)
        self.assertTrue(node.won('o'))

    def test_won_diagonal_right(self):
        lst = ['?'] * 25
        for idx in (0, 6, 12, 18):  # diag ↘ (r0c0, r1c1, r2c2, r3c3)
            lst[idx] = 'x'
        node = ConnectFour(''.join(lst), True)
        self.assertTrue(node.won('x'))

    def test_won_diagonal_left(self):
        lst = ['?'] * 25
        for idx in (3, 7, 11, 15):  # diag ↙ (r0c3, r1c2, r2c1, r3c0)
            lst[idx] = 'o'
        node = ConnectFour(''.join(lst), False)
        self.assertTrue(node.won('o'))

    def test_generate_children_count_and_turn(self):
        node = ConnectFour('?' * 25, True)
        children = node.generate_children()
        self.assertEqual(len(children), 25)
        # varmista että ensimmäinen lapsi sisältää 'x' ja vuoro vaihtuu
        self.assertIn('x', children[0].state)
        self.assertFalse(children[0].crosses_turn)

    def test_is_end_state_and_value(self):
        # x wins
        state = 'xxxx?' + ('?' * 20)
        node = ConnectFour(state, False)
        self.assertTrue(node.is_end_state())
        self.assertEqual(node.value(), 1)

        # o wins
        lst = ['?'] * 25
        for idx in (1, 6, 11, 16):
            lst[idx] = 'o'
        node2 = ConnectFour(''.join(lst), True)
        self.assertTrue(node2.is_end_state())
        self.assertEqual(node2.value(), -1)

        # draw / not win but full board
        full = "xoxoxxoxoxoxoxooxoxoxoxox"
        node3 = ConnectFour(full, True)
        self.assertTrue(node3.is_end_state())
        self.assertEqual(node3.value(), 0)

if __name__ == '__main__':
    unittest.main()