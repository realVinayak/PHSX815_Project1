LINE_SEP = '\n'
CHAR_SEP = ','


def write_multi_list(list_to_write, file_name):
    f = open(file_name, 'w')
    f.write(LINE_SEP.join(
        [CHAR_SEP.join([str(x) for x in num]) for num in list_to_write]))
    f.close()


def read_multi_list(file_name):
    f = open(file_name, 'r')
    lines = [[float(raw) for raw in line.split(CHAR_SEP)] for line in
             f.read().split(LINE_SEP)]
    f.close()
    return lines


def write_list(list_to_write, file_name):
    f = open(file_name, 'w')
    f.write('\n'.join([str(x) for x in list_to_write]))
    f.close()


def read_list(file_name):
    f = open(file_name)
    loaded_list = [float(raw) for raw in f.read().split('\n')]
    f.close()
    return loaded_list
