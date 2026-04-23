import json
import os
from datetime import datetime

# Função de gerar ID
def generate_id(tasks):
    # 1. Calcular o próximo ID
    if tasks == []:
        return 1
    else:
        # Lógica para encontrar o maior ID atual e somar 1
        return max(item['id'] for item in tasks) + 1

# Função de adicionar dados
def add_tasks():
    
    
# teste
novo_registro = {
    "id": 1,
    "description": "progamming in JAVA",
    "status": "todo",
    "createdAt": "04/22/2026",
    "updatedAt": "04/22/2026"
}

add_task(novo_registro)