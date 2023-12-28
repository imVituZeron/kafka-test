import requests, json
from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'])

for _ in range(3):
    response = requests.get("https://api.adviceslip.com/advice")
    datas = json.loads(response.text) # formating json in dictonary
    data = f"{datas['slip']['id']}--{datas['slip']['advice']}"

    payload = bytes(data, encoding="utf8")
    producer.send('ADVICES', payload)

producer.flush()