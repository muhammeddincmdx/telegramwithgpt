import aiogram
import openai

# GPT-3 ile etkileşim için OpenAI API token'ınızı buraya girin
openai.api_key = "OpenAi-Api-Key"

# Telegram botu için token'ınızı buraya girin
bot_token = "Telegram Token"

# AIogram ile botu başlatın
bot = aiogram.Bot(token=bot_token)
dp = aiogram.Dispatcher(bot)
# Gelen mesajları işlemek için bir komut tanımlayın
@dp.message_handler(commands=['start'])
async def handle_start(message: aiogram.types.Message):
    # Bot ilk çalıştığında "Merhaba, nasılsın?" mesajını gönderin
    await message.reply("Merhaba, nasılsın?")

# Gelen mesajları işlemek için bir komut tanımlayın
@dp.message_handler()
async def handle_message(message: aiogram.types.Message):
    # Gelen mesajı GPT-3'e gönderin ve cevap alın
    response = openai.Completion.create(
        engine='text-davinci-003',  # GPT-3 motorunu seçin
        prompt=message.text,  # Gelen mesajı GPT-3'e giriş olarak verin
        max_tokens=1000,  # Cevapta en fazla 50 token olmasını sağlayın
        temperature=0.7  # Daha yaratıcı cevaplar için sıcaklığı ayarlayın
    )
    # GPT-3'ten gelen cevabı Telegram'a gönderin
    await message.reply(response.choices[0].text)

# Botu çalıştırın
aiogram.executor.start_polling(dp)
