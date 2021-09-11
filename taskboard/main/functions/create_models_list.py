"""Файл с функцией для объединения двух массивов данных"""
def create_other_data_list(exists,data):
    """Функция для объединения двух массивов данных"""
    result = exists.copy()
    flag = False
    if exists is None or len(exists)==0:
        return [{"id":el.id} for el in data]
    for element in data:
        if not flag:
            for existed_element in exists:
                if existed_element["id"]!=element.id:
                    result.append({"id":element.id})
                else:
                    flag = True
                    break
    return result
