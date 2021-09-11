"""файл с классом TextFormatter"""
import re
class TextFormatter:
    """Переводит текстовые данные в json и наоборот"""
    def __init__(self,data):
        self.data = data
        self.keys = ["bio","info","desc"]

    def text_to_json(self):
        """переводит текст в json"""
        flag = False
        parsed_data = re.findall(r'<p>\[(.+?)\]</p>', self.data)
        json_data = {}
        for i,element in enumerate(parsed_data):
            if i<3:
                json_data[self.keys[i]] = element
            else:
                flag = True
                break
        if flag:
            json_data["other"] = parsed_data[3:]
        return json_data

    def json_to_text(self):
        """переводит json в текстовый формат"""
        parsed_data = ""
        for key,value in self.data.items():
            if key in self.keys:
                parsed_data += (f"<p>[{value}]</p>")
            elif key == "other":
                parsed_data += str(value)
        return parsed_data
