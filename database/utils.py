import sqlite3 as sq
import ciso8601
from datetime import datetime

sep = '#'


def start_database(database_path):

    global base, cur
    base = sq.connect(database_path)
    cur = base.cursor()
    if base:
        print('Database connected.')

    # with sq.connect(database_path) as con:
    #     cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    date DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    base.commit()


async def register_user(user_id, database_path):
    # with sq.connect(database_path) as con:
    #     cur = con.cursor()

    # Добавляем пользователя в основную таблицу
    cur.execute("""INSERT INTO users VALUES(?, ?)""", (user_id, str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))))

    # Создаем таблицу запросов поиска
    cur.execute(f"""CREATE TABLE IF NOT EXISTS user_{user_id}_requests (
                    user_id INTEGER DEFAULT {user_id},
                    city TEXT,
                    category TEXT,
                    cars TEXT,
                    year_from INT,
                    year_to INT,
                    price_from INT,
                    price_to INT,
                    km_age_from INT,
                    km_age_to INT,
                    displacement_from INT,
                    displacement_to INT,
                    transmission TEXT,
                    gear_type TEXT,
                    body_type TEXT,
                    engine TEXT,
                    section TEXT
                    )
                """)

    # Создаем таблицу поиска автомобилей
    cur.execute(f"""CREATE TABLE IF NOT EXISTS user_{user_id}_search (
                    user_id INTEGER DEFAULT {user_id},
                    publication_date DATETIME,
                    city TEXT,
                    model TEXT,
                    year INT,
                    mileage INT,
                    engine TEXT,
                    transmission TEXT,
                    body_type TEXT,
                    gear_type TEXT,
                    price TEXT,
                    url_link TEXT
                    )
                """)
    base.commit()


async def add_user_request(user_id, database_path, data):
    # with sq.connect(database_path) as con:
    #     cur = con.cursor()
    cars = []
    for car_model in data['catalog_filter']:
        cars.append('#'.join(car_model.values()))
    cur.execute(f"""INSERT INTO user_{user_id}_requests VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (user_id,
                 sep.join([str(x) for x in data['geo_id']]),
                 sep.join(cars),
                 data['category'],
                 data['year_from'],
                 data['year_to'],
                 data['price_from'],
                 data['price_to'],
                 data['km_age_from'],
                 data['km_age_to'],
                 data['displacement_from'],
                 data['displacement_to'],
                 sep.join(data['transmission']),
                 sep.join(data['gear_type']),
                 sep.join(data['body_type_group']),
                 sep.join(data['engine_group']),
                 data['section'])
                )
    base.commit()


async def add_user_search_results(user_id, database_path, cars_data):
    # with sq.connect(database_path) as con:
    #     cur = con.cursor()
    for car in cars_data:
        model = f"{car['vehicle_info']['mark_info']['name']} {car['vehicle_info']['model_info']['name']}"
        year = car['documents']['year']
        mileage = car['state']['mileage']
        date = str(ciso8601.parse_datetime(car['additional_info']['hot_info']['start_time']).replace(tzinfo=None))
        city = car['seller']['location']['region_info']['name']
        engine = car['vehicle_info']['tech_param']['human_name']
        transmission = car['vehicle_info']['tech_param']['transmission']
        body_type = car['vehicle_info']['configuration']['human_name']
        gear_type = car['vehicle_info']['tech_param']['gear_type']
        price = f"{car['price_info']['price']:,} {car['price_info']['currency']}"
        url = '/'.join(['https://auto.ru', car['category'], car['section'], 'sale', car['vehicle_info']['mark_info']['code'].lower(), car['vehicle_info']['model_info']['code'].lower(), car['saleId']])

        cur.execute(f"""INSERT INTO user_{user_id}_search VALUES(?,?,?,?,?,?,?,?,?,?,?,?)""",
                    (user_id, date, city, model, year, mileage, engine,
                     transmission, body_type, gear_type, price, url)
                    )
    base.commit()
