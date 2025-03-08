import csv

class DataExporter():

    # Recebe dados já tratados e gera o arquivo .csv
    def buildCSVFile(self, data, csv_filename):

        # Normaliza o dado para csv
        flat_data = [item for sublist in data for item in sublist]

        # Identifica nome das colunas a partir do primeiro elemento dos dados
        fieldnames = list(flat_data[0].keys())

        # Escreve para csv no diretório "export"
        with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(flat_data)