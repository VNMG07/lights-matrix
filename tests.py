import unittest
from libs import read_write as rw
from main import light_funct, create_matrix, create_matrix_with_one

with open("input.txt") as f:
    lines = f.read().splitlines()

with open("tests.txt") as f:
    test_lines = f.read().splitlines()


class TestLights(unittest.TestCase):

    def test_input_file_start_with_toggle_or_turn(self):
        for line in lines:
            commands = line.split(" ")  # get every command on the line
            if commands[0] != 'toggle':
                self.assertEqual(commands[0], 'turn')
            elif commands[0] != 'turn':
                self.assertEqual(commands[0], 'toggle')

    def test_file_contains_off(self):
        line_string = ''
        for line in lines:
            line_string += ' ' + line
        self.assertIn('off', line_string)

    def test_file_contains_on(self):
        line_string = ''
        for line in lines:
            line_string += ' ' + line
        self.assertIn('on', line_string)

    def test_file_contains_toggle(self):
        line_string = ''
        for line in lines:
            line_string += ' ' + line
        self.assertIn('toggle', line_string)

    '''We can check just the first appearance of the command, we can't control the final output, there are cases where 
    the lights are turned off/on or toggle from another command'''
    def test_check_off_if_0_remains_0(self):
        matrix = light_funct()
        matrix_with_zeroes = create_matrix(1000, 1000)
        for line in lines:
            commands = line.split(" ")
            pos = commands[-1].split(',')
            value_from_zero_matrix = matrix_with_zeroes[int(pos[0])][int(pos[1])]
            value_from_matrix = matrix[int(pos[0])][int(pos[1])]
            if commands[1] == 'off' and value_from_matrix == 0:
                self.assertEqual(value_from_matrix, value_from_zero_matrix)
                break

    def test_check_on_if_it_changes_0_to_1(self):
        matrix = light_funct()
        matrix_with_zeroes = create_matrix(1000, 1000)
        for line in lines:
            commands = line.split(" ")
            pos = commands[-1].split(',')
            value_from_zero_matrix = matrix_with_zeroes[int(pos[0])][int(pos[1])]
            value_from_matrix = matrix[int(pos[0])][int(pos[1])]
            if commands[1] == 'on':
                self.assertNotEqual(value_from_zero_matrix, value_from_matrix)
                break

    def test_check_toggle_if_it_changes_0_to_1(self):
        matrix = light_funct()
        matrix_with_zeroes = create_matrix(1000, 1000)
        for line in lines:
            commands = line.split(" ")
            pos = commands[-1].split(',')
            value_from_zero_matrix = matrix_with_zeroes[int(pos[0])][int(pos[1])]
            value_from_matrix = matrix[int(pos[0])][int(pos[1])]
            if commands[0] == 'toggle' and value_from_matrix != 0:
                self.assertNotEqual(value_from_zero_matrix, value_from_matrix)
                # we can do the same for the case 1 to 0, but we need another create_matrix function

    '''Next 3 tests are used to check the opposite case where you have a matrix with 1 everywhere'''
    # def test_check_off_if_it_changes_1_to_0(self):
    #     matrix = light_funct()
    #     matrix_with_ones = create_matrix_with_one(1000, 1000)
    #     for line in lines:
    #         commands = line.split(" ")
    #         pos = commands[-1].split(',')
    #         value_from_one_matrix = matrix_with_ones[int(pos[0])][int(pos[1])]
    #         value_from_matrix = matrix[int(pos[0])][int(pos[1])]
    #         if commands[1] == 'off':
    #             self.assertNotEqual(value_from_matrix, value_from_one_matrix)
    #             break
    #
    # def test_check_on_if_1_remains_1(self):
    #     matrix = light_funct()
    #     matrix_with_ones = create_matrix_with_one(1000, 1000)
    #     for line in lines:
    #         commands = line.split(" ")
    #         pos = commands[-1].split(',')
    #         value_from_one_matrix = matrix_with_ones[int(pos[0])][int(pos[1])]
    #         value_from_matrix = matrix[int(pos[0])][int(pos[1])]
    #         if commands[1] == 'on' and value_from_matrix == 1:
    #             self.assertEqual(value_from_matrix, value_from_one_matrix)
    #             break
    #
    # def test_check_toggle_if_it_changes_1_to_0(self):
    #     matrix = light_funct()
    #     matrix_with_ones = create_matrix_with_one(1000, 1000)
    #     for line in lines:
    #         commands = line.split(" ")
    #         pos = commands[-1].split(',')
    #         value_from_one_matrix = matrix_with_ones[int(pos[0])][int(pos[1])]
    #         value_from_matrix = matrix[int(pos[0])][int(pos[1])]
    #         if commands[0] == 'toggle' and value_from_matrix != 1:
    #             self.assertNotEqual(value_from_one_matrix, value_from_matrix)

    def test_if_index_has_correct_format(self):
        line_string = ''
        for line in lines:
            line_string += ' ' + line
        self.assertRegex(line_string, "([0-9]|[1-9][0-9]|[1-9][0-9][0-9]),([0-9]|[1-9][0-9]|[1-9][0-9][0-9]) "
                                          "through ([0-9]|[1-9][0-9]|[1-9][0-9][0-9]),"
                                          "([0-9]|[1-9][0-9]|[1-9][0-9][0-9])")

    def test_if_coord_make_a_rectangle(self):
        for line in lines:
            commands = line.split(" ")
            line_start, column_start = commands[-3].split(",")
            line_end, column_end = commands[-1].split(",")
            self.assertGreaterEqual(int(line_end), int(line_start))
            self.assertGreaterEqual(int(column_end), int(column_start))

    def test_if_data_is_in_range(self):
        for line in lines:
            commands = line.split(" ")
            line_start, column_start = commands[-3].split(",")
            line_end, column_end = commands[-1].split(",")
            self.assertGreaterEqual(int(line_end), 0)
            self.assertLessEqual(int(line_end), 999)
            self.assertGreaterEqual(int(column_end), 0)
            self.assertLessEqual(int(column_end), 999)
            self.assertGreaterEqual(int(line_start), 0)
            self.assertLessEqual(int(line_start), 999)
            self.assertGreaterEqual(int(column_start), 0)
            self.assertLessEqual(int(column_start), 999)
