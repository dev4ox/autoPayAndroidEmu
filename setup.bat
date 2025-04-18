REM Создания виртуального окружения
python -m venv venv

REM Активация виртуального окружения
call venv\Scripts\activate

REM Установка зависимостей (или проверка их наличия)
echo Установка зависимостей...
pip install -r requirements.txt

REM Уведомление об установке
echo Скрипт установлен. Для выхода нажмите любую клавишу...
pause >nul

