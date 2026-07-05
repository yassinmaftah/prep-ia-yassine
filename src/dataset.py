from src.utils import load_csv

class Dataset:
    def __init__(self, name:str):
        self.name = name
        self._records: list[dict] = []

    def load(self, records : list[dict]) -> None:
        self._records = records

    @property
    def row_count(self) -> int:
        return len(self._records)

    @property
    def columns(self) -> list[str]:
        if (self.row_count == 0):
            return []
        # print(self._records[0].keys())
        return list(self._records[0].keys())


    def summary(self) -> dict:
        return {
            "name": self.name,
            "rows": self.row_count,
            "columns": self.columns
        }
        
    def __repr__(self) -> str:
        return f"Dataset(name={self.name!r}, rows={self.row_count})"



class CsvDataset(Dataset):
    def __init__(self, name: str):
        super().__init__(name)


    def load_from_csv(self, path: str) -> None:
        raw_data = load_csv(path)
        self.load(raw_data)

    def filter_by_column(self, column: str, min_value: float) -> list[dict]:        
        return [row for row in self._records if float(row[column]) >= min_value]