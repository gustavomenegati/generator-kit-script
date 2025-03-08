from data_extractor import DataExtractor
from generator_builder import GeneratorBuilder
from data_exporter import DataExporter

def main():
    data_extractor = DataExtractor()
    stock_data = data_extractor.read_json_file("data-resources/stock.json")

    generator_builder = GeneratorBuilder()

    generator_kits = generator_builder.group_kits(stock_data)

    data_exporter = DataExporter()
    data_exporter.buildCSVFile(generator_kits, "generator_kits.csv")

if __name__ == '__main__':
    main()
