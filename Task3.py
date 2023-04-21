
user_input = input("Моя радость, напиши текст с круглыми скобками: ")

def minus_skobki(text):
    while '(' in text and ')' in text:
        start = text.find('(')
        end = text.find(')', start)
        text = text[:start] + text[end+1:]
    return text

result = minus_skobki(user_input)
print(result)
