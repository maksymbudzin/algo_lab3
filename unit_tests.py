import unittest
from career_algo import Algorithm

career_1 = Algorithm()
career_1.read_file('in_put/career1.in')
career_2 = Algorithm()
career_2.read_file('in_put/career2.in')
career_3 = Algorithm()
career_3.read_file('in_put/career3.in')

file_to_write1 = 'out_put/career1.out'
file_to_write2 = 'out_put/career2.out'
file_to_write3 = 'out_put/career3.out'


def write_data(file_to_write, change_data):
    file_to_write = file_to_write.replace('in_put', 'out_put')
    with open(file_to_write, 'w') as file:
        file.write(str(change_data))


experience_career_1 = career_1.get_max_experience()
write_data(file_to_write1, experience_career_1)

experience_career_2 = career_2.get_max_experience()
write_data(file_to_write2, experience_career_2)

experience_career_3 = career_3.get_max_experience()
write_data(file_to_write3, experience_career_3)


class SolutionTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(experience_career_1, 12)

    def test_2(self):
        self.assertEqual(experience_career_2, 3)

    def test_3(self):
        self.assertEqual(experience_career_3, 9999)
