from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    page_title = 'Beaver_knithen: главная страница'
    beaver_knithen_main_1 = "Beaver_knithen"
    beaver_knithen_main_2 = "Вязанные изделия любой сложности из наличия и на заказ"
    context = {
        'title': page_title,
        'beaver_main_1': beaver_knithen_main_1,
        'beaver_main_2': beaver_knithen_main_2,
    }
    return render_template('main_page.html', **context)


if __name__ == "__main__":
    app.run(debug=True)
