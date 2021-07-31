print('Load hubOptions')

deliverReceipts = False

localNodes = [
    {'name': 'zoneNode', 'subscribe': 'keyCaptured', 'filter': {'zone':'livingRoom'}}
]

wsServer = {
    "address"     : "192.168.0.219",
    "port"        : "8080",
    "onReceived"  : "receivedPayload",
}