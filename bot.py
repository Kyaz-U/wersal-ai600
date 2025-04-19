from ai_modules.dynamic_model import run_dynamic_predictions
import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

ADMIN_ID = 92058415
user_stats = {}

menu = ReplyKeyboardMarkup(
    keyboard=[
        ["▶️ Signal olish"],
        ["ℹ️ Yordam", "⚙️ Sozlamalar"],
        ["📊 Statistika"]
    ],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalomu alaykum, Wersal AI botiga xush kelibsiz!\nKerakli bo‘limni tanlang:",
        reply_markup=menu
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text

    # Statistika yozib borish
    if user_id in user_stats:
        user_stats[user_id] += 1
    else:
        user_stats[user_id] = 1

    if text == "▶️ Signal olish":
        result = run_dynamic_predictions()
        await update.message.reply_text(result)

    elif text == "ℹ️ Yordam":
        await update.message.reply_text("Yordam uchun: @UlugbekYusupov ga murojaat qiling.")

    elif text == "⚙️ Sozlamalar":
        await update.message.reply_text("Sozlamalar hali mavjud emas. Tez orada yangilanadi.")

    elif text == "📊 Statistika":
        await show_stats(update, context)

    else:
        await update.message.reply_text("Iltimos, menyudagi tugmalardan birini tanlang.")

async def show_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == ADMIN_ID:
        message = "📊 Foydalanuvchi statistikasi:\n"
        for uid, count in user_stats.items():
            message += f"🆔 ID: {uid}, So‘rovlar soni: {count}\n"
        await update.message.reply_text(message)
    else:
        await update.message.reply_text("Bu buyruq faqat admin uchun!")

if __name__ == "__main__":
    token = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()
