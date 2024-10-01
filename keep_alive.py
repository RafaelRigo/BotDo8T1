from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Olá! este site por enquanto não faz nada, ele apenas faz com que o bot fique online para sempre :)\nPs: se ele vai ficar off é por problemas de conexão."

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()