#!/bin/bash

# Определяем путь к текущему рабочему каталогу
CURRENT_DIR="$PWD"

# Относительный путь к директории с отчетами
REPORT_DIR="$CURRENT_DIR/reports"

# Запускаем Allure serve с использованием относительного пути к директории с отчетами
allure serve "$REPORT_DIR"
