import os
import sys
import subprocess
import click
import pprint
import warnings
import dotenv
from dev import (
    get_performance_from_jsons,
    get_quality_from_jsons,
)

dotenv.load_dotenv(override=False)
warnings.filterwarnings("ignore")

@click.group()
def cli():
    """Watermark benchmarking tool."""
    pass


def run_command(script_name, path, orgpath, isorg, args):
    cmd = (
        [
            sys.executable,
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                f"{script_name}.py",
            ),
        ]
        + list(args)
        + ["--path", path]
        + ["--orgpath", orgpath] if script_name != "decode" else []
        + ["--isorg", True if path is None else False]
    )
    subprocess.run(cmd)


@click.option(
    "--path", "-p", default="./", help="Attacked image directory."
)
@click.option(
    "--orgpath", "-p", default="./", help="Original image directory."
)
@click.argument("args", nargs=-1)
def eval(path, orgpath, args):
    """Evaluate (stable signature watermark with all metrics)."""
    run_command("decode", path, None, True, args)
    run_command("metric", path, orgpath, True, args)
    run_command("decode", None, orgpath, False, args)
    run_command("metric", path, orgpath, False, args)
    
    performance_dict = get_performance_from_jsons(os.path.join(
        os.environ.get("RESULT_DIR"), "org-decode.json",
    ), os.path.join(
        os.environ.get("RESULT_DIR"), "decode.json",
    ), "removal")
    quality_dict = get_quality_from_jsons(os.path.join(
        os.environ.get("RESULT_DIR"), "org-metric.json",
    ), os.path.join(
        os.environ.get("RESULT_DIR"), "metric.json",
    ))
    print("#" * 20)
    print("# Evaluation results:")
    print("### Watermark Performance:")
    pprint.pprint(performance_dict)
    print("### Image Quality:")
    pprint.pprint(quality_dict)
    