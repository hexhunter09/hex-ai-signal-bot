import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 TRC AI SIGNAL BOT\n\n"
        "✅ Bot is online!\n"
        "📊 Signal system coming soon..."
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("TRC AI Signal Bot is running...")

app.run_polling()
