import telebot
import keras
import numpy as np
from PIL import Image, ImageOps

from telebot import types
bot = telebot.TeleBot('YOUR TOKEN')
IMG_SIZE = 32
model = keras.models.load_model("/Users/temirlan/Desktop/my_model.h5")

my_dict = { 0:'а', 1:'ә', 2:'з', 3:'и', 4:'й', 5:'к', 
            6:'қ', 7:'л', 8:'м', 9:'н', 10:'ң', 11:'о',
            12:'б', 13:'ө', 14:'п', 15:'р', 16:'с', 17:'т',
            18:'у', 19:'ұ', 20:'ү', 21:'ф', 22:'х', 23:'в',
            24:'ц', 25:'ч', 26:'ш', 27:'щ', 28:'һ', 29:'ъ',
            30:'ы', 31:'і', 32:'ь', 33:'э', 34:'г', 35:'ю',
            36:'я', 37:'ғ', 38:'д', 39:'е', 40:'ё', 41:'ж'}

@bot.message_handler(content_types=['photo'])
def photo(message):   

    fileID = message.photo[-1].file_id   
    print(fileID)
    file = bot.get_file(fileID)
    downloaded_file = bot.download_file(file.file_path)
    with open("/Users/temirlan/ADP/image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)
    
    img = Image.open('/Users/temirlan/ADP/image.jpg')
    img = img.resize((IMG_SIZE, IMG_SIZE))
    img = ImageOps.grayscale(img)
    img.save("/Users/temirlan/ADP/grey_image.jpg")

    img_array = np.array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)

    prediction_class = np.argmax(prediction)
    prediction_class = int(prediction_class)
    print(prediction_class)
    print(type(prediction_class))
    bot.send_message(message.chat.id, "You predicted this character: {}".format(my_dict[prediction_class]))

@bot.message_handler(content_types = ['text'])
def bot_message(message):
    if message.chat.type == 'private':
        bot.send_message(message.chat.id, "Send image of the character, please.")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Send image of the character, please.")

bot.polling(none_stop=True, interval=1)