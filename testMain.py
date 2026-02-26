import unittest
import main

class TestDFS(unittest.TestCase):
    root = main.Node('A')
    root.left = main.Node('B')
    root.right = main.Node('C')
    root.left.left = main.Node('D')
    root.left.right = main.Node('E')
    result = main.dfs(root)

    def test_preorder_dfs(self):
        self.assertEqual(TestDFS.result, ['A', 'B', 'D', 'E', 'C'])

if __name__ == '__main__':
    unittest.main()