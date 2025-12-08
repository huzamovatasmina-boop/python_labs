# src/lab06/cli_text.py
import argparse
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(
        description="Текстовые утилиты для анализа файлов"
    )
    subparsers = parser.add_subparsers(dest="command", help="Доступные команды")
    
    # cat команда
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Входной файл")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")
    
    # stats команда
    stats_parser = subparsers.add_parser("stats", help="Статистика частот слов")
    stats_parser.add_argument("--input", required=True, help="Входной текстовый файл")
    stats_parser.add_argument("--top", type=int, default=5, help="Количество топ-слов")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    try:
        if args.command == "cat":
            with open(args.input, 'r', encoding='utf-8') as f:
                for i, line in enumerate(f, 1):
                    if args.n:
                        print(f"{i:4} {line}", end='')
                    else:
                        print(line, end='')
                        
        elif args.command == "stats":
            # Импортируем функцию из lab03
            from src.lab03.text_stats import calculate_word_frequency  # предположительное имя функции
            result = calculate_word_frequency(args.input, args.top)
            print(f"Топ-{args.top} слов в файле {args.input}:")
            for word, count in result:
                print(f"  {word}: {count}")
                
    except FileNotFoundError:
        print(f"❌ Ошибка: файл {args.input} не найден")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()