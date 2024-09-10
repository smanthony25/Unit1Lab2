# Sean A
# Unit 1 Lab 1
# Create a rat breeding system that aims to create a large rat

import random as r
import time as t

from ratinator import Rat

GOAL = 50000  # Target average weight (grams)
NUM_RATS = 20  # Max adult rats in the lab
INITIAL_MIN_WT = 200  # The smallest rat (grams)
INITIAL_MAX_WT = 600  # The chonkiest rat (grams)
INITIAL_MODE_WT = 300  # The most common weight (grams)
MUTATE_ODDS = 0.01  # Liklihood of a mutation
MUTATE_MIN = 0.5  # Scalar mutation - least beneficial
MUTATE_MAX = 1.2  # Scalar mutation - most beneficial
LITTER_SIZE = 8  # Pups per litter (1 mating pair)
GENERATIONS_PER_YEAR = 10  # How many generations are created each year
GENERATION_LIMIT = 500  # Generational cutoff - stop breeded no matter what


def calculate_weight(sex, mother, father):
    """Generate the weight of a single rat"""

    # Use the triangular function from the random library to skew the
    # baby's weight based on its sex
    min = mother.getWeight()
    max = father.getWeight()
    if sex == "M":
        wt = int(r.triangular(min, max, max))
    else:
        wt = int(r.triangular(min, max, min))
    return wt


def initial_population():
    """Create the initial set of rats based on constants"""
    rats = [[], []]
    mother = Rat("F", INITIAL_MIN_WT)
    father = Rat("M", INITIAL_MAX_WT)

    for r in range(NUM_RATS):
        if r < 10:
            sex = "M"
            ind = 0
        else:
            sex = "F"
            ind = 1

        wt = calculate_weight(sex, mother, father)
        R = Rat(sex, wt)
        rats[ind].append(R)

    return rats


def mutate(pups):
    """Check for mutability, modify weight of affected pups"""
    for a in pups:
        for i in a:
            randomNum = r.random()
            if randomNum <= MUTATE_ODDS:
                mutateAmount = r.uniform(MUTATE_MIN, MUTATE_MAX)
                i.mutuate(mutateAmount)
    return pups


def breed(rats):
    """Create mating pairs, create LITTER_SIZE children per pair"""
 `  1q23w   children = [[], []]
    sexes = ["M", "F"]
    r.shuffle(rats[0])
    r.shuffle(rats[1])
    for x, mother in enumerate(rats[0]):
        father = rats[1][x]
        father.litters += 1
        mother.litters += 1
        for i in range(LITTER_SIZE):
            sex = r.choice(sexes)
            if sex == "F":
                weight = calculate_weight(sex, mother, father)
                children[0].append(Rat(sex, weight))
            else:
                weight = calculate_weight(sex, mother, father)
                children[1].append(Rat(sex, weight))

    return children


def combine_rats(rats, pups):
    for i in rats[0]:
        if not i.canBreed():
            rats[0].remove(i)
    for i in rats[1]:
        if not i.canBreed():
            rats[1].remove(i)
    rats[0].extend(pups[0])
    rats[1].extend(pups[1])
    return rats


def select(rats):
    """Choose the largest viable rats for the next round of breeding"""
    rats[0].sort(reverse=True)  # It took me way too long to realize that the sort function did it from small to large
    rats[1].sort(reverse=True)
    rats[0][:] = rats[0][:10]
    rats[1][:] = rats[1][:10]

    if rats[0][0] > rats[1][0]:
        largest = rats[0][0]
    else:
        largest = rats[1][0]

    return rats, largest


def calculate_mean(rats):
    """Calculate the mean weight of a population"""
    sumWt = sum(rats[0]) + sum(rats[1])
    mean = sumWt // NUM_RATS
    return mean


def fitness(rats):
    """Determine if the target average matches the current population's average"""
    mean = calculate_mean(rats)
    return mean >= GOAL, mean


def print_results(largest, generations, runtime, mean, means):
    years = generations / GENERATIONS_PER_YEAR
    print(" [Lab Results] ".center(60, "="))
    print()
    print(f"Final Population Mean: {mean}g")
    print()
    print(f"Generations: {generations}")
    print(f"Experiment Duration: {years} years")
    print(f"Simulation Duration: {runtime} second(s)")
    print()
    print("Largest Rat")
    print(f"Sex: {largest.getSex()}")
    print(f"Weight: {largest.getWeight()} grams")
    print()
    print(" Weight Averages (grams) ".center(89, "~"))
    for index, mean in enumerate(means):
        print(f"{mean}".ljust(5), end=" ")
        if (index + 1) % 15 == 0:
            print()
    print()


def main():
    runtime = t.time()
    largestRat = Rat("M", 0)
    reachedGoal = False
    generations = 0
    means = []
    rats = initial_population()
    rats = mutate(rats)
    while not reachedGoal and generations < GENERATION_LIMIT:
        # Create and mutate pups
        pups = breed(rats)
        pups = mutate(pups)
        # Combine and sort rats
        rats = combine_rats(rats, pups)
        # Get big chungus
        rats, largest = select(rats)
        if largestRat < largest:
            largestRat = largest
        # Get the avrg
        reachedGoal, mean = fitness(rats)
        generations += 1
        means.append(mean)
    runtime = t.time() - runtime
    runtime = round(runtime, 4)
    print_results(largestRat, generations, runtime, mean, means)


if __name__ == "__main__":
    main()
