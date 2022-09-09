"""
Реализовать функцию, которая выведет FirstName из таблицы customers и кол-во их вхождений в таблицу. 
Если решаем через sql, то используем count и секцию group by.



Результат выполнения функции: "Alex 2", т.е. имя и кол-во его вхождений.



((Решение рабочее, но нарушена логика. 
Функция "развертки" выполняет несвойственное ей действие подсчета.))
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


def calc_entries(records: List) -> dict:
    '''
    Функция для подсчёта количества вхождений имён
    '''
    names_quantity = {} 
    for rec in records: 
        if rec[0] in names_quantity:
            names_quantity[rec[0]] += 1
        else:
            names_quantity[rec[0]] = 1
    
    return names_quantity


def print_entries(names_quantity: dict) -> None:
    '''
    Функция для вывода имён и количества их вхождений
    '''
    for record in names_quantity.items():
        print(f"Name: {record[0]} | Entries: {record[1]}")


def main():

    records = execute_query("SELECT FirstName FROM customers")
    names_quantity = calc_entries(records)
    print_entries(names_quantity)
    

main()