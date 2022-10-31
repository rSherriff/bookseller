from enum import Enum
from mimetypes import init
from books import *
from utils.definitions import ClientIDs

class Client:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
        self.served_today = False
        self.available_requests = []

    def complete_request(self, request_id):
        self.available_requests.remove(request_id)
        self.served_today = True

client_a = Client(ClientIDs.CLIENT_A, "Client A")

client_manager = {
    client_a.id: client_a
}