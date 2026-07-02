from src.utils import load_csv, filter_by_min_score, average_score, summarize

if __name__ == "__main__":
    records = load_csv("data/sample.csv")
    print(f"Chargé {len(records)} enregistrements.")

    filtered = filter_by_min_score(records, 10)
    print(f"Filtré {len(filtered)} enregistrements avec un score >= 10.")

    avg = average_score(filtered)
    print(f"Moyenne des scores: {avg:.2f}")

    summary = summarize(records)
    print(f"Résumé: {summary}")
