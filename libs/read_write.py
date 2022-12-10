
def read_from_file(file_path):
    """
    returns the file content as a list
    every row within the file being a list element
    :param file_path:
    :return:
    """
    try:
        with open(file_path, 'r') as fr:
            content = fr.readlines()
        return content
    except FileNotFoundError as e:
        print(f'Fisierul nu se gaseste sau nu a putut fi deschis. '
              f'Eroarea: {e}')
        return
    except Exception as e:
        print(f'eroare neasteptata: -> {e}')
        return


if __name__ == '__main__':

    names = read_from_file('nume.txt')
    if names:
        new_names = [name.strip() for name in names]
        # print(new_names)
        count = {item: new_names.count(item) for item in set(new_names)}
        print(count)
    else:
        print('eroare de fisier')
