import dotenv
from openai import OpenAI

dotenv.load_dotenv()

translator = OpenAI()
transcriber = OpenAI()
