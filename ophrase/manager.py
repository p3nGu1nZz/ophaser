from typing import List, Dict, Any, Tuple
from .task import Task
from .generator import Generator
from .log import Log
from .ophrase_const import Const
from .ophrase_config import Config

class Manager:
    def __init__(self, config: Config):
        self.config = config
        self.task = Task(config)
        self.generator = Generator(config, self.task)
        self.log = Log

    def check_version(self) -> None:
        self.task.run(['ollama', '--version'], Const.RUN_COMMAND_ERROR)

    def pull_model(self) -> None:
        self.task.run(['ollama', 'pull', self.config.model], f"{Const.PULL_COMMAND_ERROR} {self.config.model}.")

    def generate_responses_and_prompts(self, text: str) -> Tuple[List[Dict[str, Any]], List[str]]:
        responses = self.generator.generate_responses(text)
        prompts = [response['prompt'] for response in responses]
        return responses, prompts

    def generate_proofs(self, text: str, responses: List[str]) -> List[str]:
        return self.generator.generate_proofs(text, responses)

    def generate_proof_prompt(self, response: str) -> str:
        return self.task.create_prompt(response, task="proof")
