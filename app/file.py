def read(file):
    file = open(file, 'r')

    return file.read()


def write(string, file, mode='w'):
    stream = open(file, mode)
    stream.write(string)
    stream.close()
