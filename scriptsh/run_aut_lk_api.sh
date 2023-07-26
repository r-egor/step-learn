#!/bin/bash

# Определяем путь к текущему рабочему каталогу
CURRENT_DIR="$PWD"

# Относительные пути к тестовому файлу и директории с отчетами
TEST_FILE="$CURRENT_DIR/tests/test_api.py"
REPORT_DIR="$CURRENT_DIR/reports"

# Проверяем, что файл существует
if [ ! -f "$TEST_FILE" ]; then
    echo "Файл $TEST_FILE не найден"
    exit 1
fi

# Запускаем pytest с использованием относительного пути к файлу test_api.py и директории с отчетами
pytest -v -s "$TEST_FILE" --alluredir="$REPORT_DIR"
