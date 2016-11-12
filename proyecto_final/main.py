import numpy as np

nodes = 5

print "Number of Nodes ", nodes

population = np.random.randint(-100,100,(2, nodes*nodes))
population = np.multiply(population, 0.01)

half_fenothype = lambda x: x[0:len(x)/2] if np.random.randint(0,2) else x[len(x)/2:len(x)]
crossover_by_half = lambda x,y: np.append(half_fenothype(x), half_fenothype(y))

fenothype_as_vector0 = population[0]
fenothype_as_vector1 = population[1]

print "Fenothypes as Vector"
print fenothype_as_vector0
print fenothype_as_vector1
print "Fenothypes crossover_by_half "
print crossover_by_half(fenothype_as_vector0, fenothype_as_vector1)


fenothype_as_matrix0 = population[0].reshape((nodes, nodes))
fenothype_as_matrix1 = population[1].reshape((nodes, nodes))

print "Fenothypes as Matrix"
print fenothype_as_matrix0
print fenothype_as_matrix1
