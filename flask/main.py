from flask import Flask, render_template

app = Flask(__name__)

#Criar a primeira página do site
#route (caminho após o domínio) ->
#função -> o que quer exibir naquela página

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contact():
    return render_template("contatos.html")

@app.route("/cliente/<client_name>")
def client(client_name):
    return render_template("cliente.html", client_name=client_name)

#Colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
