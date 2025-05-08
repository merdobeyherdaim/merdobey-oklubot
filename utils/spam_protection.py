from telegram import Update
from telegram.ext import CallbackContext

def check_spam(update: Update, context: CallbackContext):
    # Spam mesajları engelleme işlemi
    user_message = update.message.text
    if "spam" in user_message.lower():
        update.message.reply_text("Spam mesajlar engellendi!")
        update.message.delete()
