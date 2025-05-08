from telegram import Update
from telegram.ext import CallbackContext

def admin_commands(update: Update, context: CallbackContext):
    # Admin komutları burada olacak
    update.message.reply_text("Admin komutları aktif.")
