from enum import Enum

import openai

from discord_gpt.chat_completion import ChatCompletionResponse
from settings import settings

openai.api_key = settings.OPENAI_TOKEN


class GptModel(Enum):
    GPT_3_5_TURBO = 'gpt-3.5-turbo'
    GPT_3_5_TURBO_0301 = 'gpt-3.5-turbo-0301'


class OpenAIClient:
    @staticmethod
    def complete(
        prompt: str,
        model: GptModel,
        suffix: str | None = None,
        max_tokens: str | None = 1,
        temperature: str | None = 1,
        top_p: str | None = 1,
        n: int | None = 1,
        stream: bool = False,
        logprobs: int | None = None,
        echo: bool = False,
    ) -> str:
        chat_completion_response = ChatCompletionResponse.parse_raw(openai.ChatCompletion.create(
            prompt=prompt,
            model=model.value,
            suffix=suffix,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            n=n,
            stream=stream,
            logprobs=logprobs,
            echo=echo,
        ))

        generated_text = chat_completion_response.choices[0].text

        return generated_text


