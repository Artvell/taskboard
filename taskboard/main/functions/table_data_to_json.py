"""файл с функцией для перевода данных в json"""
def table_data_to_json(ids,data,keys,counters):
    """функция для перевода данных в json формат"""
    error_data = []
    end,j = 0,0
    for i,_ in enumerate(counters):
        tmp ={
            "id":int(ids[i]),
        }
        for j in range(end,int(counters[i])-1+end):
            if keys[j]=="" or data[j]=="":
                continue
            else:
                tmp[keys[j]] = data[j]
        end = j+1
        error_data.append(tmp)
    error_data = [data for data in error_data if len(data)>1]
    return error_data
