# the same problem solved with binary tree
# it is intended to reduce the processing time


class connected_points:
  def __init__(self, size):
    self.connections = [i for i in range(size)]

  def is_connected(a, b):
    return self.connections[a] == self.connections[b]

  def root(i):
    value = self.connections[i]
    while value != i:
      value = self.connections[value]
    return value

  def union(a, b):
    rootA = root(a)
    rootB = root(b)

    self.connections[a] = b