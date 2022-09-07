"""
Реализовать функцию, которая выведет прибыль по таблице invoice_items. 
Сумма по заказу = UnitPrice * Quantity. Если решаем через sql, то нужно использовать sum.



Результат выполнение функции - одно число, которое является суммой всех заказов.

"""

import os
import sqlite3

from typing import List, Set


def execute_query(query_sql: str) -> List:
    '''
    Функция для выполнения запроса
    :param query_sql: запрос
    :return: результат выполнения запроса
    '''
    
    db_pass = os.path.join(os.getcwd(), 'chinook.db')
    connection = sqlite3.connect(db_pass)
    cur = connection.cursor()
    result = cur.execute(query_sql)
    return result
        


def unwrapper(records: List) -> None:
    '''
    Функция для вывода результата выполнения запроса
    :param records: список ответа БД
    '''
    sum = 0
    for record in records:
        sum += record[0]*record[1]
    print(f"sum: {sum}")
def main():
    
    records = execute_query("SELECT UnitPrice, Quantity FROM invoice_items")
    unwrapper(records)
    

main()