import json

class DataExtractor:

    # Usa biblioteca json para acessar os dados
    def readJsonFile(self, file_path):
        with open(f"{file_path}", "r", encoding="utf-8") as file:
            data = json.load(file)
            
        return data