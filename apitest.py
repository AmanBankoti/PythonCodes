import os
import openai
openai.api_key = os.getenv("")
openai.Model.list()
