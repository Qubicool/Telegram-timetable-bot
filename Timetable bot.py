import telebot           #Импортируем библиотеки
import requests            #Импортируем библиотеки
from datetime import date,time,datetime  #Импортируем библиотеки
from telebot import types  #Импортируем библиотеки
bot = telebot.TeleBot('import your token') #Вставляем токен своего бота

@bot.message_handler(commands=['start','help']) 
def send_welcome(message): 
    bot.reply_to(message, f'Я бот. Приятно познакомиться!') 
    keyboard = types.InlineKeyboardMarkup()

    key_weather = types.InlineKeyboardButton(text='Погода',callback_data = 'comm_wttr')
    keyboard.add(key_weather)
    
    key_timetable = types.InlineKeyboardButton(text='Расписание', callback_data = 'comm_timetable')
    keyboard.add(key_timetable)

    key_crtime = types.InlineKeyboardButton(text='Время', callback_data = 'comm_crtime')
    keyboard.add(key_crtime)

    bot.send_message(message.from_user.id, text='Выбери что ты хочешь от меня узнать', reply_markup=keyboard)

@bot.message_handler(content_types=['text']) 
def get_text_messgaes(message): 
    if message.text == 'Привет': 
        bot.send_message(message.chat.id,'Привет! Для начала напиши мне команды /start \n /help ') 
    elif message.text == 'Пока': 
        bot.send_message(message.chat.id,'Пока!') 
    else:
        bot.send_message(message.chat.id,'Я не знаю таких слов(')


@bot.callback_query_handler(func=lambda call:call.data.startswith('comm_'))
def callback_worker_class(call):
    if call.data == 'comm_wttr':
        today = str(date.today()) #В переменную today сохраняем текущую дату
        wtr = requests.get('https://wttr.in/Omsk?format=%l:+%c+%t\n', stream=True) # запрашиваем с сайта данные в определенном формате,
        data = wtr.raw.read().decode('utf-8') # декодируем данные в Utf-8, далее аналогично подробнее про форматы https://wttr.in/:help
        wtr = requests.get('https://wttr.in/Omsk?format=%f\n', stream=True)
        data1 = wtr.raw.read().decode('utf-8')
        wtr = requests.get('https://wttr.in/Omsk?format=%w\n', stream=True)
        data2= wtr.raw.read().decode('utf-8')
        new_data = data.replace('Omsk', 'Омске')# Меняем слово Omsk На Омск
        bot.send_message(call.from_user.id, f'Дата сегодня: {today}  \nПогода в {new_data} \nОщущается как: {data1} \nВетер: {data2} ')
    elif call.data == 'comm_timetable':
        keyboard = types.InlineKeyboardMarkup() 
        key_socialeconom = types.InlineKeyboardButton(text='11 c/э', callback_data='class_1se')  
        keyboard.add(key_socialeconom)
        key_technology = types.InlineKeyboardButton(text='11 ф/м', callback_data='class_tech') 
        keyboard.add(key_technology)
        key_himbio = types.InlineKeyboardButton(text='11 х/б ', callback_data='class_himbio') 
        keyboard.add(key_himbio)
        key_socialeconomm = types.InlineKeyboardButton(text='11 с/э 2', callback_data='class_2se') 
        keyboard.add(key_socialeconomm)
        bot.send_message(call.from_user.id, text='Выбери свой класс', reply_markup=keyboard)
    elif call.data == 'comm_crtime':
        time = requests.get('https://wttr.in/Omsk?format=%l:+%T', stream=True)
        data = time.raw.read().decode('utf-8')
        bot.send_message(call.from_user.id,text= 'Текущее время:')
        data1 = data[:14]
        bot.send_message(call.from_user.id,text= data1)

    else:
        bot.send_message(call.from_user.id,'error:)')

@bot.callback_query_handler(func=lambda call: call.data.startswith('class_')) #обработчик нажатия на класс( из 4-х предложенных)
def callback_worker_class(call): 
    if call.data == 'class_1se': 
        keyboard = types.InlineKeyboardMarkup()# Говорим, что будем создавать inline клавиатуру, а не reply
        key_monday = types.InlineKeyboardButton(text='Понедельник', callback_data='day_Monday') # К каждому дню идет свой ключ, который соответствует классам
        key_tuesday = types.InlineKeyboardButton(text='Вторник', callback_data='day_Tuesday') 
        key_wednesday = types.InlineKeyboardButton(text='Среда', callback_data='day_Wednesday') 
        key_thursday = types.InlineKeyboardButton(text='Четверг', callback_data='day_Thursday')
        key_friday = types.InlineKeyboardButton(text='Пятница', callback_data='day_Friday') 
        key_sunday = types.InlineKeyboardButton(text='Суббота', callback_data='day_Sunday') 
        keyboard.add(key_monday,key_tuesday,key_wednesday, key_thursday,key_friday, key_sunday)
        bot.send_message(call.from_user.id,text='Выбери день недели', reply_markup=keyboard)
    elif call.data == 'class_tech': 
        keyboard = types.InlineKeyboardMarkup()
        key_mondayT = types.InlineKeyboardButton(text='Понедельник', callback_data='day_MondayT') #Объявляем кнопки
        key_tuesdayT = types.InlineKeyboardButton(text='Вторник', callback_data='day_TuesdayT') 
        key_wednesdayT = types.InlineKeyboardButton(text='Среда', callback_data='day_WednesdayT') 
        key_thursdayT = types.InlineKeyboardButton(text='Четверг', callback_data='day_ThursdayT')
        key_fridayT = types.InlineKeyboardButton(text='Пятница', callback_data='day_FridayT') 
        key_sundayT = types.InlineKeyboardButton(text='Суббота', callback_data='day_SundayT') 
        keyboard.add(key_mondayT,key_tuesdayT,key_wednesdayT, key_thursdayT,key_fridayT, key_sundayT)#Добавляем их
        bot.send_message(call.from_user.id,text='Выбери день недели', reply_markup=keyboard)
    elif call.data == 'class_2se': 
        keyboard = types.InlineKeyboardMarkup()
        key_monday2s = types.InlineKeyboardButton(text='Понедельник', callback_data='day_Monday2s') 
        key_tuesday2s = types.InlineKeyboardButton(text='Вторник', callback_data='day_Tuesday2s') 
        key_wednesday2s = types.InlineKeyboardButton(text='Среда', callback_data='day_Wednesday2s') 
        key_thursday2s = types.InlineKeyboardButton(text='Четверг', callback_data='day_Thursday2s')
        key_friday2s = types.InlineKeyboardButton(text='Пятница', callback_data='day_Friday2s') 
        key_sunday2s = types.InlineKeyboardButton(text='Суббота', callback_data='day_Sunday2s') 
        keyboard.add(key_monday2s,key_tuesday2s,key_wednesday2s, key_thursday2s,key_friday2s, key_sunday2s)
        bot.send_message(call.from_user.id,text='Выбери день недели', reply_markup=keyboard)
    elif call.data == 'class_himbio': 
        keyboard = types.InlineKeyboardMarkup()
        key_mondayh = types.InlineKeyboardButton(text='Понедельник', callback_data='day_Mondayh') 
        key_tuesdayh = types.InlineKeyboardButton(text='Вторник', callback_data='day_Tuesdayh') 
        key_wednesdayh = types.InlineKeyboardButton(text='Среда', callback_data='day_Wednesdayh') 
        key_thursdayh = types.InlineKeyboardButton(text='Четверг', callback_data='day_Thursdayh')
        key_fridayh = types.InlineKeyboardButton(text='Пятница', callback_data='day_Fridayh') 
        key_sundayh = types.InlineKeyboardButton(text='Суббота', callback_data='day_Sundayh') 
        keyboard.add(key_mondayh,key_tuesdayh,key_wednesdayh, key_thursdayh,key_fridayh, key_sundayh)
        bot.send_message(call.from_user.id,text='Выбери день недели', reply_markup=keyboard)



@bot.callback_query_handler(func=lambda call: call.data.startswith('day_'))# Обработчик нажатия на дни, каждому дню соответсвует свой уникальный ключ,                                                                            # кот
def callback_worker_day(call):                                             # который и ищем в условии if
    if call.data == 'day_Monday': 
        msg = 'В понедельник уроки у 11 c/э1:\n1)Математика\n2)Химия\n3)Общество\n4)Общество\n5)Биология\n6)Русский'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'day_Tuesday': 
        msg = 'Во вторник уроки у 11 c/э1:\n1)Математика\n2)Математика\n3)Литература\n4)Литература\n5)ОБЖ\n6)Физ-ра'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'day_Wednesday': 
        msg = 'В среду уроки у 11 c/э1:\n1)Право\n2)Информатика\n3)Русский в вопросах\n4)Литература\n5)Экономика\n6)Экономика'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'day_Thursday': 
        msg = 'В четверг уроки у 11 c/э1:\n1)Математика\n2)Английский\n3)Физика\n4)Физика\n5)Родной язык\n6)Математика'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'day_Friday': 
        msg = 'В пятницу уроки у 11 c/э1:\n1)Математика\n2)Астрономия\n3)Английский\n4)Английский\n5)История\n6)История\n7)РНЗМ'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'day_Sunday': 
        msg = 'В субботу уроки у 11 c/э1:\n1)Химия\n2)Право\n3)Решение задач по физике\n4)ИПД\n5)Физ-ра\n6)География'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'day_MondayT': 
        msg = 'Во понедельник уроки у 11 тех:\n1)Английский\n2)Английский\n3)Русский в вопросах\n4)Математика\n5)Русский\n6)Химия'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'day_TuesdayT': 
        msg = 'Во вторник уроки у 11 тех:\n1)Литература\n2)Литература\n3)Физика\n4)Физика\n5)Математика\n6)Физ-ра\n'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'day_WednesdayT': 
        msg = 'Во среду уроки у 11 тех:\n1)Математика\n2)Математика\n3)Общество\n4)Английский\n5)Информ\n6)Информ\n'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'day_ThursdayT': 
        msg = 'В четверг уроки у 11 тех:\n1)Физика\n2)Физика\n3)Математика\n4)Математика\n5)Химия\n6)ОБЖ\n'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'day_FridayT': 
        msg = 'В пятницу уроки у 11 тех:\n1)История\n2)История\n3)Астрономия\n4)Информатика\n5)Информатика\n6)Родной язык\n7)Инженер. графика\n'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'day_SundayT': 
        msg = 'В субботу уроки у 11 тех:\n1)РНЗМ\n2)Физика\n3)ИПД\n4)Литература\n5)Физ-ра\n6)Биология\n'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'day_Monday2s':
        msg ='В понедельник уроки у 11c/э2 :\n1)Химия\n2)Математика\n3)Математика\n4)Биология\n5)Обществознание\n6)Обществознание\n'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'day_Tuesday2s': 
        msg = 'Во вторник уроки у 11 c/э2:\n1)Астрономия\n2)Литература\n3)Литература\n4)Русский в вопросах\n5)Физика\n6)Физика\n7)Физ-ра'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'day_Wednesday2s': 
        msg = 'В среду уроки у 11 c/э2:\n1)Информатика\n2)Право\n3)Экономика\n4)Экономика\n5)Математика\n6)Математика\n'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'day_Thursday2s': 
        msg = 'В четверг уроки у 11 c/э2:\n1)Английский\n2)Литература\n3)Русский\n4)Родной язык\n5)ОБЖ\n6)Химия\n'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'day_Friday2s': 
        msg = 'В пятницу уроки у 11 c/э2:\n1)Английский\n2)Английский\n3)История\n4)История\n5)Математика\n6)Математика\n'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'day_Sundays2s': 
        msg = 'В субботу уроки у 11 c/э2:\n1)Право\n2)РНЗМ\n3)География\n4)Физ-ра\n5)ИПД\n6)Решение задач по физике\n'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'day_Mondayh':
        msg ='В понедельник уроки у 11 х/б :\n1)Русский\n2)ОБЖ\n3)Английский\n4)Английский\n5)Математика\n6)\Биологияn'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'day_Tuesdayh': 
        msg = 'Во вторник уроки у 11 х/б:\n1)Физика\n2)Физика\n3)Биология\n4)Математика\n5)Химия\n6)Решение задач по химии\n7)Физкультура'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'day_Wednesdayh': 
        msg = 'В среду уроки у 11 х/б:\n1)Биология\n2)Английский\n3)Общая биология\n4)Обществознание\n5)Обществознание\n6)Русский в вопросах\n'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'day_Thursdayh': 
        msg = 'В четверг уроки у 11 х/б:\n1)Математика\n2)Математика\n3)Родной язык\n4)Химия\n5)История\n6)История\n'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'day_Fridayh': 
        msg = 'В пятницу уроки у 11 х/б:\n1)Астрономия\n2)Литература\n3)Математика\n4)Математика\n5)Литература\n6)Информатика\n'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'day_Sundayh': 
        msg = 'В субботу уроки у 11 х/б:\n1)Экология\n2)Химия\n3)Литература\n4)Физкультура\n5)География\n6)ИПД\n'
        bot.send_message(call.message.chat.id, msg)
    
    
    
bot.polling()