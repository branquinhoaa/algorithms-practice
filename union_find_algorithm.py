# create a class with 2 methods: union and find
# this class will implement the connected component that
# will say if two components are conected or not between them
# to solve it, the array is instantiated with unique numbers and each 
# union operation we will change the value of the connected points for the same value

class connected_component:

  def __init__(self, id_size):
    self.connections = [i for i in range(id_size)]

  def is_connected(point_a, point_b):
    return connections[point_a] == connections[point_b]

  def union(point_a, point_b):
    a = self.connections[point_a]
    b = self.connections[point_b]

    for i in range(len(self.connections)):
        if(self.connections[i] == a):
          self.connections[i]=b

