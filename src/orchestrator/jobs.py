from dagster import Definitions
from orchestrator.assets import hello, world

defs = Definitions(assets=[hello, world])
