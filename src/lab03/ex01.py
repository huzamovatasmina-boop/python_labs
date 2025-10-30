def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """
    Нормализует текст: приводит регистр, заменяет ё на е, убирает лишние пробелы.
    
    Args:
        text: Исходный текст
        casefold: Приводить к нижнему регистру (по умолчанию True)
        yo2e: Заменять ё/Ё на е/Е (по умолчанию True)
        
    Returns:
        Нормализованный текст
    """
    if casefold==True:
        text=text.casefold()

    if yo2e==True:
        text=text.replace("ё","е").replace("Ё","Е")

    for char in ['\t', '\r', '\n']:
        text = text.replace(char, ' ')
        
    text=text.split()
    text=" ".join(text)
    return text
text="Hello\r\nWorld"
result=normalize(text)
print(result)