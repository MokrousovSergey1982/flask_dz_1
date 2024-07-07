from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def sports_store():
    return render_template("base_dz_1.html")


@app.route('/single_sport/')
def single_sport():
    single_sport = {
        'season': 'Сезон',
        'type': 'Вид спорта',
        'name': 'Название'
    }

    single_sport_list = [
        {
            'season': 'Лето',
            'type': 'Бег',
            'name': 'Шиповки'
        },
        {
            'season': 'Зима',
            'type': 'Лыжные гонки',
            'name': 'Лыжи'
        },
    ]
    return render_template("single_sport_dz_1.html", **single_sport,
                           single_sport_list=single_sport_list)


@app.route('/team_sport/')
def team_sport():
    team_sport = {
        'season': 'Сезон',
        'type': 'Вид спорта',
        'name': 'Название'
    }

    team_sport_list = [
        {
            'season': 'Лето',
            'type': 'Футбол',
            'name': 'Бутсы'
        },
        {
            'season': 'Зима',
            'type': 'Хоккей',
            'name': 'Коньки'
        },
    ]
    return render_template("team_sport_dz_1.html", **team_sport, team_sport_list=team_sport_list)


if __name__ == '__main__':
    app.run(debug=True)
