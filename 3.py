from tkinter import *
import requests
from datetime import *
import locale

  

def clicked():  
    a1=txt.get()
    try:
        req=requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={a1}&lang=ru&units=metric&appid={'b4d12d9266ad8521558be286fb5d1c81'}'
        )
        data=req.json()

        cloud=data['clouds']['all']
        temp=data['main']['temp']
        feelstemp=data['main']['feels_like']
        maxtemp=data['main']['temp_max']
        mintemp=data['main']['temp_min']
        vlazh=data['main']['humidity']
        davlenie=data['main']['pressure']
        visibil=data['visibility']
        wind=data['wind']['speed']
        city=data['name']
        wethdesc=data['weather'][0]['description']

        locale.setlocale(locale.LC_ALL, 'ru_RU')
        time = datetime.now(timezone.utc)
        day_of_the_month = time.strftime("%d")
        day_of_the_week = time.strftime(("%A"))
        month = time.strftime("%B")
        year = time.strftime("%Y")
        format_of_time = time.strftime("%H:%M:%S")

        a21='Сегодня', day_of_the_week+'.', 'День:', day_of_the_month+'.', 'Месяц:', month+'.', 'Год:',year+'.'
        a2=Label(window,text=a21,font='Arial')
        a2.grid(column=0,row=1)
        a31='Время по UTC: ', format_of_time+'.'
        a3=Label(window,text=a31,font='Arial')
        a3.grid(column=0,row=2)
        a4=Label(window,text=f'Выбранный город: {city}.\nСегодня {wethdesc}.',font='Arial') 
        a4.grid(column=0,row=3)       

        if data.get('snow',False)!=False:
            if data['snow'].get('1h',False)!=False:
                snow1=data['snow']['1h']
                a5=Label(window,text=f'Выпало осадков за последний час: {snow1} мм.',font='Arial')
                a5.grid(column=0,row=4)
            else:
                snow3=data['snow']['3h']
                a6=Label(window,text=f'Выпало осадков за последние три часа: {snow3} мм.',font='Arial')
                a6.grid(column=0,row=5)
        elif data.get('rain',False)!=False:
            if data['rain'].get('1h',False)!=False:
                rain1=data['rain']['1h']
                a7=Label(window,text=f'Выпало осадков за последний час: {rain1} мм.',font='Arial')
                a7.grid(column=0,row=4)
            else:
                rain3=data['rain']['3h']
                a8=Label(window,text=f'Выпало осадков за последние три часа: {rain3} мм.',font='Arial')
                a8.grid(column=0,row=5)

        if data.get('snow',False)!=False:
            a9=Label(window,text=f'Температура: {temp}°C, ощущается как {feelstemp}°C.\nМаксимальная/минимальная температуры: {maxtemp}°C/{mintemp}°C.\nОблачность: {cloud}%.\nВлажность: {vlazh}%.\nДавление: {davlenie} гектопаскаль.\nВидимость: {visibil} метров.\nСкорость ветра: {wind} м/с.\n\nХорошего дня!',font='Arial')
            a9.grid(column=0,row=6)
        else:
            a9=Label(window,text=f'Температура: {temp}°C, ощущается как {feelstemp}°C.\nМаксимальная/минимальная температуры: {maxtemp}°C/{mintemp}°C.\nОблачность: {cloud}%.\nВлажность: {vlazh}%.\nДавление: {davlenie} гектопаскаль.\nВидимость: {visibil} метров.\nСкорость ветра: {wind} м/с.\n\nХорошего дня!',font='Arial')
            a9.grid(column=0,row=4)

    except Exception as ex:
        a10=Label(window,text='Данный город не найден.',font='Arial')
        a10.grid(column=0,row=1)
    
      

window = Tk()  
window.title('Погода')  
window.geometry('500x500')  
lbl = Label(window, text='Введите город')  
lbl.grid(column=0, row=0)  
txt = Entry(window,width=10)  
txt.grid(column=1, row=0)  
btn = Button(window, text='Поиск погоды', command=clicked)  
btn.grid(column=2, row=0) 
window.mainloop()