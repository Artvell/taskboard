import base64

class Encoder:
    def __init__(self, text):
        self.text = text
    def encode(self):
        byte_text = self.text.encode("UTF-8")
        encoded_byte_text = base64.b64encode(byte_text)
        encoded_text = encoded_byte_text.decode("UTF-8")
        return encoded_text
    def decode(self):
        byte_text = self.text.encode("UTF-8")
        decoded_byte_text = base64.b64decode(byte_text)
        decoded_text = decoded_byte_text.decode("UTF-8")
        return decoded_text
