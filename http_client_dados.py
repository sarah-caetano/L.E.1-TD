import http.client

def HTTPclient(host, port):

	L = int(input())

	for i in range(L):
		content = input() # página HTML que vai ser trabalhada
		conn = http.client.HTTPConnection(host, port) #conexão
		conn.request("GET", content) # estabelecendo parâmetros pra fazer o request
		r = conn.getresponse() # recebe o dado! :)
		data = r.read().decode() # recebe o conteúdo em texto, .decode() = transcreve pra string
		print(data)
		conn.close() # fechar a conexão atual pra próxima conexão ser feita

HTTPclient("localhost", "8888")