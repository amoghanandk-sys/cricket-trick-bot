import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ All Tricks Tracking Enabled\n\n"
        "Manual triggers:\n"
        "🎯 Catch Drop\n"
        "🤕 Captain Injured\n"
        "🔄 Dead Rubber\n"
        "💥 Last Ball Six\n"
        "⚡ First Spell 2 Wickets\n"
        "🎲 51 Ball Theory"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot running...")
app.run_polling(
