def create_other_data_list(exists,data):
    result = exists.copy()
    f = False
    if exists == None or len(exists)==0:
        return [{"id":el.id} for el in data]
    for element in data:
        if not f:
            for el in exists:
                if el["id"]!=element.id:
                    result.append({"id":element.id})
                else:
                    f = True
                    break
    return result