import json
from typing import List, Dict, Any, Tuple
from .constants import Const
from .config import Config
from .manager import Manager

class Ophrase:
    def __init__(self, cfg: Config):
        self.manager = Manager(cfg)

    def check(self) -> None:
        self.manager.check()

    def pull(self) -> None:
        self.manager.pull()

    def generate(self, text: str) -> Tuple[List[Dict[str, Any]], List[str]]:
        return self.manager.generate(text)
