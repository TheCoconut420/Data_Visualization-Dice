import matplotlib.pyplot as plt

class Visualization:
    def visualize(self, data):
        labels = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        title = "Dice roll results"
        plt.bar(labels, data)
        plt.title(title)
        plt.show()