# coding: utf-8 python: 3.7
import logging

log = logging.getLogger('logger')


def logging_info():
    """Настройки логгера"""
    log_file_name = 'file.log'

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter('\n%(asctime)s %(levelname)s %(message)s', '%Y-%m-%d %H:%M'))
    stream_handler.setLevel(logging.DEBUG)
    log.addHandler(stream_handler)

    file_handler = logging.FileHandler(log_file_name, encoding='utf8')
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s', '%Y-%m-%d %H:%M:%S'))
    file_handler.setLevel(logging.DEBUG)
    log.addHandler(file_handler)

    log.setLevel(logging.DEBUG)
