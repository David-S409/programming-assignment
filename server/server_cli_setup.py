import argparse


def setup_cli():
    parser = argparse.ArgumentParser(description="This is the server portion of P1")
    parser.add_argument(
        "-p",
        "--port",
        dest="port",
        help="Port number to run the FTP Server",
        default=21,
    )

    args = parser.parse_args()

    return args
