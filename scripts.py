from flask import Flask, render_template

app=Flask(__name__)
#ruta donde se va a visulizar el sitio web
@app.route('/')

def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.run(debug=True)  #debug=True para que se actualice automaticamente el sitio web