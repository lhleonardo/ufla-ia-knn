class Instance:
    def __init__(self, params, category):
        self.params = params
        self.category = category

    def distance(self, another):
        result = 0
        for i in range(len(self.params)):
            result += (self.params[i] - another.params[i]) ** 2

        return result


class Knn:
    def __init__(self, data):
        self.data = data

    def __distance(self, unknown):
        neighbours = []

        for element in self.data:
            neighbours.append((element, element.distance(unknown)))

        return sorted(neighbours, key=lambda element: element[1])

    def predict(self, unkown, k):

        # Cria a matriz de k vizinhos mais proximos
        neighbours = self.__distance(unkown)

        category_count = {}
        for i in range(k):
            instance, _ = neighbours[i]
            if instance.category in category_count:
                category_count[instance.category] += 1
            else:
                category_count[instance.category] = 1

        possible_category = None

        for category in category_count.keys():
            if possible_category is None:
                possible_category = category
            elif category_count[category] > category_count[possible_category]:
                possible_category = category

        return possible_category
