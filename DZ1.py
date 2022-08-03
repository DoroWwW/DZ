"""""
1. Создать 3 переменные с одинаковыми данными и с одинаковыми идентификаторами

2. Создать 2 переменные с одинаковыми данными и с разными идентификаторами

3. Поменять их типы так, чтобы у 1-х трёх стали разные идентификаторы, но при этом остались одинаковые данные, а у 2-х последних стали одинаковые идентификаторы и остались одинаковые данные.



* добиться нужного результата необходимо только приведением типов данных к нужному



Пример выполнения:

a1 = ....

a2 = ....



a1 == a2

True

a1 is a2

True



преобразование типов а1 и а2 без присвоения им новых значений и потом:



a1 == a2

True

a1 is a2

False
"""""


#1
same_id1 = (100,)
same_id2 = (100,)
same_id3 = (100,)

#2

diff_id1 = [202,]
diff_id2 = [202,]


#3

#первые три 
print("before:")
print("same id1 ",id(same_id1))
print("same id2 ",id(same_id2))
print("same id3 ",id(same_id3))

print("after:")
print("same id1 ",id(list(same_id1)))
print("same id2 ",id(list(same_id2)))
print("same id3 ",id(list(same_id3)))

#остальные два
print("before:")
print("diff id1 ", id(diff_id1))
print("diff id2 ", id(diff_id2))

print("after:")
print("diff id1 ",id(tuple(diff_id1)))
print("diff id2 ",id(tuple(diff_id2)))

