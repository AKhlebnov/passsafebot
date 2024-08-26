"""
Telegram bot for interacting with Django REST API to manage passwords.

Usage:
- /start: sends a welcome message.
- /get_password <resource>: retrieves the password for the specified resource.
"""

import logging
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
# Set higher logging level for httpx to
# avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# Токен вашего Telegram-бота
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# URL API вашего Django-приложения
API_URL = 'http://127.0.0.1:8000/api/passwords/'


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_text(
        f"Hi {user.full_name}! "
        "Use /get_password <resource> to retrieve your password."
    )


async def get_password(
        update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Get a password for the specified resource and send it to the user."""
    if len(context.args) == 0:
        await update.message.reply_text(
            "Please provide the resource name. Usage: /get_password <resource>"
        )
        return

    resource = ' '.join(context.args)
    response = requests.get(API_URL, params={'resource': resource})

    if response.status_code == 200:
        passwords = response.json()
        if passwords:
            password = passwords[0]['password']
            await update.message.reply_text(
                f'Password for {resource}: {password}'
            )
        else:
            await update.message.reply_text(
                f'No password found for the resource: {resource}'
            )
    else:
        await update.message.reply_text(
            'Error fetching password from the API. Please try again later.'
        )


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # Register handlers for commands
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("get_password", get_password))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
