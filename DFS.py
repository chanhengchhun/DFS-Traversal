class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def pre_order_dfs(node: Node, visited=None):
    """
    Pre-order depth-first search (DFS) algorithm for binary tree traversal.
    Remember there is no actual tree binding in the code,
    we're just store data in variable left and right in Node class.
    we are manipulating with data structure, not with actual tree behind the scene.
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
    pre_order_dfs(node.left, visited)  # explore left branch
    pre_order_dfs(node.right, visited)  # explore right branch

    return visited

def main():
    root_node = Node(1)
    root_node.left = Node(2)
    root_node_left = root_node.left
    root_node_left.left = Node(4)
    root_node_left.right = Node(5)
    root_node.right = Node(3)


    print(pre_order_dfs(root_node))

if __name__ == "__main__":
    main()
