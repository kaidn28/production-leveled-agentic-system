from .claude import ClaudeChat

def create_llm(type, base_url, api_key, model):
    if type == "claude":
        llm = ClaudeChat(base_url, api_key, model)
        llm.initialize()
        return llm

    raise ValueError(f"Model type {type} not available")