import socketserver
import http.server

HOST = "localhost"
PORT = 8888
httpd = None

try:
	Handler = http.server.SimpleHTTPRequestHandler #apontar pra classe do handler
	httpd = socketserver.TCPServer((HOST, PORT), Handler) 
	httpd.serve_forever() #ativando o handler - receiveing requests
	
except Exception as e:
#para encerrar:
	if httpd is not None:
		httpd.shutdown() #encerra todos os pedidos
		httpd.server_close() #fecha o socket q está escutando a porta
	raise