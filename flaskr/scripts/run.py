#!/usr/bin/env python3
from flaskr import create_app


def main():
    """
    Entry point

    :return:
    """
    app = create_app()
    app.run()


if __name__ == "__main__":
    main()
