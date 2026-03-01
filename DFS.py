class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder_dfs(node: Node, visited=None):
    """
    Pre-order depth-first search (DFS) algorithm for binary tree traversal using recursion.
    Args:
        node: current node (structure from Node class)
        visited: visited nodes

    Returns: visited nodes

    """
    if visited is None:
        visited: list = []
    # return if tree doesn't exist
    if node is None:
        return visited

    visited.append(node.value)
    preorder_dfs(node.left, visited)  # explore left branch
    preorder_dfs(node.right, visited)  # explore right branch

    return visited

def main():
    root_node = Node(1)
    root_node.left = Node(2)
    root_node.left.left = Node(4)
    root_node.left.right = Node(5)
    root_node.right = Node(3)

    #print(preorder_dfs(root_node))
    print(preorder_dfs(root_node))

if __name__ == "__main__":
    main()
