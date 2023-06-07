from enum import Enum

import openai

from settings import settings

openai.api_key = settings.OPENAI_TOKEN


class Model(Enum):
    GPT_3_5_TURBO = 'gpt-3.5-turbo'
    GPT_3_5_TURBO_0301 = 'gpt-3.5-turbo-0301'


class OpenAIClient:
    def __init__(
        self,
    ) -> None:
        self.model = Model.GPT_3_5_TURBO


