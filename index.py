from flask import Flask,render_template, json,request,url_for,redirect


app = Flask(__name__)

def arquivoNaoExiste(nomeArquivoTxt): 
        try:
            arquivoTxt = open(nomeArquivoTxt)
            arquivoTxt.close()
            print('arquivo existe')
            return False
        except:
            print('Arquivo nao existe')
            return True

def criaArquivo(nomeArquivoTxt):
    arquivoTxt = open(nomeArquivoTxt,"w")
    arquivoTxt.write('[]')
    arquivoTxt.close()



   

@app.route("/" ,methods=["POST","GET"])
def index():
    if(arquivoNaoExiste("arquivoListaArray.txt")):
        criaArquivo("arquivoListaArray.txt")
    else:
        try:

            arquivoTxt = open("arquivoListaArray.txt",'r')
            
        except:
            criaArquivo()
            arquivoTxt = open("arquivoListaArray.txt",'r')
            listaTxt = json.loads(arquivoTxt.read())
            arquivoTxt.close()

        listaTxt = json.loads(arquivoTxt.read())
        lista_array = listaTxt
        lista_array = json.dumps(lista_array)  
        return render_template("tabelaMain.html", lista_array = lista_array)

    arquivoTxt = open("arquivoListaArray.txt",'r')
    listaTxt = json.loads(arquivoTxt.read())
    return render_template("tabelaMain.html", lista_array = listaTxt)
    


@app.route("/tabela", methods= ["POST","GET"])
def tabelaLibelula():
    print(request.form.get('lista_array'))
    if(request.method == "POST"):
        
        arquivoTxt = open("arquivoListaArray.txt","w")
        listaInput = request.form.get('lista_array')
        arquivoTxt.write(f"{listaInput}")
    return redirect(url_for('index'))

@app.route("/tabela2")
def tabela2():
    if(arquivoNaoExiste("arquivotabela2.txt")):
        criaArquivo("arquivotabela2.txt")
    else:
        try:

            arquivoTxt = open("arquivotabela2.txt",'r')
            
        except:
            criaArquivo()
            arquivoTxt = open("arquivotabela2.txt",'r')
            listaTxt = json.loads(arquivoTxt.read())
            arquivoTxt.close()

        listaTxt = json.loads(arquivoTxt.read())
        lista_array = listaTxt
        lista_array = json.dumps(lista_array)  
        return render_template("tabela_22.0.html", lista_array = lista_array)

    arquivoTxt = open("arquivotabela2.txt",'r')
    listaTxt = json.loads(arquivoTxt.read())
    return render_template("tabela_22.0.html", lista_array = listaTxt)
    

@app.route("/tabela2Rt" , methods=["GET","POST"])
def tabelaRetorno():
    print(request.form.get('lista_array'))
    if(request.method == "POST"):
        
        arquivoTxt = open("arquivotabela2.txt","w")
        listaInput = request.form.get('lista_array')
        arquivoTxt.write(f"{listaInput}")
    return redirect(url_for('tabela2'))


@app.route("/img")
def imgGrafic():
    return render_template("siteImg.html")

app.run(debug=True)