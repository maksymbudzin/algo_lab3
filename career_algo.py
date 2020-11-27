import csv


class Algorithm:
    def __init__(self):
        self.number_of_company_levels = 0
        self.experience_for_position = []

    def read_file(self, filename):
        with open(filename) as data:
            csv_reader = csv.reader(data, delimiter=" ")
            next(csv_reader)
            for row in csv_reader:
                self.experience_for_position.append(list(map(lambda x: int(x), row)))
            self.number_of_company_levels = len(self.experience_for_position)

    def get_max_experience(self):
        for layer in range(self.number_of_company_levels - 2, -1, -1):
            for element in range(layer + 1):
                self.get_the_longest_career_path(layer, element)
        return self.experience_for_position[0][0]

    def get_the_longest_career_path(self, layer, element):
        current_left = self.experience_for_position[layer + 1][element]
        curent_right = self.experience_for_position[layer + 1][element + 1]
        if current_left > curent_right:
            self.experience_for_position[layer][element] += current_left
        else:
            self.experience_for_position[layer][element] += curent_right
