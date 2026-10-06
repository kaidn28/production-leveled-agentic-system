from langchain_anthropic import ChatAnthropic
from .chat_model import ChatModel

class ClaudeChat(ChatModel):
    def initialize(self):
        self.llm = ChatAnthropic(
            base_url=self.base_url,
            api_key=self.api_key,
            model=self.model,
            temperature=0
        )

    def chat(self, messages, args):
        response = self.llm.invoke(messages)
        return "\n".join([x['text'] for x in response.content if 'text' in x.keys()])

