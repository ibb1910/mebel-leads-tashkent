import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🪑 Mebel Leads Tashkent запущен!\n\n"
        "Я буду присылать сюда найденные заявки "
        "на мебель после подключения источников."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Бот готов к настройке источников заявок.\n"
        "Поиск ещё не подключён."
    )

def main():
    if not TOKEN:
        raise RuntimeError("Не задан BOT_TOKEN")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.run_polling()

if __name__ == "__main__":
    main()
