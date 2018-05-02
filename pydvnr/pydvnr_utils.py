import logging
import os
import platform
import sys

import psutil

logger = logging.getLogger('pydvnr')


def show_banner():
    banner = """    
    ____            __                
   / __ \__  ______/ /   ______  _____
  / /_/ / / / / __  / | / / __ \/ ___/
 / ____/ /_/ / /_/ /| |/ / / / / /    
/_/    \__, /\__,_/ |___/_/ /_/_/     
      /____/                          

    """

    logger.info(banner)


def get_basic_information():
    logger.info('---------- Operating System ----------')

    os_version = platform.platform()
    release = platform.release()
    version = platform.version()

    logger.info('OS: %s', os_version)
    logger.info('Release: %s', release)
    logger.info('Version: %s', version)
    logger.info('CWD: %s', os.getcwd())

    logger.info('---------- Memory ----------')

    memory = psutil.virtual_memory()
    total_memory = memory.total >> 30
    available_memory = memory.available >> 30
    percent_memory = memory.percent

    logger.info('%s GB of %s GB available - %s', available_memory, total_memory, percent_memory)

    logger.info('---------- CPU ----------')
    processors = psutil.cpu_count()
    logger.info('%s processors', processors)


def get_python_version():
    logger.info('---------- Python Version ----------')
    full_python_version = sys.version.split('\n')[0]

    python_version = sys.version_info[:3]

    joined_version = '.'.join(map(str, python_version))

    logger.info(full_python_version)

    check_python_version(python_version, joined_version)

    logger.info('---------- Python Path ----------')

    logger.info(sys.executable)


def get_package_information(pip, pip_version):
    logger.info('---------- Packages ----------')

    packages = []

    if not pip_version.startswith('10'):
        packages = pip.get_installed_distributions()
    elif pip_version.startswith('10'):
        from pip._internal.utils.misc import get_installed_distributions

        packages = get_installed_distributions()

    packages.sort(key=lambda x: x.key)

    for package in packages:
        logger.info(repr(package))

        for dep, reqs in list(package._dep_map.items()):
            for req in reqs:
                logger.info('\t' + str(req))


def get_framework():
    # django, flask, pyramid, etc
    logger.info('---------- Framework ----------')

    try:
        import django

        logger.info('Django %s', django.get_version())
    except:
        pass

    try:
        import flask
        logger.info('Flask %s', flask.__version__)
    except:
        pass

    try:
        import pkg_resources

        logger.info('Pyramid %s', pkg_resources.get_distribution('pyramid').version)
    except:
        pass

    try:
        import bottle

        logger.info('Bottle %s; Currently Unsupported', bottle.__version__)
    except:
        pass

    try:
        import cherrypy

        logger.info('CherryPy %s; Currently Unsupported', cherrypy.__version__)
    except:
        pass

    try:
        import tornado

        logger.info('Tornado %s; Currently Unsupported', tornado.version)
    except:
        pass

    try:
        import aiohttp

        logger.info('Aiohttp %s; Currently Unsupported', aiohttp.__version__)
    except:
        pass


def check_python_version(python_version, joined_python_version):
    if python_version < (2, 7, 0):
        logger.error('The Python Agent only supports Python version 2.7 and above for Python 2')

    if python_version < (3, 4, 0):
        logger.error('The Python Agent only supports Python version 2.4 and above for Python 3')

    if joined_python_version in ['2.7.5', '2.7.6']:
        logger.warning('Your version of Python has a regular expression bug that prevents us from fully analyzing SSRF '
                       'and Command Injection attacks. It is recommended that you upgrade build versions.')


def check_pip_version():
    logger.info('---------- Pip ----------')

    try:
        import pip
    except:
        logger.warning('Pip is not installed!')
        return

    pip_version = pip.__version__

    logger.info('Pip version: %s', pip_version)

    if int(pip_version[0]) < 8:
        logger.warning(
            'An older version of pip is being used. It is recommended you upgrade to 9 or 10 for new features.')

    get_package_information(pip, pip_version)
