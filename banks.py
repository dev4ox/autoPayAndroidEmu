import time
import subprocess

# Функции эмуляции нажатия на банковские приложения внутри memu
def yandex_bank(adb_path, adb_id) -> None:
    # -------------------------   FUNCTION YANDEX BANK    -------------------------------------------------------------
    # Открытие банковского приложения (название пакета приложения, в
    subprocess.run(
        [adb_path, "-s", adb_id, "shell", "monkey", "-p", "com.yandex.bank",
         "-c", "android.intent.category.LAUNCHER", "1"])

    time.sleep(5)

    # Ввод пароля (координаты, если пароль 1234)
    subprocess.run([adb_path, "-s", adb_id, "shell", "input", "tap", "135", "900"])
    subprocess.run([adb_path, "-s", adb_id, "shell", "input", "tap", "360", "900"])
    subprocess.run([adb_path, "-s", adb_id, "shell", "input", "tap", "135", "1000"])
    subprocess.run([adb_path, "-s", adb_id, "shell", "input", "tap", "360", "1000"])
    time.sleep(2)

    # Открытие платежей
    subprocess.run([adb_path, "-s", adb_id, "shell", "input", "tap", "440", "1230"])

    # Открытие галлереи
    subprocess.run([adb_path, "-s", adb_id, "shell", "input", "tap", "650", "90"])

    # Выбор изображения QR-кода
    subprocess.run([adb_path, "-s", adb_id, "shell", "input", "tap", "175", "425"])

    # Привязка QR-кода
    # subprocess.run([adb_path, "-s", adb_id, "shell", "input", "tap", "175", "425"])
    time.sleep(1)

    # Закрыть приложение
    subprocess.run(
        [adb_path, "-s", adb_id, "shell", "am", "force-stop", "com.yandex.bank"])

    # -------------------------   FUNCTION YANDEX BANK END    ---------------------------------------------------------


def ozon_bank(adb_path, adb_id) -> None:
    # -------------------------   FUNCTION OZON BANK    ---------------------------------------------------------------
    # Открытие банковского приложения (название пакета приложения, в
    subprocess.run(
        [adb_path, "-s", adb_id, "shell", "monkey", "-p", "ru.ozon.fintech.finance",
         "-c", "android.intent.category.LAUNCHER", "1"])

    time.sleep(5)

    # Ввод пароля (координаты, если пароль 1234)
    subprocess.run([adb_path, "-s", adb_id, "shell", "input", "tap", "200", "730"])
    subprocess.run([adb_path, "-s", adb_id, "shell", "input", "tap", "350", "730"])
    subprocess.run([adb_path, "-s", adb_id, "shell", "input", "tap", "200", "850"])
    subprocess.run([adb_path, "-s", adb_id, "shell", "input", "tap", "350", "850"])
    time.sleep(2)

    # Оплата QR
    subprocess.run([adb_path, "-s", adb_id, "shell", "input", "tap", "150", "550"])

    # Открытие галлереи
    subprocess.run([adb_path, "-s", adb_id, "shell", "input", "tap", "350", "1150"])

    # Выбор "Загрузить Фото"
    subprocess.run([adb_path, "-s", adb_id, "shell", "input", "tap", "150", "1100"])

    # Выбор альбома из галлереи
    subprocess.run([adb_path, "-s", adb_id, "shell", "input", "tap", "350", "500"])

    # Выбор фотографии
    subprocess.run([adb_path, "-s", adb_id, "shell", "input", "tap", "200", "250"])

    # Оплата QR-кода
    subprocess.run([adb_path, "-s", adb_id, "shell", "input", "tap", "380", "1160"])
    time.sleep(1)

    # Выход из оплаты
    subprocess.run([adb_path, "-s", adb_id, "shell", "input", "tap", "670", "65"])

    # Закрыть приложение
    subprocess.run(
        [adb_path, "-s", adb_id, "shell", "am", "force-stop", "ru.ozon.fintech.finance"])

    # -------------------------   FUNCTION OZON BANK END    -----------------------------------------------------------


def tinkoff_bank(adb_path, adb_id) -> None:
    # -------------------------   FUNCTION TINKOFF BANK    -----------------------------------------------------------
    # Открытие приложения галлерея
    subprocess.run(
        [adb_path, "-s", adb_id, "shell", "monkey", "-p", "com.android.gallery3d",
         "-c", "android.intent.category.LAUNCHER", "1"], stdout=subprocess.DEVNULL)

    time.sleep(5)
    subprocess.run([adb_path, "-s", adb_id, "shell", "input", "tap", "675", "70"])
    time.sleep(1)
    subprocess.run([adb_path, "-s", adb_id, "shell", "input", "tap", "500", "285"])
    time.sleep(2)

    # Открытие банковского приложения (название пакета приложения, в
    subprocess.run(
        [adb_path, "-s", adb_id, "shell", "monkey", "-p", "com.idamob.tinkoff.android",
         "-c", "android.intent.category.LAUNCHER", "1"], stdout=subprocess.DEVNULL)

    time.sleep(10)

    # Ввод пароля (координаты, если пароль 1234)
    subprocess.run([adb_path, "-s", adb_id, "shell", "input", "tap", "210", "930"])
    subprocess.run([adb_path, "-s", adb_id, "shell", "input", "tap", "350", "930"])
    subprocess.run([adb_path, "-s", adb_id, "shell", "input", "tap", "210", "1025"])
    subprocess.run([adb_path, "-s", adb_id, "shell", "input", "tap", "350", "1025"])
    time.sleep(15)

    # Кнопка "платежи"
    subprocess.run([adb_path, "-s", adb_id, "shell", "input", "tap", "215", "1230"])
    time.sleep(10)

    # Проверка на всплывающее уведомление (его закрытие)
    subprocess.run([adb_path, "-s", adb_id, "shell", "input", "tap", "18", "90"])
    time.sleep(2)

    # Кнопка "Сканировать"
    subprocess.run([adb_path, "-s", adb_id, "shell", "input", "tap", "600", "175"])
    time.sleep(5)

    # Открытие галлереи внутри приложения
    subprocess.run([adb_path, "-s", adb_id, "shell", "input", "tap", "52", "1125"])
    time.sleep(2)

    # Выбор изображения QR-кода
    subprocess.run([adb_path, "-s", adb_id, "shell", "input", "tap", "80", "200"])
    time.sleep(1)

    # Кнопка "Выбрать фото
    subprocess.run([adb_path, "-s", adb_id, "shell", "input", "tap", "350", "1200"])
    time.sleep(5)

    # 👇👇👇 ВОЗМОЖНО ЗДЕСЬ НУЖНО ДОБАВИТЬ КНОПКУ ПРИВЯЗКИ СБП!!!
    subprocess.run([adb_path, "-s", adb_id, "shell", "input", "tap", "515", "675"])
    time.sleep(5)

    # Закрыть приложение банка
    subprocess.run(
        [adb_path, "-s", adb_id, "shell", "am", "force-stop", "com.idamob.tinkoff.android"])

    # Закрыть приложение галлерея
    subprocess.run(
        [adb_path, "-s", adb_id, "shell", "am", "force-stop", "com.android.gallery3d"])

    # -------------------------   FUNCTION TINKOFF BANK END    -------------------------------------------------------

