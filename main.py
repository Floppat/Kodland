from flask import Flask
import random

app = Flask(__name__)

facts = {
'Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.',
'Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.',
'Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время',
'Согласно исследованию, проведенному в 2019 году, более 60% людей отвечают на рабочие сообщения в своих смартфонах в течение 15 минут после того, как они вышли с работы.',
'Один из способов борьбы с технологической зависимостью - это поиск занятий, которые приносят удовольствие и улучшают настроение.',
'Илон Маск утверждает, что социальные сети созданы для того, чтобы удерживать нас внутри платформы, чтобы мы тратили как можно больше времени на просмотр контента.',
'Илон Маск также выступает за регулирование социальных сетей и защиту личных данных пользователей. Он утверждает, что социальные сети собирают огромное количество информации о нас, которую потом можно использовать для манипулирования нашими мыслями и поведением.',
'Социальные сети имеют как позитивные, так и негативные стороны, и мы должны быть более осознанными в использовании этих платформ.'
}
fotos = {
    'https://www.cats.org.uk/media/13136/220325case013.jpg?width=500&height=333.49609375'
    'https://thumbor.forbes.com/thumbor/fit-in/900x510/https://www.forbes.com/advisor/wp-content/uploads/2023/07/top-20-small-dog-breeds.jpeg.jpg'
    'https://arigus.tv/upload/resize_cache/iblock/3b2/680_680_1/yr85idltllgw1hfsgmbqf8dbfhde515n.jpg'
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRspCloTEAW_bbkBNLwHwZ1g-cYFQpAyjP6cxxzSVxp_Q&s'
    'https://upload.wikimedia.org/wikipedia/commons/7/7a/1859-Martinique.web.jpg'
}
@app.route('/')
def index():
    return """<h1>привет это сайт где вы сможете посмотреть рандомный факт</h1>
    <a href="/random_fact">перейти на страницу с рандомным фактом</a>
    <a href="/random_foto">перейти на страницу с рандомным фото</a>
"""
@app.route('/random_fact')
def random_fact():
    return '<h1>Рандомный факт</h1>'f'<p>{random.choice(facts)}</p>'
@app.route('/random_foto')
def random_foto():
    return '<h1>Рандомное фото</h1>' f'<img src={random.choice(fotos)} width = 600px>'
app.run(debug=True)
