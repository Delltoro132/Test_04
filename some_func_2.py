# coding: utf-8 python: 3.7
import os
import psutil


def prep():
    """
    Высчитывает кол-во оперативной памяти на машине
    :return: list[int(8), True]
    """
    memory_info = psutil.virtual_memory()
    memory_total = memory_info.total
    memory_in_gb = round(memory_total / (1024 * 1024 * 1024))
    int_memory_in_gb = int(memory_in_gb)
    if int_memory_in_gb > 1:
        return int_memory_in_gb, False
    else:
        return int_memory_in_gb, True


def run():
    """Создает файл объемом 1024 KB"""
    with open('test.txt', mode='wb') as file:
        file.truncate(1024 * 1024)


def clean_up():
    """Удаляет файл если он найден"""
    if os.path.exists('test.txt'):
        os.remove('test.txt')


prep()
# run()
# clean_up()
# prep()
