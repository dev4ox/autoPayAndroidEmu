## Инструкция по запуску
1. Распакуйте файлы из архива в отдельную папку
2. Создайте эмулятор MEmu, задайте ему имя
3. Внутри MEmu установить:
   - TBank (войти в приложение банка и подождать 20 секунд для полной прогрузки приложения)
4. Установить на пк Python 3.12: https://www.python.org/downloads/release/python-3129/
5. Выйти из пользователя (перезапустить ПК) для активации пользовательской переменной python
6. Распаковать папку в удобное место
7. Откройте файл settings.py с помощью блокнота или IDE, заполните:
   - ℹ️ BOT_TOKEN - создавайте своего бота через @botfather, добавляйте его в администраторы группы
   - ⚠️ После создания бота перейдите в @botfather, введите команду 
/setprivacy
выберите созданного бота и нажмите на кнопку disable
8. После запустите setup.bat и отправьте любое фото в чат. В командной строке напишет id чата (-100********)
9. Вставьте данный id чата в settings.py
10. Всё настроено!

ДЛЯ ЗАПУСКА: start.bat


### Примечание:
1. Если меняете путь до **adb.exe**, обратите внимание на слэш "**/**". Он должен быть НЕ БЭК-СЛЭШЕМ!