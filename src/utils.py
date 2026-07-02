import csv
from pathlib import Path 

def load_csv(path : str | Path) -> list[dict]: 
    data_list = []
    with open(path) as file_data :
        data = csv.DictReader(file_data)
        for row in data:
            data_list.append(row)
            
    return data_list
    

# print(load_csv("data/sample.csv"))

def filter_by_min_score(records: list[dict], min_score: float) -> list[dict]:
    """Retourne les enregistrements dont score >= min_score."""
    return [row for row in records if float(row['score']) >= min_score]


def average_score(records: list[dict]) -> float:
    """Calcule la moyenne du champ 'score'. Retourne 0.0 si liste vide."""
    if (len(records) == 0) :
        return 0.0
    scores = [float(row['score']) for row in records]
    return sum(scores) / len(records)

def summarize(records: list[dict]) -> dict:
    if (len(records) == 0) :
        return {
        'count': 0,
        'avg_score': 0.0,
        'max_score': 0.0,
        'min_score': 0.0
        }
    all_scors = [float(row['score']) for row in records]
    return {
        'count': len(records),
        'avg_score': average_score(records),
        'max_score': max(all_scors),
        'min_score': min(all_scors)
    }
