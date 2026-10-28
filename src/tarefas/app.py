from flask import Flask, render_template

app = Flask (__name__)

@app.route('/test')
def test():
    return 'servidor online!'

@app.route('/')
def home():
    return render_template('base.html', titulo='Lista de tarefas do Elder')

if __name__ == '__main__':
    app.run()