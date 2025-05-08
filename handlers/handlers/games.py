from telegram import Update
from telegram.ext import CallbackContext

def play_game(update: Update, context: CallbackContext):
    # Oyun oynama işlemi burada yapılacak
    update.message.reply_text("Hangi oyunu oynamak istersiniz? /chess, /backgammon vb.")
