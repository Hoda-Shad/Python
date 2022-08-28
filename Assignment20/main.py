import telebot
import random
from khayyam import JalaliDate, JalaliDatetime
from gtts import gTTS
import qrcode
import pysynth as ps

mybot = telebot.TeleBot("5421189666:AAFSVtlCxMTL6w5uBOpT-hxrzR3J8kJcPrM")


@mybot.message_handler(commands=['start'])
def send_welcome(message):
    name = message.from_user.first_name
    # print(name)
    mybot.reply_to(message, f"سلام {name} خوش اومدی")



mymarkup = telebot.types.ReplyKeyboardMarkup(row_width=1)
btn1 = telebot.types.KeyboardButton('New Game:')

mymarkup.add(btn1)


@mybot.message_handler(commands=['game'])
def game(message):
    mybot.reply_to(message, 'یک عدد حدس بزن بین 0 و 100')
    mybot.register_next_step_handler(message, game2)


bot_num = random.randint(0, 100)


def game2(message):
    if int(message.text) == bot_num:
        mybot.send_message(message.chat.id, 'آفرین برنده شدی')
        mybot.number = random.randint(0, 20)
        mes = mybot.send_message(message.chat.id, 'برای یازی مجدد New Game را کلیک کنید:', reply_markup=mymarkup)
        mybot.register_next_step_handler(mes, game)

    elif int(message.text) > bot_num:
        mybot.send_message(message.chat.id, 'بیا پایین تر')
        mybot.register_next_step_handler(message, game2)

    elif int(message.text) < bot_num:
        mybot.send_message(message.chat.id, 'برو بالاتر')
        mybot.register_next_step_handler(message, game2)


@mybot.message_handler(commands=['age'])
def Birthday(message):
    a = {}
    mybot.reply_to(message, 'تاریخ تولد خود را وارد کن:')
    mybot.register_next_step_handler(message, age)


def age(message):
    a = message.text.split('-')
    print(a)
    print(JalaliDatetime.now())
    age = JalaliDatetime.now() - JalaliDatetime(int(a[0]), int(a[1]), int(a[2]))

    mybot.send_message(message.chat.id, f' سن شما {age} است')


@mybot.message_handler(['voice'])
def voice(message):
    mybot.reply_to(message, 'Enter a sentence in English:')
    mybot.register_next_step_handler(message, converttxtvc)


def converttxtvc(message):
    language = 'en'
    myobj = gTTS(text=message.text, lang=language, slow=False)
    myobj.save("voice.mp3")
    voice = open('voice.mp3', 'rb')
    mybot.send_voice(message.chat.id, voice)

@mybot.message_handler(['max'])
def input_nums(message):
    mybot.reply_to(message, 'اعداد را وارد کنید تا ماکزیمم را برگردانیم')
    mybot.register_next_step_handler(message, find_max)


def find_max(message):
    mynumberes = message.text.split(',')
    list = []
    for i in mynumberes:
        list.append(int(i))
    mybot.send_message(message.chat.id, f' ماکزیمم {max(list)} است')

@mybot.message_handler(['argmax'])
def input_nums(message):
    mybot.reply_to(message, 'اعداد را وارد کنید تا اندیس ماکزیمم را برگردانیم')
    mybot.register_next_step_handler(message, find_argmax)


def find_argmax(message):
    mynumberes = message.text.split(',')
    list = []
    for i in mynumberes:
        list.append(int(i))
    mybot.send_message(message.chat.id, f' اندیس ماکزیمم {list.index(max(list))} است')
    # a = max(list)
    # for i in range(len(list)):
    #     if list[i]==a:
    #         mybot.send_message(message.chat.id, f' اندیس ماکزیمم {i} است')


@mybot.message_handler(['qrcode'])
def inputsen(message):
    mybot.reply_to(message, 'یک چمله وارد کتید')
    mybot.register_next_step_handler(message, makeqrcode)

def makeqrcode(message):
    img = qrcode.make(message.text)
    img.save('qrcode.png')
    image = open('qrcode.png', 'rb')
    mybot.send_photo(message.chat.id, image)

@mybot.message_handler(commands= ['help'])
def show_max(message):
    mybot.reply_to(message, 'Plese send:\n/game if you want help\n/age if you want to know your age.\n/voice if you want to change your sentence to voice\n/max if you want to the maximum number\n/argmax if you want to argument of the maximum number')

@mybot.message_handler(commands=['music'])
def music_input(message):
    mybot.reply_to(message, 'لطفا یک نت را وارد کن:')
    mybot.register_next_step_handler(message, music)

def music(message):
    song = message.text
    ps.make_wav(song, fn="test.wav")
    mybot.send_audio(message.chat.id, audio=open('test.wav', 'rb'))

mybot.polling()
