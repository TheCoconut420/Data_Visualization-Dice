class WriteDataToFile:
    def write_data_to_file(self, result):
        file = open("dice_data.txt", "a")
        file.write(str(result)+"\n")