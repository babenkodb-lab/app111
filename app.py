# Импортируем Flask — библиотеку для создания веб-приложений на Python.
# render_template нужен, чтобы отдавать HTML-файл из папки templates.
from flask import Flask, render_template

# Создаём экземпляр приложения. __name__ — это имя текущего файла, Flask так ориентируется.
app = Flask(__name__)

# Декоратор @app.route('/') говорит: когда кто-то заходит на главную страницу "/",
# запусти функцию home().
@app.route('/')
def home():
    # Функция возвращает готовую HTML-страницу index.html из папки templates.
    return render_template('index.html')


# Этот блок выполнится только если мы запускаем файл напрямую (не импортируем).
if __name__ == '__main__':
    # Запускаем сервер на локальном компьютере. debug=True включает автоперезагрузку при изменениях.
    app.run(debug=True)