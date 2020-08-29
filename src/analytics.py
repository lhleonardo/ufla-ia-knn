from knn import Instance
from knn import Knn

import csv
import random


def ReadFile(filename):
    # Monta a matriz de dados
    dataset = []
    file = csv.reader(open(filename, "r"))

    categories = []

    for row in file:
        category = row[-1]
        if len(row) != 0:
            params = []
            for i in range(len(row)-1):
                params.append(float(row[i]))
            instance = Instance(params=params, category=category)
            dataset.append(instance)

            if not category in categories:
                categories.append(category)

    return (dataset, categories)


def GenerateCustomDataset(filepath, percentage=0.2):
    dataset, categories = ReadFile(filepath)
    test_data = []
    training_data = []
    # Constroi a base de dados:
    for instance in dataset:
        if random.random() < percentage:
            test_data.append(instance)
        else:
            training_data.append(instance)

    return (test_data, training_data, categories)


def __accuracy(matrix, length):
    correct_predict_count = 0

    for index in range(len(matrix)):
        correct_predict_count += matrix[index][index]

    correct_accuracy = (correct_predict_count*100) / length
    fault_accurency = 100 - correct_accuracy

    return (correct_accuracy, fault_accurency)


def analyze(k, filepath):
    test_data, training_data, categories = GenerateCustomDataset(
        filepath=filepath)

    predicted_data = []

    knn = Knn(training_data)

    matrix = [[0 for i in range(len(categories))]
              for i in range(len(categories))]

    for instance in test_data:
        result = knn.predict(instance, k)

        result_index = categories.index(result)
        category_index = categories.index(instance.category)

        matrix[result_index][category_index] += 1

        predicted_data.append(
            Instance(params=instance.params, category=result))

    correct_accuracy, fault_accurency = __accuracy(matrix, len(test_data))
    return (matrix, correct_accuracy, fault_accurency)
