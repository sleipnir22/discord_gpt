from enum import Enum

from pydantic.main import BaseModel


class GptModel(Enum):
    GPT_3_5_TURBO = 'gpt-3.5-turbo'
    GPT_3_5_TURBO_0301 = 'gpt-3.5-turbo-0301'


class Choice(BaseModel):
    text: str
    index: int
    logprobs: str | None
    finish_reason: str


class Usage(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class ChatCompletionResponse(BaseModel):
    id: str
    object: str
    created: int
    model: str
    choices: list[Choice]
    usage: Usage


class Message(BaseModel):
    role: str
    content: str
    name: str | None


class ChatCompletionRequest(BaseModel):
    messages: list[Message]
    model: GptModel
    suffix: str | None = None
    max_tokens: str | None = 1
    temperature: str | None = 1
    top_p: str | None = 1
    n: int | None = 1
    stream: bool = False
    logprobs: int | None = None
    echo: bool = False