import unittest
from libs import read_write as rw
from main import light_funct

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

    ''' for the next 3 tests you need to be sure the lights will not 
    turn on/off after you find first line where they appear'''
    def test_check_off(self):
        matrix = light_funct()
        for line in lines:
            commands = line.split(" ")
            pos = commands[-1].split(',')
            position_before = matrix[int(pos[0])][int(pos[1])]
            if commands[1] == 'off' and position_before == 0:
                self.assertEqual(position_before, matrix[int(pos[0])][int(pos[1])])
                break
            elif commands[1] == 'off' and position_before == 1:
                self.assertNotEqual(position_before, matrix[int(pos[0])][int(pos[1])])
                break

    def test_check_on(self):
        matrix = light_funct()
        for line in lines:
            commands = line.split(" ")
            pos = commands[-1].split(',')
            position_before = matrix[int(pos[0])][int(pos[1])]
            if commands[1] == 'on' and position_before == 1:
                self.assertEqual(position_before, matrix[int(pos[0])][int(pos[1])])
                break
            elif commands[1] == 'on' and position_before == 0:
                self.assertNotEqual(position_before, matrix[int(pos[0])][int(pos[1])])
                break

    def test_check_toggle(self):
        matrix = light_funct()
        for line in lines:
            commands = line.split(" ")
            pos = commands[-1].split(',')
            position_before = matrix[int(pos[0])][int(pos[1])]
            if commands[0] == 'toggle':
                self.assertNotEqual(position_before, matrix[int(pos[0])][int(pos[1])])
                break


    def test_if_index_has_corect_format(self):
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


