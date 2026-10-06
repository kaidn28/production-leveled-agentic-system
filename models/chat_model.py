from abc import ABC, abstractmethod

class ChatModel(ABC):
    def __init__(self, base_url=None, api_key=None, model=None):
        self.base_url = base_url
        self.api_key = api_key
        self.model = model

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def chat(self, messages, args):
        pass