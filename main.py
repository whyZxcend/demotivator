from aiogram import Bot, Dispatcher, executor, types
import photo_editor
from colorama import init, Fore, Style

TOKEN = 'wтокен'

init()

try:
    bot = Bot(token= TOKEN)
    dp = Dispatcher(bot)

    @dp.message_handler(commands=['start'])
    async def start(message: types.Message):
        await bot.send_message(message.from_user.id, 'приветик\nОтправь мне фото с подписью\n\ndeveloper @x0x1dead, исходный код можете просить у него')

    @dp.message_handler(content_types=['photo'])
    async def photo(message):

        await message.photo[-1].download('pic/mem.jpg')      

        if message.caption:
            text = message.caption

            photo_editor.add_text(text)    
            await bot.send_photo(message.from_user.id, photo=open('pic/paste/ok.jpg', 'rb'))
        else:
            await bot.send_message(message.from_user.id, 'Ты забыл добавить подпись')

    if __name__ == '__main__':
        print('Бот успешно запущен')
        executor.start_polling(dp, skip_updates=True)
except:
    print(Fore.RED + 'Вы забыли ввести токен\nЭто можно сделать в файле main.py' + Fore.RESET)
