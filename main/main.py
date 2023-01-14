import telebot
import moviepy.editor
bot = telebot.TeleBot('TOKEN')

@bot.message_handler(content_types=['video'])
def video_to_audio(message):
    try:
        '''get_vidoe'''
        bot.reply_to(message, "Ожидайте...")

        chat_id = message.chat.id

        file_info = bot.get_file(message.video.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src = (f'./media/{message.chat.id}.mp4')
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)


        '''CONVERT'''
        video_file = Path(f'./media/{message.chat.id}.mp4')

        video = moviepy.editor.VideoFileClip(f'{video_file}')
        audio = video.audio
        audio.write_audiofile(f'./media/{video_file.stem}.mp3')


        '''out_audio'''
        audio = open(f'./media/{video_file.stem}.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)

    except Exception as e:
        print(e)

@bot.message_handler(content_types = ['text'])
def bot_message(message):
    if message.chat.type == 'private':
        bot.send_message(message.chat.id, "Отправьте картинку.")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Отправьте картинку.")

bot.polling(none_stop=True, interval=0)
