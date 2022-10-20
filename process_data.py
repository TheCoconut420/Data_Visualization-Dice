class ProcessData:
    def process():
        data = []
        file = open("dice_data.txt", "r")
        for line in file:
            data.append(int(line))
        file.close()
        data.sort()
        return data
    
    def get_amount_of_numbers(data):
        amount_of_numbers = []
        for i in range(2, 13):
            amount_of_numbers.append(data.count(i))
        return amount_of_numbers
