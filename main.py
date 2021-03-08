# coding: utf-8 python: 3.7

import unittest
import os

from logging_info import log, logging_info
import some_func_1
import some_func_2

logging_info()


class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


@unittest.skipIf(some_func_1.prep(), 'skipped')
class TcId00ListOfFiles(unittest.TestCase):

    def test_01_prep(self):
        """Проверка функции some_func_1.prep()"""
        return_value = some_func_1.prep()

        # logging in file.log
        if return_value:
            log.info('OK: Количество секунд, кратно 2')
        else:
            log.info('NOK: Количество секунд, не кратно 2')

        self.execute()
        self.assertFalse(return_value)

    @staticmethod
    def test_02_run():
        """Проверка функции some_func_1.run()"""
        # logging in file.log
        if some_func_1.run():
            log.info(f'OK: Список файлов из домашней директории: \n{some_func_1.run()}')
        else:
            log.info(f'NOK: Список файлов не был найден.')

    def test_03_clean_up(self):
        pass

    def execute(self):
        """Дополнительные проверки для some_func_1.prep()"""
        return_value = some_func_1.prep()

        # logging in file.log
        if return_value is not None:
            log.info(f'OK: Значение return_value: {return_value} - не является пустым.')
        else:
            log.info(f'NOK: Значение return_value: {return_value} - является пустым.')

        if isinstance(return_value, bool):
            log.info(f'OK: Значение return_value: {return_value} - является булевым.')
        else:
            log.info(f'NOK: Значение return_value: {return_value} - не является булевым.')

        self.assertIsNotNone(return_value)
        self.assertIsInstance(return_value, bool)


@unittest.skipIf(some_func_2.prep()[1], 'skipped')
class TcId01RandomFile(unittest.TestCase):

    def test_01_prep(self):
        """Проверка функции some_func_2.prep()"""
        return_info = some_func_2.prep()[0]

        # logging in file.log
        if return_info > 1:
            log.info('OK: В системе больше 1 GB оперативной памяти.')
        else:
            log.info('NOK: В системе меньше 1 GB оперативной памяти.')

        self.execute()
        self.assertGreater(return_info, 1)

    def test_02_run(self):
        """Проверка функции some_func_2.run()"""
        some_func_2.run()
        file_exist = os.path.exists('test.txt')

        # logging in file.log
        if file_exist:
            log.info('OK: Файл был создан и находится на диске.')
        else:
            log.info('NOK: Файл не был создан.')

        self.assertTrue(file_exist)

    def test_03_clean_up(self):
        """Проверка функции some_func_2.clean_up()"""
        some_func_2.clean_up()
        file_exist = os.path.exists('test.txt')

        # logging in file.log
        if file_exist:
            log.info('NOK: Файл не был удален. ')
        else:
            log.info('OK: Файл отсутствует.')

        self.assertFalse(file_exist)

    def execute(self):
        """Дополнительные проверки для some_func_2.prep()"""
        return_info = some_func_2.prep()[0]

        # logging in file.log
        if return_info:
            log.info(f'OK: Количество оперативной памяти определино: {return_info} GB')
        else:
            log.info(f'NOK: Не удалось определить количество памяти.')

        if isinstance(return_info, int):
            log.info(f'OK: Найденное значение, целое число.')
        else:
            log.info(f'NOK: Найденное значение не число.')

        self.assertIsNotNone(return_info)
        self.assertIsInstance(return_info, int)


if __name__ == "__main__":
    unittest.main(failfast=True, exit=False)
