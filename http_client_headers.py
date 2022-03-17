import http.client
def switch(tipo, content):
	if tipo == "audio/mpeg":
		print("Playing audio:", content)
	elif tipo == "text/html":
		print("Browsing:", content)
	elif tipo == "video/x-msvideo":	
		print("Playing media:", content)
	elif tipo == "application/json":	
		print("Processing JSON:", content)
	elif tipo == "text/html;charset=utf-8":	
		print("Content not found")
	else:
		print("Unknown file/media:", tipo+"-"+content)

def HTTPclient(host, port):

	L = int(input())

	for i in range(L):

		content = input() # página HTML que vai ser trabalhada
		conn = http.client.HTTPConnection(host, port) #conexão
		conn.request("GET", content) # estabelecendo parâmetros pra fazer o request
		r = conn.getresponse() # recebe o dado! :)
		headers = r.getheaders()
		print("Header =", headers, "\n")
		tipo = "0"
		for header in headers:
			if (header[0] == 'Content-Type') or (header[0] == 'Content-type'):
				tipo = header[1]
		print(tipo)
		switch(tipo, content)
		conn.close() 

HTTPclient("localhost", 8888)