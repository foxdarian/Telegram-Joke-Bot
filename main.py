import os
import logging
import aiohttp

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("TOKEN")


# Set up logging to help with debugging and monitoring the bot's activity
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    logger.info(f"User {update.effective_user.id} started the conversation.")

    reply_markup = InlineKeyboardMarkup(
        [[InlineKeyboardButton("Get a joke", callback_data='get_joke')]]
    )

    await update.message.reply_text("Hello! This bot can send to you jokes. Click on the button below to get a joke!", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle button clicks."""
    query = update.callback_query
    await query.answer() # Acknowledge the button click to prevent the loading animation from persisting on the user's end

    if query.data == 'get_joke':
        API_URL = "https://api.chucknorris.io/jokes/random"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(API_URL) as response:
                    if response.status == 200:
                        data = await response.json()
                        joke = data.get("value", "Sorry, couldn't fetch a joke at the moment.")
                        await query.edit_message_text(text=joke)
                    else:
                        logger.error(f"Failed to fetch joke. Status code: {response.status}")
                        await query.edit_message_text(text="Sorry, couldn't fetch a joke at the moment.")
        except Exception as e:
            logger.error(msg="Exception while fetching joke:", exc_info=e)
            await query.edit_message_text(text="Sorry, couldn't fetch a joke at the moment.")


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log the error and send a message to the user."""
    logger.error(msg="Exception while handling an update:", exc_info=context.error)

    if isinstance(update, Update) and update.message:
        try:
            await update.message.reply_text("An error occurred while processing your request. Please try again later.")
        except Exception as e:
            logger.error(msg="Failed to send error message to user:", exc_info=e)


def main():
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.add_error_handler(error_handler) # Error handler to log any exceptions that occur during the bot's operation

    application.run_polling() # Start the bot and keep it running until interrupted

if __name__ == '__main__':
    main()