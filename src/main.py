
import json
def txt_to_json(entre, sortie):
    with open(entre, 'r', encoding='utf-8') as f:
        data_list = []
        for line in f:
            data = json.loads(line)
            data_list.append(data)

    with open(sortie, 'w') as f:
        json.dump(data_list, f, indent=4)

    print("Fichier modifié avec succès!")

txt_to_json('data.txt', 'nouveau_fichier.json')