from dagster import asset, asset_check, Output, MetadataValue
import subprocess

from pathlib import Path, PosixPath
from tempfile import mkdtemp


@asset
def scrape() -> Output[PosixPath]:
    directory = mkdtemp()
    process = subprocess.Popen(
        ["uv", "run", "--project=../scraper", "cvm", "2", directory, "metadata.json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    # communicate() sends data to stdin (if provided) and reads data from stdout and stderr until the process terminates
    stdout, stderr = process.communicate()

    metadata_path = Path(directory) / "metadata.json"

    return Output(value=metadata_path, metadata={"metadata_path": metadata_path})


@asset
def make_reports(scrape: PosixPath) -> Output[PosixPath]:
    output_file = scrape.parent / "output.json"
    process = subprocess.Popen(
        [
            "uv",
            "run",
            "--project=../ai-journal-api",
            "api",
            "01.md",
            scrape.as_posix(),
            output_file,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    # communicate() sends data to stdin (if provided) and reads data from stdout and stderr until the process terminates
    stdout, stderr = process.communicate()
    return Output(value=output_file, metadata={"output_file": output_file})
