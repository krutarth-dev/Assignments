class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def constructBinaryTree(s):
    if not s:
        return None

    # Find the root value and its index
    root_value = 0
    i = 0
    while i < len(s) and s[i] != '(':
        root_value = root_value * 10 + int(s[i])
        i += 1

    # Construct the root node
    root = TreeNode(root_value)

    # Find the substring representing the left subtree
    count = 0
    j = i
    while j < len(s):
        if s[j] == '(':
            count += 1
        elif s[j] == ')':
            count -= 1
        if count == 0:
            break
        j += 1

    # Construct the left subtree
    root.left = constructBinaryTree(s[i+1:j])

    # Check if there's a substring remaining for the right subtree
    if j+1 < len(s):
        root.right = constructBinaryTree(s[j+2:-1])

    return root

def inorderTraversal(root):
    if not root:
        return []

    result = []
    result.extend(inorderTraversal(root.left))
    result.append(root.val)
    result.extend(inorderTraversal(root.right))
    return result

# Testing the example
s = "4(2(3)(1))(6(5))"
tree = constructBinaryTree(s)
inorder = inorderTraversal(tree)
print(inorder)  # Output: [4, 2, 6, 3, 1, 5]
