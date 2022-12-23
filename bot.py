import logging
import telegram.ext
from telegram.ext import (CommandHandler, MessageHandler, Updater)
from get_movie_series import (get_recommendation, get_similar, get_series)
from get_memes_reddit import getMeme
from get_quotes import quote_generator

Token = "5719692431:AAE3hb7S6SPe8eIoSgDuqxhIRWG8vNDoP2I"


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="""
        What's up buddy
        Here are the list of commands that you can try
        /similar->Get similar movies
        /recommend-> Get a random movie recommendation
        /series->Get a random popular series Happy Binging:)
        /meme -> Get a popular meme
        /quote ->Get a random quote
        """)


def recommend(update, context):
    response = get_recommendation()
    print(response["poster"])
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Movie Recommendation\n\nTitle : {}\n\nOverview : {}\n".format(response["title"], response["overview"]))
    context.bot.send_photo(
        chat_id=update.effective_chat.id, photo=response["poster"], caption="Here's the poster.")


def similar(update, context):
    message = update.message.text.replace('/similar', '').strip()
    if message == '':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Type a movie after "/similar" to get similar movies')
    else:
        response = get_similar(message)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Movie Recommendation\n\nTitle : {}\n\nOverview : {}\n".format(response["title"],
                                                                                response["overview"]))
        context.bot.send_photo(
            chat_id=update.effective_chat.id, photo=response["poster"], caption="Here's the poster.")


def series(update, context):
    response = get_series()
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Series Recommendation\n\nTitle : {}\n\nOverview : {}\n".format(response["title"], response["overview"]))
    context.bot.send_photo(
        chat_id=update.effective_chat.id, photo=response["poster"], caption="Here's the poster.")


def meme(update, context):
    response = getMeme()
    print(response)
    context.bot.send_photo(
        chat_id=update.effective_chat.id, photo=response, caption="Here's the Meme.")


def quotes(update, context):
    response = quote_generator()
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Quote : {}\n\nAuthor : {}\n".format(response["content"], response["author"]))


if __name__ == '__main__':
    updater = Updater(token=Token, use_context=True)
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    similar_handler = CommandHandler('similar', similar)
    dispatcher.add_handler(similar_handler)

    recommend_handler = CommandHandler('recommend', recommend)
    dispatcher.add_handler(recommend_handler)

    series_handler = CommandHandler('series', series)
    dispatcher.add_handler(series_handler)

    memes_handler = CommandHandler('meme', meme)
    dispatcher.add_handler(memes_handler)

    quote_handler = CommandHandler('quote', quotes)
    dispatcher.add_handler(quote_handler)

    updater.start_polling()
    updater.idle()
