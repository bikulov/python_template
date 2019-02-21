#!/usr/bin/env python


import argparse
import logging
import datetime


def parse_arguments():
    parser = argparse.ArgumentParser(
        "Application title",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.set_defaults(func=None)
    parser.add_argument(
        "--verbose",
        help="Verbose logging",
        action="store_true"
    )
    subparsers = parser.add_subparsers()

    first_module_parser = subparsers.add_parser(
        "first_module",
        help="First module",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    first_module_parser.set_defaults(func=first_module)
    first_module_parser.add_argument(
        "--name",
        default="ksar",
        help="Username",
    )

    second_module_parser = subparsers.add_parser(
        "second_module",
        help="Second module",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    second_module_parser.set_defaults(func=second_module)
    second_module_parser.add_argument(
        "--dry-run",
        help="Do not do anything",
        action="store_true"
    )
    second_module_parser.add_argument(
        "--number",
        help="Int number",
        type=int,
        default=618,
    )

    return parser.parse_args()


def first_module(args):
    logging.info(args.name)


def calculate_square(number):
    return number * number


def second_module(args):
    logging.info(args.dry_run)
    logging.info(args.number)

    if not args.dry_run:
        logging.info("Square of %s: %s" % (args.number, calculate_square(args.number)))


def main():
    args = parse_arguments()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="[%(filename)s:%(lineno)d] %(levelname)-8s [%(asctime)s]  %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    if args.func:
        args.func(args)


if __name__ == "__main__":
    main()
