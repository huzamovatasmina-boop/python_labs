# src/lab06/cli_convert.py
import argparse
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(
        description="Конвертер данных между форматами JSON, CSV, XLSX"
    )
    subparsers = parser.add_subparsers(dest="command", help="Доступные команды")
    
    # json2csv команда
    json2csv_parser = subparsers.add_parser("json2csv", help="Конвертировать JSON в CSV")
    json2csv_parser.add_argument("--in", dest="input", required=True, help="Входной JSON файл")
    json2csv_parser.add_argument("--out", dest="output", required=True, help="Выходной CSV файл")
    
    # csv2json команда  
    csv2json_parser = subparsers.add_parser("csv2json", help="Конвертировать CSV в JSON")
    csv2json_parser.add_argument("--in", dest="input", required=True, help="Входной CSV файл")
    csv2json_parser.add_argument("--out", dest="output", required=True, help="Выходной JSON файл")
    
    # csv2xlsx команда
    csv2xlsx_parser = subparsers.add_parser("csv2xlsx", help="Конвертировать CSV в XLSX")
    csv2xlsx_parser.add_argument("--in", dest="input", required=True, help="Входной CSV файл")
    csv2xlsx_parser.add_argument("--out", dest="output", required=True, help="Выходной XLSX файл")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    try:
        if args.command == "json2csv":
            from src.lab05.json_csv import json_to_csv
            json_to_csv(args.input, args.output)
            print(f"✅ Успешно конвертирован {args.input} → {args.output}")
            
        elif args.command == "csv2json":
            from src.lab05.json_csv import csv_to_json
            csv_to_json(args.input, args.output)
            print(f"✅ Успешно конвертирован {args.input} → {args.output}")
            
        elif args.command == "csv2xlsx":
            from src.lab05.csv_xlsx import csv_to_xlsx
            csv_to_xlsx(args.input, args.output)
            print(f"✅ Успешно конвертирован {args.input} → {args.output}")
            
    except FileNotFoundError as e:
        print(f"❌ Ошибка: файл не найден - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Ошибка при конвертации: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
    