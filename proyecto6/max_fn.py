import numpy as np

population_size = 12
population_gen = 2

population = np.random.randint(0,30,(population_size,population_gen))
fitness = np.zeros((population_size,3))
max_fn = np.zeros((population_size,1))
max_fn_index = np.zeros((population_size/3,1))
N = 0

while N < 5000:
    for i in range(population_size):
        x1 = population[i][0]
        x2 = population[i][1]
        if x1 + 2*x2 <= 30:
            fitness[i][0] = 1
        if x1 >= 0 and x2 >= 0:
            fitness[i][1] = 1

        max_fn[i] = 15*x1 + 30*x2 + 4*x1*x2 - 2*x1*x1 -4*x2*x2

        if max_fn[i] > 0:
            fitness[i][2] = 0.5

    print "\nPopulation until now .. \n", population

    print "\nFitness until now.. \n", fitness

    print "\nMax Fn \n", max_fn
    for n in range(len(max_fn_index)):
        index = np.argmax(max_fn)
        max_fn_index[n] = index
        max_fn[index] = 0

    print "\nIndex of the max candidates.. \n", max_fn_index

    for n in range(len(max_fn_index)):
        index = int(max_fn_index[n])
        max_k = fitness[index][2] + 0.5
        if max_k <= 1:
            fitness[index][2] += 0.5

    for n in range(len(fitness)):
        if sum(fitness[n])/3 < 0.8 or fitness[n][0] == 0 or fitness[n][1] == 0:
            population[n] = np.random.randint(0,30,(1,population_gen))

    print "\nFitness \n", fitness

    print "\nPopulation \n", population
    N += 1
