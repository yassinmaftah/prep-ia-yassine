from src.dataset import CsvDataset

if __name__ == "__main__":
    print("--- Démarrage du pipeline POO ---")
    
    dataset = CsvDataset("Sample Data")
    dataset.load_from_csv("data/sample.csv")
    
    print(dataset)
    print(f"the resume: {dataset.summary()}")
    
    passed = dataset.filter_by_column('score', 10)
    print(f"Admis (score >= 10): {len(passed)}")