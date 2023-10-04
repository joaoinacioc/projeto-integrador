from flask import Flask, render_template

app = Flask(__name__)

#Criar a primeira página do site
#route (caminho após o domínio) ->
#função -> o que quer exibir naquela página

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/clientes/<nome_cliente>")
def clientes(nome_cliente):
    return render_template("clientes.html", nome_cliente=nome_cliente)

#Colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

# servidor do heroku