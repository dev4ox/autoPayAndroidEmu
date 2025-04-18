import os
import subprocess
import cv2
from pyzbar.pyzbar import decode
from telegram import Update, Bot
from telegram.ext import Application, MessageHandler, filters, CallbackContext
from pymemuc import PyMemuc
from settings import *
from banks import tinkoff_bank, ozon_bank, yandex_bank

bot = Bot(token=BOT_TOKEN)


def contains_qr_code(image_path) -> bool:
    """Проверяет, есть ли QR-код на изображении."""
    try:
        image = cv2.imread(image_path)
        decoded_objects = decode(image)
        return len(decoded_objects) > 0
    except Exception as e:
        print(f"⚠️ Ошибка при проверке QR-кода: {e}")
        return False


def get_adb_devices(adb_path: str) -> list:
    """Возвращает список всех подключённых ADB-устройств."""
    result = subprocess.check_output([adb_path, "devices"]).decode("utf-8")
    devices = []
    for line in result.strip().split("\n")[1:]:  # пропускаем первую строку
        if line.strip() and "device" in line:
            device_id = line.split()[0]
            devices.append(device_id)
    return devices


def connect_memu(file_path: str, file_name: str) -> str:
    """Подключается к эмулятору по имени, возвращает его adb_id и загружает файл."""
    # Получение нужного adb_id по имени VM
    adb_id = MEMU_ADB_PORTS.get(MEMU_VM_NAME)
    if not adb_id:
        raise Exception(f"❌ Неизвестное имя виртуальной машины: '{MEMU_VM_NAME}'")

    # Проверка, подключён ли этот ADB ID
    connected_devices = get_adb_devices(ADB_PATH)
    print(f"📱 Подключённые ADB-устройства: {connected_devices}")

    if adb_id not in connected_devices:
        raise Exception(f"⚠️ Эмулятор '{MEMU_VM_NAME}' с ADB ID '{adb_id}' не найден среди подключённых.")

    # Загружаем изображение в эмулятор
    try:
        subprocess.run([ADB_PATH, "-s", adb_id, "push", file_path, f"/sdcard/Pictures/Telegram/{file_name}"], check=True)
        print(f"📥 Файл '{file_name}' успешно передан в эмулятор {MEMU_VM_NAME} ({adb_id})")
    except subprocess.CalledProcessError as e:
        raise Exception(f"⚠️ Ошибка при передаче файла в эмулятор '{MEMU_VM_NAME}': {e}")

    return adb_id



async def process_qr(update: Update, context: CallbackContext):
    adb_id = ''
    message = update.effective_message

    print(f'В процессе сообщение из чата: {message.chat.id}, id сообщения: {message.message_id}\n')

    if not message.photo:
        print("Фото не найдено")
        return

    # Скачивание фото
    try:
        file_id = message.photo[-1].file_id
        file = await context.bot.get_file(file_id)
        if not os.path.exists(SAVE_FOLDER):
            os.makedirs(SAVE_FOLDER, exist_ok=True)
        file_name = f"{MEMU_VM_NAME}_{message.message_id}.jpg"
        file_path = os.path.join(SAVE_FOLDER, file_name)
        await file.download_to_drive(file_path)
    except Exception as e:
        print(f"Ошибка скачивания фото: {e}")
        await context.bot.send_message(chat_id=CHAT_ID, text=f"⚠️ Ошибка скачивания фото.")
        return

    # Проверка наличия QR-кода на изображении
    if not contains_qr_code(file_path):
        print(f"QR-код не найден в файле {file_path}")
        return  # Пустой return, обработка не продолжается

    try:
        adb_id = connect_memu(file_path, file_name)
    except Exception as e:
        print(e)
        await context.bot.send_message(chat_id=CHAT_ID, text=str(e))

    # Выбор функции оплаты через банк
    try:
        if BANK == "yandex":
            yandex_bank(ADB_PATH, adb_id)
            bank_name = 'Яндекс'
        elif BANK == "ozon":
            ozon_bank(ADB_PATH, adb_id)
            bank_name = 'Озон'
        elif BANK == "tinkoff":
            tinkoff_bank(ADB_PATH, adb_id)
            bank_name = 'ТБанк'
        else:
            raise Exception("⚠️ Выбрано неверное банковское приложение!")
        await context.bot.send_message(chat_id=CHAT_ID, text=f"Оплата выполнена через {bank_name} банк")
    except Exception as e:
        print(f"Ошибка при оплате через банковское приложение: {e}")
        await context.bot.send_message(chat_id=CHAT_ID, text="Ошибка при оплате через банковское приложение.")


def main():
    print("Перед запуском настройте файл settings.py!!!\nСкрипт запущен")
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.PHOTO, process_qr))
    app.run_polling()


if __name__ == "main":
    main()

    # print(connect_memu(os.path.join(SAVE_FOLDER, f"qr_124.jpg")))
    # tinkoff_bank("127.0.0.1:21503")