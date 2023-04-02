#!/usr/bin/env python


from websocket import create_connection

ws = create_connection("ws://192.168.0.1/websocket")
ws.send("init "+'1'*10)
print("Sent 1")
result =  ws.recv()
print("Received '%s'" % result)
ws.send('sysutils: ' + 'a'*50000)
print ws.recv()
ws.close()
