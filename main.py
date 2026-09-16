import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.getenv("PORT", 10000))

# Web server
web = Flask(__name__)

@web.route("/")
def home():
    return "TRC AI Signal Bot is Online!"

def run_web():
    web.run(host="0.0.0.0", port=PORT)

# Telegram command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 TRC AI SIGNAL BOT\n\n"
        "✅ Bot is online!\n"
        "📊 AI Signal System Coming Soon..."
    )

# Start web server
threading.Thread(target=run_web, daemon=True).start()

# Start Telegram bot
app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("🤖 TRC AI Signal Bot is running...")

app.run_polling()
