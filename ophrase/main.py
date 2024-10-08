import json
from tenacity import retry, stop_after_attempt, wait_fixed
from rich.console import Console
from rich.json import JSON
from typing import List, Dict, Any, Tuple
from .log import Log
from .serializer import Serializer
from .constants import Const
from .config import Config
from .manager import Manager
from .args import Args
from .error import handle_error, ValidationError
from .decorators import args

console = Console()

class Main:
    def __init__(self, cfg: Config):
        self.cfg = cfg
        self.manager = Manager(cfg)

    @staticmethod
    @retry(stop=stop_after_attempt(5), wait=wait_fixed(1))
    @args
    def run(parsed_args):
        try:
            main = Main(Config(debug=parsed_args.debug))
            Log.setup(parsed_args.debug)
            if parsed_args.debug:
                Log.start_main_function()
            main._execute(parsed_args.text, parsed_args.debug, parsed_args.prompt)
        except Exception as e:
            handle_error(e, parsed_args.debug)

    def _execute(self, text: str, debug: bool, include_prompts: bool) -> None:
        try:
            self.manager.check_version()
            responses, response_prompts = self.manager.generate_responses_and_prompts(text)
            final_result = Serializer.serialize_output(text, responses, response_prompts, include_prompts)
            json_output = json.dumps(final_result, indent=2, separators=(',', ': '))
            console.print(JSON(json_output))
        except ValidationError as e:
            handle_error(e, debug)
        except Exception as e:
            handle_error(e, debug)


