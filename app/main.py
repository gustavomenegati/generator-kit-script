from data_extractor import DataExtractor
from generator_builder import GeneratorBuilder
from data_exporter import DataExporter

def main():
    data_extractor = DataExtractor()
    stock_data = data_extractor.readJsonFile("data-resources/stock.json")

    generator_builder = GeneratorBuilder()

    generator_kits = generator_builder.groupKits(stock_data)

    data_exporter = DataExporter()
    data_exporter.buildCSVFile(generator_kits, "generator_kits.csv", ["ID Gerador", "Potência do Gerador (em W)", "ID Produto", "Nome do Produto", "Quantidade Item"])

if __name__ == '__main__':
    main()
