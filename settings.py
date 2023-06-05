from pydantic import BaseSettings


class Settings(BaseSettings):
    TOKEN: str = ''

    class Config:
        env_file = '.env'
        env_prefix = 'DISCORD_GPT_'


settings = Settings()
