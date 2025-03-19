# PassSafeBot

PassSafeBot — это веб-приложение для безопасного хранения паролей с возможностью управления через Telegram-бота.  
Проект разрабатывается на Django с использованием Bootstrap для фронтенда и библиотеки Fernet для шифрования паролей.  

> 💡 Проект в активной разработке — функциональность Telegram-бота и шифрование паролей будут дорабатываться в следующих версиях. Следите за обновлениями в разделе **TODO**!

---

## 🚀 **Функциональность**
- Регистрация и авторизация пользователей  
- Управление паролями (создание, просмотр, обновление, удаление)  
- Категоризация паролей  
- Поиск и фильтрация паролей  
- Telegram-бот для работы с паролями  
- Шифрование паролей с использованием Fernet  
- Восстановление пароля через почту с использованием SMTP 

---

## 🛠️ **Технологии**
- Python 3.11  
- Django 4.2
- Bootstrap 5 
- Telegram API  
- Cryptography (Fernet)  

---

## 🔑 **Настройка .env файла**
Создайте .env файл в корне проекта и добавьте в него следующие параметры:

```env
# Настройки Django
ALLOWED_HOSTS=localhost,127.0.0.1
ADMINS=[["Иван","ivan@example.com"]]
SECRET_KEY=your-django-secret-key
DEBUG=True

# Настройка почты для восстановления пароля
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_USE_SSL=True
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-email-password

# Telegram Bot
TOKEN=your-telegram-bot-token
```

---

## 📦 **Установка и запуск**
### **1. Клонирование репозитория**
```bash
git clone git@github.com:AKhlebnov/passsafebot.git
```
### **2. Перейти в директорию проекта**
```bash
cd passsafebot/backend
```
### **3. Установить зависимости**
Рекомендуется использовать виртуальное окружение:
```bash
python -m venv venv
source venv/Scripts/activate  # Для Windows
# source venv/bin/activate  # Для Linux/macOS
```
Установить зависимости:
```bash
pip install -r requirements.txt
```
### **4. Выполнить миграции**
```bash
python manage.py migrate
```
### **5. Создать суперпользователя**
```bash
python manage.py createsuperuser
```
### **6. Запустить проект**
```bash
python manage.py runserver
```

---

## 🤖 **Настройка Telegram-бота**
1. Создайте нового бота через @BotFather
2. Получите токен для бота
3. Вставьте токен в настройки проекта (файл .env)
4. Перейдите в директорию бота
```bash
cd passsafebot/telegram
```
5. Запустите бота:
```bash
python telebot.py
```

---

## 🚧 **TODO**
* ✅ Сделать шифрование на django-cryptography
* ✅ Добавить регистрацию и авторизацию через Django
* 🛡️ Доработать валидацию данных
* 🤖 Доработать telegram бота, добавить дополнительные команды и API к нему
* 🌐 Улучшить интерфейс (единообразный стиль)
* 🔍 Реализовать поиск и фильтрацию ресурсов  
* 🔑 Полностью реализовать шифрование паролей через Fernet
* 🔒 Добавить двухфакторную аутентификацию 2FA
* ✅ Восстановление пароля через почту

---

## 📄 **Лицензия**
Проект распространяется под лицензией MIT.

---

## 💡 **Автор**
### Александр Хлебнов ###
[GitHub](https://github.com/AKhlebnov/)
[Telegram](https://t.me/khlebnov)

---

### 🔥 **PassSafeBot — надёжное хранилище для ваших паролей!**
