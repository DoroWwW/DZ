"""
Используя input() ввести предложение состоящее из двух слов. Создать 2 переменные и в каждую записать по 1 введённому слову
используя методы строк. 
Создать новую переменную 3-мя разными способами форматирования (фактически 3 переменные), которая бы состояла из введённых слов
в обратном порядке, первое слово должно состоять только из больших букв, а второе с первой заглавной буквы и остальных маленьких.
В начале предложения должен быть восклицательный знак, а в конце вопросительный.

Используя только атрибуты функции print() вывести первоначальную строку и получившиеся разными способами форматирования через
 разделитель "<<<>>>", вывод сделать в файл.
 """

sentence = input("Enter the sentence:")

first_word ,second_word = sentence.split()
second_word = second_word.upper() 
first_word =  first_word.title()
edited_sentence_1 = "!%(s)s %(f)s?" % {"s": second_word, "f": first_word}
edited_sentence_2 = "!{} {}?".format(second_word, first_word)
edited_sentence_3 = f"!{second_word} {first_word}?"


#write in file

file_txt = open(r"D:\GitHub reps\DZ\DZ3\dz3.txt", "w")

print(f"sentence: {sentence} ", f" %s:{edited_sentence_1} ", f" format:{edited_sentence_2} ", f" fstring:{edited_sentence_3}", sep = "<<<>>>", file = file_txt )

file_txt.close()

#Пшеничний Дмитро