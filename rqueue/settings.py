import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import AzureChatOpenAI


HOME_DIR = ""
BASE_LOG_DIR = os.path.join(HOME_DIR, "logs")
DEFAULT_LOG_DIR_OUT = f"{BASE_LOG_DIR}/stdout.txt"

#Execution frequencies
IMMEDIATE_FREQUENCY = "Once"
INTERVAL_FREQUENCY = "Interval"
DAILY_FREQUENCY = "Daily"

OPENAI_EMBEDDING_MODEL = "text-embedding-ada-002"
OPENAI_GPT_MODEL = "gpt-3.5-turbo"
ENGINE = ""
OPENAI_API_BASE = ""
OPENAI_API_TYPE = ""
OPENAI_API_KEY = ""
openai.api_version = "2023-03-15-preview"
openai.api_key = OPENAI_API_KEY

LLM = AzureChatOpenAI(deployment_name=ENGINE, 
					model_name=OPENAI_GPT_MODEL,
					openai_api_base=OPENAI_API_BASE,
					openai_api_version=openai.api_version,
					openai_api_key=OPENAI_API_KEY)
EMBEDDINGS = OpenAIEmbeddings(openai_api_key=openai.api_key, model=OPENAI_EMBEDDING_MODEL, chunk_size=1)