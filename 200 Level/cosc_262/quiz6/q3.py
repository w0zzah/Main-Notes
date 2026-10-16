from collections import namedtuple
Node = namedtuple("Node", ["value", "left", "right"])

def binary_search_tree(nums, is_sorted=False, start=0, end=None):
    if not is_sorted:
        nums = sorted(nums)
    if end is None:
        end = len(nums)
    
    n = end - start
    if n == 1:
        tree = Node(nums[start], None, None)
    else:
        mid = start + n // 2
        left = binary_search_tree(nums, True, start, mid)
        right = binary_search_tree(nums, True, mid, end)
        tree = Node(nums[mid - 1], left, right)
    return tree

def print_tree(tree, level=0):
    """Print the tree with indentation"""
    if tree.left is None and tree.right is None:
        print(2 * level * ' ' + f"Leaf({tree.value})")
    else:
        print(2 * level * ' ' + f"Node({tree.value})")
        print_tree(tree.left, level + 1)
        print_tree(tree.right, level + 1)

def count_nodes(tree):
    if tree is None:
        return 0
    return 1 + count_nodes(tree.left) + count_nodes(tree.right)

def count_leaves_at_level(tree, level=0):
    if tree is None:
        return {}
    if tree.left is None and tree.right is None:
        return {level: 1}
    result = {}
    for d, count in {**count_leaves_at_level(tree.left, level+1), 
                     **count_leaves_at_level(tree.right, level+1)}.items():
        result[d] = result.get(d, 0) + count
    return result

nums = [15, 3, 11, 21, 7, 0, 19, 33, 29, 4]
tree = binary_search_tree(nums)

print("Tree structure:")
print_tree(tree)
print(f"\nTotal nodes: {count_nodes(tree)}")
print(f"Leaves by level: {count_leaves_at_level(tree)}")