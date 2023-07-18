""" Импортирование библиотеки для работы с Flask и запусков субпроцессов. """

import subprocess
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """ Эта функция запускает Home Page """

    return render_template('index.html')

@app.route('/AutomationTest')
def autotest():
    """ Эта функция запускает Automation Test Page  """

    return render_template('AutomationTest.html')

@app.route('/BotPage')
def bot():
    """ Эта функция запускает Bot Page  """

    return render_template('BotPage.html')


@app.route("/runallure")
def run_allure():
    """ Эта функция запуская и отвечает за генерацию отчета allure. """

    cmd = ["./scriptsh/runallure.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('AutomationTest.html', text=out, json=out)


@app.route("/run")
def run():
    """ Эта функция запуская и отвечает за тесты страницы /example. """

    cmd = ["./scriptsh/run_aut_lk.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('AutomationTest.html', text=out, json=out)


if __name__ == "__main__":
    app.run(debug=True)