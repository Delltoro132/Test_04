# coding: utf-8 python: 3.7
import os
import time


def prep():
    """
    Высчитывает кол-во секунд от начала эпохи Unix и проверяет на кратность 2.
    :return: True or False
    """
    seconds = round(time.time())
    if seconds % 2 == 0:
        return True
    else:
        return False


def run():
    """
    Находит имена файлов из текущей директории  виде списка.
    :return: ['file.log', 'logging_info.py', ...]
    """
    return os.listdir(path=".")


def clean_up():
    pass

