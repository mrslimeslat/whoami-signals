import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🟢 WHOAMI Signal Bot is connected!\n\n"
        "I'm ready to send you trading signals."
    )


def main():
    if not TOKEN:
        raise RuntimeError("TELEGRAM_BOT_TOKEN is not set.")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("WHOAMI Signal Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
