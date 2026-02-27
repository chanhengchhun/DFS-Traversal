# Depth-First Search Traversal

## Key Concept
There is **no actual tree structure**. The tree exists only because:
- Node objects store **references** to other Node objects in `.left` and `.right` attributes
- Your traversal code follows those references
- You interpret the resulting chain of objects as a "tree"

When you write `root_node.left.left = Node(4)`, Python is:
1. Getting the object stored in `root_node.left` (which is `Node(2)`)
2. Accessing the `.left` attribute on that object
3. Storing a new Node reference there

There are no pointers, no memory addresses, no tree binding - just **objects referencing other objects**.

---

## Components

### Class: `Node`
Represents a single node in the binary tree.

| Attribute | Type | Description |
|-----------|------|-------------|
| `value` | any | The data stored in the node |
| `left` | Node or None | Reference to the left child node |
| `right` | Node or None | Reference to the right child node |

> **Note:** `.left` and `.right` are just variable names. Python does not enforce any "left" or "right" semantics. The tree structure is created entirely by you through manual assignment.

---

### Function: `pre_order_dfs(node, visited)`
Performs a **pre-order** depth-first search traversal on a binary tree.

**Pre-order traversal order:**
1. Visit current node first
2. Traverse left subtree
3. Traverse right subtree

**Parameters:**
- `node` (Node): The current node being visited
- `visited` (list, optional): List accumulating visited node values. Defaults to `None`.

**Returns:**
- `list`: Node values in pre-order DFS sequence

**How it works:**
1. Initialize `visited` as empty list if `None`
2. Base case: if `node is None`, return `visited`
3. Append current node's value to `visited`
4. Recursively traverse left subtree
5. Recursively traverse right subtree
6. Return `visited`

---

### Function: `main()`
Builds a sample binary tree and runs the DFS traversal.

**Tree structure built:**
```
      1        <- root_node
     / \
    2   3
   / \
  4   5
```

**Expected output:**
```
[1, 2, 4, 5, 3]
```

---

## Execution

```bash
python DFS.py
```

Output:
```
[1, 2, 4, 5, 3]
```

---

## Complexity

| Metric | Complexity |
|--------|------------|
| Time | O(n) - each node is visited once |
| Space | O(h) - recursion stack depth equals tree height |

> Worst case space is O(n) for a completely skewed tree.

---

## Potential Improvements

- Add full type hints: `node: Node | None`, `visited: list[int] | None`
- Implement **in-order** (left → root → right) and **post-order** (left → right → root) traversals
- Add an iterative DFS version using a stack to avoid hitting Python's recursion limit
- Add input validation to enforce correct node types

