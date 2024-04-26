from __future__ import annotations
from typing import Protocol
from pathlib import Path
import yaml
import logging


class CommandLineArgs(Protocol):
    config: str


class AppSettings:
    config_file = Path("config.yml")
    log_file: Path
    log_level: int

    def command_line_args(self) -> AppSettings:
        from argparse import ArgumentParser

        parser = ArgumentParser(description="A simple calculator.")

        parser.add_argument(
            "--config", "-c", help="Configuration file.", default="config.yml"
        )

        args = parser.parse_args()
        self.config_file = Path(args.config)
        return self

    def load_app_configuration(self) -> AppSettings:
        with self.config_file.open("r", encoding="UTF-8") as config_file:
            config = yaml.load(config_file, Loader=yaml.SafeLoader)
            self.log_file = Path(config["log_file"])
            self.log_level = getattr(
                logging, config["log_level"], logging.WARNING
            )

        return self

    def configure_logging(self) -> AppSettings:
        logging.basicConfig(
            filename=self.log_file,
            level=self.log_level,
            format="%(levelname)s: %(message)s",
        )

        return self


# chain pattern
AppSettings().command_line_args().configure_app()
