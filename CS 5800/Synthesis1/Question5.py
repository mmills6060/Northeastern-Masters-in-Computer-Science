def diameter(T):
  heights = {}
  def get_height(node):
    if node is None:
      return 0
    else:
      heights[node] = max(get_height(node.left),
                           get_height(node.right)) + 1
    return heights[node]

  for node in T.nodes:
    get_height(node)

  diameter = 0
  for node in T.nodes:
    left_height = heights[node.left] if node.left is not None else 0
    right_height = heights[node.right] if node.right is not None else 0
    diameter = max(diameter, left_height + right_height + 1)
  return diameter