import json
import os

# Função de gerar ID
def generate_id(tasks):
    # 1. Calcular o próximo ID
    if tasks == []:
        return 1
    else:
        # Lógica para encontrar o maior ID atual e somar 1
        return max(item['id'] for item in tasks) + 1

# Função de adicionar dados
def add_task(dado, novo_dado='data.json'):
    # 1. Verifica se o arquivo existe
    if not os.path.exists('data/data.json'):
        # Se o arquivo (data) não existir ele, cria uma lista vazia
        with open('data/data.json', 'w') as file:
            json.dump([], file)
    else:
        # 2. Lê os dados existentes
        with open('data/data.json', 'r', encoding='utf-8') as f:
                # 3. Le os dados existentes
                data = json.load(f)
    
    # 4. Grava de volta no JSON
    with open('data/data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
        data.append(dado)
    
# teste
novo_registro = {
    "id": 1,
    "description": "progamming in JAVA",
    "status": "todo",
    "createdAt": "04/22/2026",
    "updatedAt": "04/22/2026"
}

add_task(novo_registro)