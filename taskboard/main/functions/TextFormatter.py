import re
class TextFormatter:
    def __init__(self,data):
        self.data = data
        self.keys = ["bio","info","desc"]
        print("data: ",self.data)
    def textToJson(self):
        f = False
        parsed_data = re.findall('<p>\[(.+?)\]</p>', self.data)
        json_data = {}
        for i in range(len(parsed_data)):
            if i<3:
                json_data[self.keys[i]] = parsed_data[i]
            else:
                f = True
                break
        if f:
            json_data["other"] = parsed_data[3:]
        return json_data
    
    def jsonToText(self):
        parsed_data = ""
        for key,value in self.data.items():
            if key in self.keys:
                parsed_data += (f"<p>[{value}]</p>")
            elif key == "other":
                parsed_data += str(value)
        print(parsed_data)
        return parsed_data