import argparse
from datetime import datetime
import pandas as pd
from autotrader.binance.api import candles


def valid_date(s):
    if isinstance(s, datetime):
        return s
    try:
        return datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)


def load_data_from_api(start_time, end_time, batch_size, process_records):
    current_time = start_time
    while current_time < end_time:
        # TODO: send this to stderr or something, so we can pipe the output somewhere
        print(f'fetching {batch_size} rows starting at {current_time}')
        df = candles('BTCUSDT', interval='5m', start_time=current_time, limit=batch_size)
        process_records(df, is_first_row=(current_time == start_time))
        current_time = df.iat[-1, 0] + pd.Timedelta(minutes=5)


# TODO: possibly make this a proper lifecycle using a class
def process_stdout(df, is_first_row):
    print(df.to_csv(header=is_first_row, index=False))


def process_file(file_handle):
    return lambda df, is_first_row: df.to_csv(file_handle, header=is_first_row, index=False)


def load_data(filename, start_time, end_time, batch_size):
    is_file = filename != '-'

    if is_file:
        try:
            start_time = pd.to_datetime(pd.read_csv(filename).iat[-1, 0])
        except FileNotFoundError:
            pass

        file_handle = open(filename, 'a')
        try:
            load_data_from_api(start_time, end_time, batch_size, process_file(file_handle))
        finally:
            file_handle.close()
    else:
        load_data_from_api(start_time, end_time, batch_size, process_stdout)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--out', required=True, type=str, dest='filename',
                        help="The filename to store the data in. If the file already exists, --start is ignored "\
                        "and data loading will continue from the most recent record. Use '-' for stdout.")
    parser.add_argument('-b', '--batch-size', default=1000, type=int,
                        help="How many records to pull at once. (default: 1000)")
    parser.add_argument('--start', default=datetime(2000, 1, 1), type=valid_date,
                        help="The date to start pulling data from. Format is YYYY-MM-DD. (default: 2000-01-01)")
    parser.add_argument('--end', default=datetime.utcnow(), type=valid_date,
                        help="The date at which to stop pulling data. Format is the same as --start. "\
                        "Otherwise, leave blank to pull data up to right now.")
    args = parser.parse_args()

    load_data(args.filename, args.start, args.end, args.batch_size)
