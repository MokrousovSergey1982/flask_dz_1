from flask import Flask, render_template, request, make_response, flash, url_for, redirect


app = Flask(__name__)

app.secret_key = b'f57f3a0bd0192d415028b4394165b34dbc95a97f1447aae754d9939180fe3db5'

@app.route('/')
def base():
    return render_template('base.html')


@app.route('/cookie/', methods=['POST'])
def cookie():
    username = request.form['name']
    usermail = request.form['mail']

    response = make_response(redirect('/greeting/'))
    response.set_cookie('name', username)
    response.set_cookie('mail', usermail)
    return response


@app.route('/greeting/')
def greeting():
    username = request.cookies.get('name')
    usermail = request.cookies.get('mail')
    if not username or not usermail:
        flash('ВВЕДИТЕ ВАШЕ ИМЯ и ПОЧТУ', 'danger')
        return redirect(url_for('authorization'))
    flash('ФОРМА УСПЕШНО ДОБАВЛЕНА', 'success')
    return render_template('greeting.html', name=username)


@app.route('/authorization/', methods=['GET', 'POST'])
def authorization():
    context = {
        'task': 'ДОМАШНИЕ ЗАДАНИЕ'
    }
    if request.method == 'POST':
        username = request.form.get('name')
        usermail = request.form.get('mail')
        context = {'username': username,
                   'usermail': usermail}
    return render_template('authorization.html', **context)


@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    response = make_response(redirect('/'))
    response.delete_cookie('name')
    response.delete_cookie('mail')
    return response


if __name__ == '__main__':
    app.run(debug=True)