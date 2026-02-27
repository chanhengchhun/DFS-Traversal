class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def dfs(node, visited_list=None):
    if visited_list is None:
        visited_list = []
    # return if tree doesn't exist
    if node is None:
        return visited_list

    visited_list.append(node.val)
    dfs(node.left, visited_list) # 3 explore left branch
    dfs(node.right, visited_list) # 4 explore right branch

    return visited_list
