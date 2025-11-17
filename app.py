from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "key123"

@app.route('/', methods=["GET", "POST"])
def home():
    
    if request.method == "POST":
        name = request.form.get('nombre')
        lastname = request.form.get('apellido')
        email = request.form.get('email')
        cantidad = request.form.get('cantidad')
        session['nombre'] = name
        session['apellido'] = lastname
        session['email'] = email
        session['cantidad'] = cantidad
        return redirect(url_for('principal'))
    
    return render_template('index.html')

@app.route('/principal', methods=["POST","GET"])
def principal():
        name = session.get('nombre', '')
        lastname = session.get('apellido', '')
        email = session.get('email', '')
        cantidad = session.get('cantidad', 0)
        
        try:
            cantidad = int(cantidad)
        except:
            cantidad = 0
        
        palabras_español = []
        palabras_ingles = []
        

        
        if request.method == "POST":
            for i in range(int(cantidad)):
                palabra = request.form.get(f'spanish_{i}')
                palabras_español.append(palabra)
            
            for i in range(int(cantidad)):
                palabr = request.form.get(f'english_{i}')
                palabras_ingles.append(palabr)
        
        pares = list(zip(palabras_español, palabras_ingles))
                
        return render_template('principal.html', name=name, lastname=lastname, email=email, cantidad=cantidad, español=palabras_español, ingles=palabras_ingles, pares=pares)




if __name__ == '__main__':
    app.run(debug=True)