# Sean A
# Unit 1 Lab 2
# Create a graph that shows the grwoth of rats over their generations

import matplotlib.pyplot as plt


def readFile(filename):
    with open(filename) as file:
        contents = file.read()
    return contents


def cleanData(string):
    return string.split("\n")


def main():
    files = ["largestRats.txt", "meanRats.txt", "smallestRats.txt"]
    for i in files:
        try:
            i = readFile(i)
        except:
            print("There was an error reading file " + i)
            print("Please check to make sure the file exists")
            print()
            continue

        i = cleanData(i)
        i = [int(size) for size in i]
        plt.plot(i)

        plt.title("Rat Growth")
        plt.xlabel("Generation")
        plt.ylabel("Weight (grams)")

        plt.legend(files)
    plt.savefig("RatGrowth.png")


if __name__ == "__main__":
    main()
