import os
import dotenv
from models import create_llm

dotenv.load_dotenv('.env')

def main():
    llm = create_llm(
        type='claude',
        base_url=os.environ.get("BASE_URL"),
        api_key=os.environ.get("API_KEY"),
        model=os.environ.get("MODEL")
    )

    print(llm.chat("Hi, how are you today", None))


if __name__ == "__main__":
    main()