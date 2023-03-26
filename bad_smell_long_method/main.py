# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def _read(csv: str):
    l = [line.split(';') for line in csv.split('\n')]
    data = [{'name': i[0], 'age': i[1]} for i in l]
    return data


def _sort(data):
    return sorted(data, key=lambda x: int(x['age']))


def _filter(data):
    new_data = [person for person in data if int(person['age']) > 10]
    return new_data


def get_users_list(csv):
    data = _read(csv)
    _new_data = _sort(data)
    result_data = _filter(_new_data)

    return result_data


if __name__ == '__main__':
    print(get_users_list(csv))
