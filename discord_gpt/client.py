from enum import Enum

import openai

from discord_gpt.chat_completion import ChatCompletionResponse, ChatCompletionRequest
from settings import settings

openai.api_key = settings.OPENAI_TOKEN


class OpenAIClient:
    @staticmethod
    def complete(
        request: ChatCompletionRequest
    ) -> str:
        chat_completion_response = ChatCompletionResponse.parse_obj(openai.ChatCompletion.create(
            **request.dict()
        ))

        generated_text = chat_completion_response.choices[0].text

        return generated_text
