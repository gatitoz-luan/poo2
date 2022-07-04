compara_pontos = [55, 4, 92, 1, 104, 64, 104, 99, 20]
max_value = max(compara_pontos)
id_vence = []

for idx in range(len(compara_pontos)):
    if (compara_pontos[idx] == max_value):
        id_vence.append(idx) 
    
print(id_vence)