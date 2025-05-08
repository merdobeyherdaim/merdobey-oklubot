import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from handlers import music, games, admin
from utils import translator, tagger, spam_protection

# Bot Token
API_TOKEN = "7708774015:AAEUyPy43HsUHdCOJNQoC30vNjhV4fEvjko"

# Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Bot Commands
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Merhaba, ben bir Telegram botuyum! Yardım almak için /help yazabilirsiniz.")

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("""
    /music - Müzik dinleyebilirsiniz
    /play - Oyunları oynayabilirsiniz
    /translate - Çeviri yapabilirsiniz
    """)

def main():
    # Create the Updater and pass it your bot's token
    updater = Updater(API_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Command Handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    # Add Music, Game, Admin Handlers
    dp.add_handler(CommandHandler("music", music.play_music))
    dp.add_handler(CommandHandler("play", games.play_game))
    dp.add_handler(CommandHandler("admin", admin.admin_commands))

    # Add Spam Protection
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, spam_protection.check_spam))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
