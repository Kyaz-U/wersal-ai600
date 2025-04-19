from ai_modules.dynamic_model import run_dynamic_predictions
import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

menu = ReplyKeyboardMarkup(
    keyboard=[
        ["▶️ Signal olish"],
        ["ℹ️ Yordam", "⚙️ Sozlamalar"]
    ],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalomu alaykum, Wersal AI botiga xush kelibsiz!\nKerakli bo‘limni tanlang:",
        reply_markup=menu
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "▶️ Signal olish":
        result = run_dynamic_predictions()
        await update.message.reply_text(result)

    elif text == "ℹ️ Yordam":
        await update.message.reply_text("Yordam uchun: @UlugbekYusupov ga murojaat qiling.")

    elif text == "⚙️ Sozlamalar":
        await update.message.reply_text("Sozlamalar hali mavjud emas. Tez orada yangilanadi.")

    else:
        await update.message.reply_text("Iltimos, menyudagi tugmalardan birini tanlang.")

if __name__ == '__main__':
    token = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()
