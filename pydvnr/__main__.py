import logging
import sys

logger = logging.getLogger('pydvnr')
logger.addHandler(logging.FileHandler('contrast-pydvr.txt'))
logger.setLevel(logging.INFO)

from . import pydvnr_utils


def main():
    if '-s' in sys.argv:
        logger.handlers = []

        logger.addHandler(logging.StreamHandler(sys.stdout))
    else:
        print('Output is shown in contrast-pydvr.txt')

    pydvnr_utils.show_banner()

    pydvnr_utils.get_basic_information()

    pydvnr_utils.get_python_version()

    pydvnr_utils.check_pip_version()

    pydvnr_utils.get_framework()


if __name__ == '__main__':
    main()
