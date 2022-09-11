def filter_(data, param):
    return list(filter(lambda x: param in x, data))


def map_(data, param):
    column = int(param)
    return list(map(lambda x: x.split(' ')[column], data))


def unique_(data, *args, **kwargs):
    return list(set(data))


def sorted_(data, param):
    revers_param = True if param == 'desc' else False
    return sorted(data, reverse=revers_param)


def limit_(data, param):
    limit_number = int(param)
    return list(data)[:limit_number]


def file_generator(file_name):
    for row in open(f"data/{file_name}", 'r'):
        yield row
