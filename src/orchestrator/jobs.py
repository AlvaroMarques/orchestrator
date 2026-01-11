from dagster import Definitions
from orchestrator.assets import scrape, make_reports

defs = Definitions(assets=[scrape, make_reports])
