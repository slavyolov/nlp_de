import pandas as pd
from ydata_profiling import ProfileReport
from pathlib import Path
import logging
from src.utils.reader import read_csv


logger = logging.getLogger(__name__)


def data_profiling(input_path: str, file_separator: str, output_path: str) -> ProfileReport.to_file:
    """
    Run data profiling on csv input files

    Args:
        input_path: input path for which the profile report is executed
        file_separator: file delimiter
        output_path: output path that stores the profile report

    Returns:

    """
    # read file
    df = read_csv(input_path=input_path, file_separator=file_separator)

    # generate profile report
    profile = ProfileReport(df=df, title=f"Profiling report of file {input_path}")
    output_file = Path(Path(__file__).parents[2],
                       output_path, f"profiling_of_{input_path.split(sep='/')[-1:][0].replace('.csv', '.html')}")
    return profile.to_file(output_file=output_file)
