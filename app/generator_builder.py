import itertools
from collections import defaultdict

class GeneratorBuilder:

    # Criação de um dicionário que agrupa equipamentos de acordo com sua categoria
    def group_stock_by_category(self, stock_data):

        stock_data_by_category = defaultdict(list)

        for item in stock_data:
            stock_data_by_category[item['Categoria']].append(item)

        return stock_data_by_category


    # Agrupamento dos kits de geradores
    def group_kits(self, stock_data):

        generator_counter = 0

        stock_data_by_category = self.group_stock_by_category(stock_data)

        # Usa produto cartesiano para obter todas as combinações possíveis.
        all_possible_combinations = list(itertools.product(*stock_data_by_category.values()))

        # Filtra combinações onde todos os itens tem a mesma "Potencia em W"
        valid_combinations = []
        for kit in all_possible_combinations:
            
            # Extrai "Potencia em W" de cada dicionário na combinação
            potencia_values = {item['Potencia em W'] for item in kit}

            # Se todos forem os mesmos, teremos exatamente 1 elemento.
            if len(potencia_values) == 1:
                generator_counter += 1

                self.add_group_id(kit, generator_counter)

                valid_combinations.append(list(kit))

        return valid_combinations

    def add_group_id(self, kit, generator_counter):

        for item in kit:
            item["ID Gerador"] = str(generator_counter).zfill(5)
