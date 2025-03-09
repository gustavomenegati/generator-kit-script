import itertools
from collections import defaultdict

class GeneratorBuilder:

    def groupStockByCategory(self, stock_data):

        stock_data_by_category = defaultdict(list)

        for item in stock_data:
            stock_data_by_category[item['Categoria']].append(item)

        return stock_data_by_category


    # Agrupamento dos kits de geradores
    def groupKits(self, stock_data):

        # Criação de um dicionário que agrupa equipamentos de acordo com sua categoria
        stock_data_by_category = self.groupStockByCategory(stock_data)

        # Usa produto cartesiano para obter todas as combinações possíveis.
        all_possible_combinations = list(itertools.product(*stock_data_by_category.values()))

        # Identifica combinações válidas
        valid_combinations = self.searchValidCombinations(all_possible_combinations)
        
        return valid_combinations


    def searchValidCombinations(self, all_possible_combinations):
        # Filtra combinações onde todos os itens tem a mesma "Potencia em W"
        valid_combinations = []

        for kit in all_possible_combinations:
            # Cria um mapeamento rápido: Categoria -> item
            itens = {item['Categoria']: item for item in kit}

            # Extrai os itens de cada categoria
            panel = itens.get('Painel Solar')
            inversor = itens.get('Inversor')
            controller = itens.get('Controlador de carga')

            # Verifica se realmente temos os 3 elementos no kit
            if not (panel and inversor and controller):
                continue

            panel_power = panel['Potencia em W']
            inversor_power = inversor['Potencia em W']
            controller_power = controller['Potencia em W']

            # Verifica relações válidas entre potências (iguais ou painel tendo como potência um divisor da potência dos demais equipamentos)
            if (panel_power == inversor_power == controller_power) or (inversor_power == controller_power and (inversor_power % panel_power == 0)):

                # Define a quantidade de cada equipamento
                panels_quantity = int(inversor_power / panel_power)
                panel["Quantidade Item"] = panels_quantity
                inversor["Quantidade Item"] = 1
                controller["Quantidade Item"] = 1
                
                valid_combinations.append(list(kit))

        treated_combinations = self.treatDataToExport(valid_combinations)

        return treated_combinations

    # Trata os dados para exportação 
    def treatDataToExport(self, generator_kits):
        treated_combinations = []
        generator_counter = 0

        for kit in generator_kits:
            generator_counter += 1
            treated_combinations.append([])

            # Percorre por todos os itens do kit válido
            for item in kit:

                item_copy = item.copy()

                # Adiciona id do gerador
                item_copy["ID Gerador"] = str(generator_counter).zfill(5)

                # Verifica e remove Categoria caso não tenha sido removida anteriormente
                if "Categoria" in item_copy: item_copy.pop("Categoria")

                # Muda nomes de colunas para se adequar ao formato final da exportação
                if "Id" in item_copy: item_copy["ID Produto"] = item_copy.pop("Id")
                if "Produto" in item_copy: item_copy["Nome do Produto"] = item_copy.pop("Produto")
                if "Potencia em W" in item_copy: item_copy["Potência do Gerador (em W)"] = item_copy.pop("Potencia em W")

                treated_combinations[generator_counter - 1].append(item_copy)

        return treated_combinations