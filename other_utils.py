from datetime import date
from datetime import timedelta

# Defining a dictionary with names of weekdays
weekdays = {0: 'Poniedziałek',
            1: 'Wtorek',
            2: 'Środa',
            3: 'Czwartek',
            4: 'Piątek',
            5: 'Sobota',
            6: 'Niedziela'}

# Defining a dictionary with cities
cities = {'Toruń': ['Toruń', 53.013748, 18.598141],
            'Kraków': ['Kraków', 50.083328, 19.91667],
            'Warszawa': ['Warszawa', 52.23547, 21.04191],
            'Łódź': ['Łódź', 51.75, 19.466669],
            'Gdańsk': ['Gdańsk', 54.361118, 18.68976],
            'Poznań': ['Poznań', 52.406189, 16.92341],
            'Lublin': ['Lublin', 51.25, 22.566669],
            'Zakopane': ['Zakopane', 49.298988, 19.948851],
            'Wrocław': ['Wrocław', 51.099998, 17.033331],
            'Szczecin': ['Szczecin', 53.42894, 14.55302],
            'Rzeszów': ['Rzeszów', 50.005402, 21.9884],
            'Częstochowa': ['Częstochowa', 50.796459, 19.12409],
            'Suwałki': ['Suwałki', 54.102718, 22.92914]}

# Defining a dictionary with labels for plots
plots_labels = {'temp': 'Temperatura',
                'feels_like': 'Odczuwalna',
                'pressure': 'Ciśnienie',
                'humidity': 'Wilgotność'}


# Generating five previous days
def generate_previous_days():
    previous_days = []
    for i in range(1, 6):
        previous = date.today() - timedelta(days=i)
        previous_days.append(previous)
    return previous_days
