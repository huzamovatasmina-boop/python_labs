# test_lab05.py
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx


def main():
    print("Тестируем JSON → CSV")
    json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")

    print("Тестируем CSV → JSON")
    csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")

    print("Тестируем CSV → XLSX")
    csv_to_xlsx("data/samples/people.csv", "data/out/people.xlsx")

    print("Все тесты завершены!")


if __name__ == "__main__":
    main()
