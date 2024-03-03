from langchain_community.llms.openai import AzureOpenAI

from src.settings import OpenAISettings


class AzureOpenAIBuilder:
    def __init__(self):
        self._deployment_name = None
        self._openai_api_version = None
        self._temperature = 0.1
        self._top_p = 0
        self._presence_penalty = 0
        self._frequency_penalty = 0
        self._max_tokens = -1

    def deployment_name(self, deployment_name):
        self._deployment_name = deployment_name
        return self

    def openai_api_version(self, openai_api_version):
        self._openai_api_version = openai_api_version
        return self

    def temperature(self, temperature):
        self._temperature = temperature
        return self

    def build(self):
        if not self._deployment_name:
            raise ValueError("Deployment name must be set.")
        return AzureOpenAI(
            deployment_name=self._deployment_name,
            openai_api_version=self._openai_api_version,
            temperature=self._temperature,
            top_p=self._top_p,
            presence_penalty=self._presence_penalty,
            frequency_penalty=self._frequency_penalty,
            max_tokens=self._max_tokens,
        )


class AzureOpenAIFactory:
    @staticmethod
    def create_model() -> AzureOpenAI:
        settings = OpenAISettings()
        return (
            AzureOpenAIBuilder()
            .deployment_name(settings.deployment)
            .openai_api_version(settings.version)
            .build()
        )


MODEL = AzureOpenAIFactory.create_model()
