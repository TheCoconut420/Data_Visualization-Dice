import dice_simulator
import write_data_to_file
import process_data
import visualization


class Main():
    def __init__(self):
        self.dice_simulator = dice_simulator.Dice
        self.write_data_to_file = write_data_to_file.WriteDataToFile()
        self.process_data = process_data.ProcessData
        self.visualization = visualization.Visualization()

    def main(self):
        for i in range(100000):
            result = self.dice_simulator.roll()
            self.write_data_to_file.write_data_to_file(result)
        data = process_data.ProcessData.get_amount_of_numbers(process_data.ProcessData.process())
        self.visualization.visualize(data)

if __name__ == "__main__":
    main = Main()
    main.main()