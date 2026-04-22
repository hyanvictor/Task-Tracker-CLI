import json
import os

# Criando o arquvio JSON
with open('data/data.json', 'r') as f:
    data = json.load(f)

# Função de gerar ID
def generate_id(tasks):
    # 1. Calcular o próximo ID
    if tasks == []:
        return 1
    else:
        # Lógica para encontrar o maior ID atual e somar 1
        return max(item['id'] for item in tasks) + 1

# Função de adicionar dados
def add_task(data):
    # 1. Carregar a lista do JSON antes de ler.
    if os.path.exists(data):
        with open(data, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = [] # Arquivo vazio ou corrompido
    else:
        data = []
