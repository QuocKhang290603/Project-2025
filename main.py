from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes,MessageHandler,filters,CallbackContext

#async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE)
#async def show_data(update: Update, context: ContextTypes.DEFAULT_TYPE)

if __name__=='__main__':
    token_telegram='7855492175:AAG9wKVXsbBZiMqP9L04kJMUMjOnumOVDyA'
    app = ApplicationBuilder().token(token_telegram).build()
    # Lắng nghe tin nhắn chứa file
    #app.add_handler(MessageHandler(filters.Document.ALL, handle_file))
    #app.add_handler(CommandHandler('show_data',show_data))
    app.run_polling()