# Sean A
# Unit 1 Lab 2
# Create a graph that shows the grwoth of rats over their generations

import matplotlib.pyplot as plt


def readFile(filename):
    with open(filename) as file:
        contents = file.read()
    return contents


def cleanData(data):
    cleanedData = [int(weight) for weight in data.split('\n')]
    return cleanedData


def main():
    files = ["largestRats.txt", "meanRats.txt", "smallestRats.txt"]
    outputFile = "RatGrowth.png"
    print(f"Creating a graph using {', '.join(files)}...")
    for i in files:
        try:
            i = readFile(i)
        except:
            print("There was an error reading file " + i)
            print("Please check to make sure the file exists")
            print()
            continue

        i = cleanData(i)
        plt.plot(i)

        plt.title("Rat Growth")
        plt.xlabel("Generation")
        plt.ylabel("Weight (grams)")

        plt.legend(files)
    plt.savefig(outputFile)

    print(f"Done! Ouputted results into {outputFile}")


if __name__ == "__main__":
    main()
