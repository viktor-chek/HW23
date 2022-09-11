import service

CMD_TO_SERVICE = {
    "filter": service.filter_,
    "map": service.map_,
    "unique": service.unique_,
    "sort": service.sorted_,
    "limit": service.limit_
}


def response_builder(path, cmd1, param1, cmd2, param2):
    try:
        content = service.file_generator(path)
        step_one = CMD_TO_SERVICE[cmd1](data=content, param=param1)
        return CMD_TO_SERVICE[cmd2](data=step_one, param=param2)

    except FileNotFoundError:
        return f"Файл '{path}' не найден", 404
