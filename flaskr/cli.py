import argparse


def get_args() -> argparse.Namespace:
    """
    Return arguments

    :return: argparse.Namespace
    """
    parser = argparse.ArgumentParser(
        description="A basic blogging application."
    )
    parser.add_argument(
        "--host",
        help="the hostname to listen on",
        default="127.0.0.1",
        type=str
    )
    parser.add_argument(
        "--port",
        help="the port of the webserver",
        default=5000,
        type=int
    )
    parser.add_argument(
        "--debug",
        help="enable debug mode",
        dest="debug",
        action="store_true"
    )
    parser.add_argument(
        "--no-debug",
        help="disable debug mode",
        dest="debug",
        action="store_false"
    )
    parser.set_defaults(debug=False)

    return parser.parse_args()
