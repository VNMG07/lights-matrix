from libs import read_write as rw


def create_matrix(n, m):
    return [m * [0] for i in range(n)]


def get_coordinates(line):
    coord = {}
    try:
        command = line.split(' ')
        if len(command) == 5:
            coord[command[1]] = [map(int, command[2].split(',')), map(int, command[-1].strip().split(','))]
        else:
            coord[command[0]] = [map(int, command[1].split(',')), map(int, command[-1].strip().split(','))]
        return coord
    except AttributeError as e:
        print(f'error occurred -> {e}')
        return


def get_indexes(l_start, l_end, c_start, c_end):
    indexes = []
    for i in range(int(l_start), int(l_end) + 1):
        for j in range(int(c_start), int(c_end) + 1):
                indexes.append([i, j])
    return indexes


def change_lights(matrix, coordinates):
    try:
        choices = {'on': 1, 'off': 0}
        for k, v in coordinates.items():
            line_start, column_start = v[0]
            line_end, column_end = v[1]
            indexs = get_indexes(line_start, line_end, column_start, column_end)
            for index in indexs:
                if k != 'toggle':
                    matrix[index[0]][index[1]] = choices[k]
                else:
                    matrix[index[0]][index[1]] = 0 if matrix[index[0]][index[1]] == 1 else 1
        return matrix
    except KeyError as e:
        print('not dictionary key')
    except Exception as e:
        print(f'Unexpected exception occurred! -> {e}')


def change_upgraded_lights(upgraded_matrix, coordinates):
    try:
        for k, v in coordinates.items():
            line_start, column_start = v[0]
            line_end, column_end = v[1]
            indexs = get_indexes(line_start, line_end, column_start, column_end)
            for index in indexs:
                if k != 'toggle':
                    if k == 'off' and upgraded_matrix[index[0]][index[1]] > 0:
                        upgraded_matrix[index[0]][index[1]] -= 1
                    elif k == 'off' and upgraded_matrix[index[0]][index[1]] == 0:
                        upgraded_matrix[index[0]][index[1]] = 0
                    elif k == 'on':
                        upgraded_matrix[index[0]][index[1]] += 1
                else:
                    upgraded_matrix[index[0]][index[1]] += 2
        return upgraded_matrix
    except KeyError as e:
        print('not dictionary key')
    except Exception as e:
        print(f'Unexpected exception occurred! -> {e}')


def amount(matrix):
    """gets the number of lights which are turned on"""
    lights_on = 0
    for item in matrix:
        lights_on += sum(item)
    return lights_on


def light_funct():
    matrix = []
    file_content = rw.read_from_file('input.txt')
    m = create_matrix(1000, 1000)
    for line in file_content:
        coord = get_coordinates(line)
        if coord:
            matrix = change_lights(m, coord)
        else:
            print('Program stopped due to above error')
    return matrix


def upgraded_light_funct():
    matrix = []
    file_content = rw.read_from_file('input.txt')
    m = create_matrix(1000, 1000)
    for line in file_content:
        coord = get_coordinates(line)
        if coord:
            matrix = change_upgraded_lights(m, coord)
        else:
            print('Program stopped due to above error')
    return matrix


if __name__ == '__main__':
    matrix = light_funct()
    lights_on = amount(matrix)
    upgraded_matrix = upgraded_light_funct()
    upgraded_lights_on = amount(upgraded_matrix)
    print(f'There are {lights_on} lights turned on')
    print(f'There are {upgraded_lights_on} upgraded lights turned on')
