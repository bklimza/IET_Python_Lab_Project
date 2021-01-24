import tkinter.ttk as ttk
import time
import calendar
from current_weather_utils import *
from forecast_weather_utils import *
from archival_weather_utils import *

# Creating a window
window = tk.Tk()

# Defining a window size
window.geometry("400x270")

# Defining a new icon
window.iconbitmap("weather.ico")

# Defining a window name
window.title('Pogoda')

# Defining new background color
window.config(background='white')


# Defining a function with actions for the start button
def start_button_actions():
    try:
        if int_var1.get() == 1:
            create_current_weather_window(stations_str_var.get())
        elif int_var1.get() == 2:
            str_vars_get = [str_var.get() for str_var in str_vars if not str_var.get() == '']
            day = calendar.timegm(time.strptime(days_str_var.get(), "%Y-%m-%d"))
            create_previous_day_data_chart(stations_str_var.get(), day, str_vars_get, days_str_var.get())
        elif int_var1.get() == 3:
            create_daily_forecast_weather_window(stations_str_var.get())
    except (KeyError, ValueError):
        pass


# Adding labels
station_label = tk.Label(window, text="Dzień", background='white')
station_label.place(x=240, y=82)

day_label = tk.Label(window, text="Miasto", background='white')
day_label.place(x=240, y=32)

# Adding a combo box with cities
stations_str_var = tk.StringVar()
stations_combo_box = ttk.Combobox(window, textvariable=stations_str_var, background='white')
stations_combo_box.place(x=240, y=52)
stations_combo_box['values'] = list(cities.keys())

# Adding check buttons
int_var1 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Pokaż aktualną pogodę', variable=int_var1, onvalue=1, background='white')
c1.place(x=10, y=30)

c2 = tk.Checkbutton(window, text='Pokaż dane z poprzedniego dnia', variable=int_var1, onvalue=2, background='white')
c2.place(x=10, y=60)

c3 = tk.Checkbutton(window, text='Pokaż prognozę na kilka dni', variable=int_var1, onvalue=3, background='white')
c3.place(x=10, y=210)

# -------------------------------------------------------

str_vars = [tk.StringVar() for _ in range(4)]
c4 = tk.Checkbutton(window, text='Temperatura', variable=str_vars[0], onvalue='temp', offvalue='', background='white')
c4.place(x=40, y=90)

c5 = tk.Checkbutton(window, text='Temperatura odczuwalna', variable=str_vars[1], onvalue='feels_like', offvalue='', background='white')
c5.place(x=40, y=120)

c6 = tk.Checkbutton(window, text='Ciśnienie', variable=str_vars[2], onvalue='pressure', offvalue='', background='white')
c6.place(x=40, y=150)

c7 = tk.Checkbutton(window, text='Wilgotność', variable=str_vars[3], onvalue='humidity', offvalue='', background='white')
c7.place(x=40, y=180)

# Adding a combo box with days
days_str_var = tk.StringVar()
stations_combo_box = ttk.Combobox(window, textvariable=days_str_var, background='white')
stations_combo_box.place(x=240, y=102)
stations_combo_box['values'] = generate_previous_days()

# Adding a start button
start_button = tk.Button(window, text='Uruchom', height=3, width=19, command=start_button_actions, background='white')
start_button.place(x=240, y=180)

window.mainloop()
