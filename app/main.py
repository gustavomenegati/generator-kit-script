from data_extractor import DataExtractor
from generator_builder import GeneratorBuilder
from data_exporter import DataExporter
import time

def main():

    while True:

        # Instancia classe de extração e usa para leitura da base de dados
        data_extractor = DataExtractor()
        stock_data = data_extractor.readJsonFile("data-resources/stock.json")

        # Instancia classe que transforma dados dos geradores e fornece os dados extraídos
        generator_builder = GeneratorBuilder()
        generator_kits = generator_builder.groupKits(stock_data)

        # Instancia classe de exportação, fornecendo os dados a serem exportados, nome do arquivo e formato desejado 
        data_exporter = DataExporter()
        data_exporter.buildCSVFile(generator_kits, "generator_kits.csv", ["ID Gerador", "Potência do Gerador (em W)", "ID Produto", "Nome do Produto", "Quantidade Item"])

        # Após a execução inicial, aguarda 7 dias para a próxima execução
        one_week_in_seconds = 7 * 24 * 60 * 60
        time.sleep(one_week_in_seconds)

if __name__ == '__main__':
    main()
