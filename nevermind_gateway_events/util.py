import os
import site

from contracts_lib_py import Keeper
from contracts_lib_py.web3_provider import Web3Provider

from nevermind_gateway_events.config import Config


def get_config():
    return Config(filename=os.getenv('CONFIG_FILE', 'config.ini'))


def get_storage_path(config):
    return config.get('resources', 'storage.path', fallback='./provider-events-monitor.db')


def get_keeper_path(config):
    path = config.keeper_path
    if not os.path.exists(path):
        if os.getenv('VIRTUAL_ENV'):
            path = os.path.join(os.getenv('VIRTUAL_ENV'), 'artifacts')
        else:
            path = os.path.join(site.PREFIXES[0], 'artifacts')

    return path


def init_account_envvars():
    os.environ['PARITY_ADDRESS'] = os.getenv('PROVIDER_ADDRESS', '')
    os.environ['PARITY_PASSWORD'] = os.getenv('PROVIDER_PASSWORD', '')
    os.environ['PARITY_KEYFILE'] = os.getenv('PROVIDER_KEYFILE', '')


def keeper_instance():
    return Keeper.get_instance()


def web3():
    return Web3Provider.get_web3(get_config().keeper_url)
