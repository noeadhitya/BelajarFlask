from flask import Flask #import library dari framework flask
app = Flask(__name__) #instansiasi dari main program flask

@app.route('/') #root dari flask - index file yang akan diakses pertama kali
#fungsi hello world yang dijalankan ketika index file diakses.
def hello_world():
    return 'Hello, World!'

@app.route('/nama/<nama>')
def namaku(nama):
    return 'Halo, namaku %s' %nama

@app.route('/nim/<int:nim>')
def nimku(nim):
    return 'Halo, nimku %d' %nim


@app.route('/bil/<int:bil1>/<int:bil2>')
def calc(bil1,bil2):
    hasil = bil1 - bil2
    return '%d' %hasil

#jika akan diakses menggunakan python app.py dan bukan dari flask run
if __name__ == '__main__':
    app.run()
