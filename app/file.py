import json


def dump(data, file, mode='w'):
    stream = open(file, mode)
    json.dump(data, stream)
    stream.close()


def load(file):
    stream = open(file)
    data = json.load(stream)
    stream.close()

    return data


def read(file):
    file = open(file)

    return file.read()


def write(string, file, mode='w'):
    stream = open(file, mode)
    stream.write(string)
    stream.close()
