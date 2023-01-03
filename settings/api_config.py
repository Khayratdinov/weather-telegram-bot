from sqlalchemy import create_engine

geo_key = "d571e1c5-3443-4d05-a1de-33e105ffd4bf"


weather_key = {"X-Yandex-API-Key": "e5f5f8fa-616f-42e4-8e4c-3950f5ddb1dc"}


engine = create_engine('postgresql+psycopg2://postgres:admin12345@localhost:5432/botdb', echo=True)


