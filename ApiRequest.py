from flask import Flask, request
from json import dumps

app = Flask(__name__,static_folder='static')

#Fazer chamada, para obter o Token 
#@app.route(' ', methods=["POST"])
def posttoken():
    url = "/client_id = <your-client-id> & client_secret = <your-secret-here> & grant_type = client_credentials & resource = <resource-url>"
    data = {'agente_usuario':'agente_usuario', 'Host':'login.microsoftonline.com', 'Content-Type': 'application / x-www-form-urlencoded'    }
    
    response = request.post(url, data= data)
    print response.Content
#@app.route('/post', methods=[])
#def post():
    
#Realizando Requisição de Teste: 
#@app.route('/head', methods=['HEAD'])
def head():
    url = "https://digitallatam-apis-uat.chubb.com/policies HTTP / 1.1 "
    data = { 'Host':'login.microsoftonline.com', 'Ocp-Apim-Subscription-Key': key, 'Autorização': 'Portador <aad-token-here>'    }
    response = request.post(url, data= data)
    return response.Content


# Ids de Solicitação
#@app.route('/postid', methods=['post'])
def postid():
    url = "POST / política HTTP /1.1  "
    data = { 'Ocp-Apim-Subscription-Key': key, 'Autorização': 'Portador <aad-token-here>', 'Tipo de conteúdo': 'application / json',  "id": "", "dateUtc": "2019-01-29T16: 04: 38.859Z", "dados":' '    }
    response = request.post(url, data= data)
    return response.Content

# Método GET: 
#@app.route('/postid', methods=['post'])
def get():
    url = "policy / {12345} / status HTTP / 1.1 "
    data = { 'Ocp-Apim-Subscription-Key': key, 'Autorização': 'Portador <aad-token-here>', 'Tipo de conteúdo': 'application / json',  "id": "", "dateUtc": "2019-01-29T16: 04: 38.859Z", "dados":' '    }
    response = request.post(url, data= data)
    return response.Content




if __name__ == '__main__':
    app.run(debug=True)
