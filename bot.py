from aiogram import Bot, Dispatcher, executor, types
#bot init

bot = Bot(token="5481361012:AAHKpUuqMQrehX4eud8ZKcG4Jd_fwWmBekE")

dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
  file = open("msg.txt", "w")
  txt = message.text
  file.write = (txt + "\n")
  file.close()

  if txt == "/start":
    ans = "Привет, я был создан для признания в любви! \n"
    ans += "Введи свою ФИО и я скажу кто тебя любит)"
    await message.answer(ans)
  elif txt == "Таран Анастасия Владимировна":
    ans = "Тебя любит ->"
    await message.answer(ans)

#run long-poling

if __name__ == "__main__":
  executor.start_polling(dp, skip_updates=True)
