from websocket_server import WebsocketServer

def new_client(client, server):
	server.send_message_to_all("Hey all, a new client has joined us")

server = WebsocketServer(host='0.0.0.0', port=int(os.environ["PORT"]))
server.set_fn_new_client(new_client)
server.run_forever()