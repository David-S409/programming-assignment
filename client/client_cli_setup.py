import argparse


def setup_cli():
    parser = argparse.ArgumentParser(description="This is the client portion of P1")
    parser.add_argument(
        "-d",
        "--domain",
        dest="domain",
        help="Domain of the FTP server",
        default="0.0.0.0",
    )
    parser.add_argument(
        "-p",
        "--port",
        dest="port",
        help="Port of the FTP server",
        default=21,
    )

    args = parser.parse_args()

    return args
