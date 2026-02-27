import unittest
import DFS

class TestDFS(unittest.TestCase):
    root = DFS.Node('A')
    root.left = DFS.Node('B')
    root.right = DFS.Node('C')
    root.left.left = DFS.Node('D')
    root.left.right = DFS.Node('E')
    result = DFS.dfs(root)

    def test_preorder_dfs(self):
        self.assertEqual(TestDFS.result, ['A', 'B', 'D', 'E', 'C'])

if __name__ == '__main__':
    unittest.main()