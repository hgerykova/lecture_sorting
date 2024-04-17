import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        for row in reader:
            for key in row.keys():
                if key not in data:
                    data[key] = [int(row[key])]
                else:
                    data[key].append(int(row[key]))
    return data


def selection_sort(numbers_1):
        n = len(numbers_1)
        for i in range(n):
            number_index = i
            for j in range(i+1, n):
                if numbers_1[j] < numbers_1[number_index]:
                    number_index = j
            numbers_1[i], numbers_1[number_index] = numbers_1[number_index], numbers_1[i]
        return numbers_1






def main():
    numbers = read_data("numbers.csv")
    # print(numbers)
    numbers_1 = numbers["series_1"]
    # print(numbers_1)
    sorted_numbers = selection_sort(numbers_1)
    print(sorted_numbers)



if __name__ == '__main__':
    main()
