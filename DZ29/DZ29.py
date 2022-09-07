"""
Реализовать функцию, которая выведет FirstName из таблицы customers и кол-во их вхождений в таблицу. 
Если решаем через sql, то используем count и секцию group by.



Результат выполнения функции: "Alex 2", т.е. имя и кол-во его вхождений.

"""



import os
import sqlite3
from statistics import quantiles

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
    quantity_name = {} 
    for rec in records: 
        
              
        if rec[0] in quantity_name:
            quantity_name[rec[0]] += 1
        else:
            quantity_name[rec[0]] = 1
    for i in quantity_name.items():
        print(i[0],i[1])


def main():
    
    
    records = execute_query("SELECT FirstName FROM customers")
    unwrapper(records)
    

main()