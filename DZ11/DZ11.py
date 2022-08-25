"""
При помощи функции filter() из котрежа слов отфильтровать только те, которые являются полиндромами
 (слова которые читаются одинаково в обе стороны), регистр букв не учитывать.
"""


inputdata = ['Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык']
print(inputdata)

data_polindrom = list(filter(lambda x: x.lower() == x [::-1].lower(), inputdata))

print(inputdata)
print(data_polindrom)