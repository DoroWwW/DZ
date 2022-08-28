"""
Дана строка в байтовом виде:" b'r\xc3\xa9sum\xc3\xa9'.

Декодировать её в строковый вид в кодировке по умолчанию.

Затем результат преобразовать снова в байтовый, только уже в кодировке "Latin1".

И на конец результат снова декодировать в строку.

(результаты всех преобразований выводить на экран).


"""




string = b'r\xc3\xa9sum\xc3\xa9'
string  = string.decode()
print(string)
string = string.encode("Latin1")
print(string)
string = string.decode("Latin1")
print(string)