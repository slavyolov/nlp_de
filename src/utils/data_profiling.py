import pandas as pd
from ydata_profiling import ProfileReport
from pathlib import Path
import logging


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
    file_path = Path(Path(__file__).parents[2], input_path)

    # read file
    df = pd.read_csv(filepath_or_buffer=file_path, sep=file_separator, header=None, on_bad_lines='skip')

    # check data loss due to bad lines
    lines_at_start = count_lines_enumerate(file_path)
    lines_at_end = len(df)
    pct_missing = 1 - (lines_at_end/lines_at_start)
    logger.info(
        f"{pct_missing * 100:.2f}% of the input data is lost due to bad lines"
    )

    profile = ProfileReport(df=df, title=f"Profiling report of file {input_path}")
    output_file = Path(Path(__file__).parents[2],
                       output_path, f"profiling_of_{input_path.split(sep='/')[-1:][0].replace('.csv', '.html')}")
    return profile.to_file(output_file=output_file)


def count_lines_enumerate(file_name):
    """
    Count the number of lines in a file

    Args:
        file_name:

    Returns:

    """
    line_count = 0

    # Read the input file and return the line count
    fp = open(file_name, 'r')
    for line_count, line in enumerate(fp):
        pass
    return line_count
