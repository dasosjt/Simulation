
import numpy as np

population_size = 120
population_gen = 2
max_value = 6

population = np.random.uniform(0,max_value,(population_size,population_gen))

N = 0

while N < 2000:
    fitness = np.zeros((population_size,3))
    max_fn = np.zeros((population_size,1))
    max_fn_index = np.zeros((population_size/3,1))

    for i in range(population_size):
        x1 = population[i][0]
        x2 = population[i][1]

        if (3*x1 + 2*x2) <= 6:
            fitness[i][0] = 1

        if x1 >= 0 and x2 >= 0:
            fitness[i][1] = 1

        max_fn[i] = 5*x1 -x1*x1 + 8*x2 - 2*x2*x2

        if max_fn[i] > 0:
            fitness[i][2] = 0.5

    #print "\nPopulation until now .. \n", population

    #print "\nFitness until now.. \n", fitness

    #print "\nMax Fn \n", max_fn
    for n in range(len(max_fn_index)):
        index = np.argmax(max_fn)
        max_fn_index[n] = index
        max_fn[index] = 0

    #print "\nIndex of the max candidates.. \n", max_fn_index

    for n in range(len(max_fn_index)):
        index = int(max_fn_index[n])
        max_k = fitness[index][2] + 0.5
        if max_k <= 1:
            fitness[index][2] += 0.5

    #print "\n New Fitness \n", fitness

    #print "\nCrossover \n"
    for n in range(len(fitness)):
        if sum(fitness[n])/3 < 0.8 or fitness[n][0] == 0 or fitness[n][1] == 0 or fitness[n][2] == 0.5:
            cross_over0 = np.random.randint(0,population_size/3, 1)
            cross_over1 = np.random.randint(0,population_size/3, 1)
            mutation = np.random.randint(0,2,1)
            new_fen = np.random.randint(0,2,1)
            if new_fen == 1:
                gen0 = np.random.uniform(0,max_value,1)
                gen1 = np.random.uniform(0,max_value,1)
                #print ("Fen number {} with [{}, {}].. and new Fen".format(n, gen0, gen1))
                population[n][0] = gen0
                population[n][1] = gen1
            else:
                if mutation == 1:
                    mut0 = np.random.uniform(-max_value,max_value,1)
                    mut1 = np.random.uniform(-max_value,max_value,1)
                    #print ("Fen number {} with [{}, {}].. and Mutation ".format(n, population[int(max_fn_index[cross_over0])][0]+mut0, population[int(max_fn_index[cross_over1])][1]+mut1))
                    population[n][0] = population[int(max_fn_index[cross_over0])][0]+mut0
                    population[n][1] = population[int(max_fn_index[cross_over1])][1]+mut1
                elif mutation == 0:
                    #print ("Fen number {} with [{}, {}]".format(n, population[int(max_fn_index[cross_over0])][0], population[int(max_fn_index[cross_over1])][1]))
                    population[n][0] = population[int(max_fn_index[cross_over0])][0]
                    population[n][1] = population[int(max_fn_index[cross_over1])][1]

    #print "\nPopulation \n", population
    N += 1
#print "\nIndex of the max candidates.. \n", max_fn_index
#print "\nFitness \n", fitness
#print "\nPopulation \n", population
c = 0
found = False
while not found:
    max_candidate_index = int(max_fn_index[c])
    max_candidate = population[max_candidate_index]
    if fitness[max_candidate_index][0] == 1 and fitness[max_candidate_index][1] == 1 and fitness[max_candidate_index][2] == 1:
        found = True
    else:
        c += 1
print "\nThe best candidate is \n", max_candidate
