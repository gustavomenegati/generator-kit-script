import csv

class DataExporter():

    # Recebe dados já tratados e gera o arquivo .csv
    def buildCSVFile(self, data, csv_filename, fieldnames):
        
        # Unifica as listas em apenas uma para facilitar expçortação
        flat_data = [item for sublist in data for item in sublist]

        # Escreve para csv no diretório "export"
        with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(flat_data)