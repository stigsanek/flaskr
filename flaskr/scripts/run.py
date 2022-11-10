#!/usr/bin/env python3
from flaskr import create_app
from flaskr.cli import get_args


def main():
    """
    Entry point

    :return:
    """
    args = get_args()

    app = create_app()
    app.run(host=args.host, port=args.port, debug=args.debug)


if __name__ == "__main__":
    main()
