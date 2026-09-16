import os
import threading
import random
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

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 TRC AI SIGNAL BOT\n\n"
        "✅ Bot is Online!\n"
        "📊 Use /signal for a test signal."
    )

# /signal
async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    signals = [
        ("🟢 CALL", 87),
        ("🔴 PUT", 84),
        ("🟡 WAIT", 61)
    ]

    signal_name, confidence = random.choice(signals)

    message = (
        "🤖 TRC AI SIGNAL\n\n"
        f"📊 Signal: {signal_name}\n"
        f"📈 Confidence: {confidence}%\n"
        "⏱️ Timeframe: M1\n"
        "⚠️ TEST SIGNAL — Not financial advice"
    )

    await update.message.reply_text(message)

# Start web server
threading.Thread(target=run_web, daemon=True).start()

# Telegram bot
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("signal", signal))

print("🤖 TRC AI Signal Bot is running...")

app.run_polling()
