import os
import time

from contracts_lib_py.contract_handler import ContractHandler
from contracts_lib_py.utils import get_account
from contracts_lib_py.web3_provider import Web3Provider
from contracts_lib_py.keeper import Keeper

from nevermind_gateway_events.log import setup_logging
from nevermind_gateway_events.provider_events_monitor import ProviderEventsMonitor
from nevermind_gateway_events.util import get_config, get_keeper_path, init_account_envvars


def run_events_monitor():
    setup_logging()
    config = get_config()
    keeper_url = config.keeper_url
    storage_path = config.get('resources', 'storage.path', fallback='./provider-events-monitor.db')

    web3 = Web3Provider.get_web3(keeper_url)
    ContractHandler.artifacts_path = get_keeper_path(config)
    keeper = Keeper.get_instance()
    init_account_envvars()

    account = get_account(0)
    if account is None:
        raise AssertionError(f'Provider events monitor cannot run without a valid '
                             f'ethereum account. Account address was not found in the environment'
                             f'variable `PROVIDER_ADDRESS`. Please set the following environment '
                             f'variables and try again: `PROVIDER_ADDRESS`, [`PROVIDER_PASSWORD`, '
                             f'and `PROVIDER_KEYFILE` or `PROVIDER_ENCRYPTED_KEY`] or `PROVIDER_KEY`.')

    if not account.key_file and not (account.password and account.key_file):
        raise AssertionError(f'Provider events monitor cannot run without a valid '
                             f'ethereum account with either a `PROVIDER_PASSWORD` '
                             f'and `PROVIDER_KEYFILE`/`PROVIDER_ENCRYPTED_KEY` '
                             f'or private key `PROVIDER_KEY`. Current account has password {account.password}, '
                             f'keyfile {account.key_file}, encrypted-key {account._encrypted_key} '
                             f'and private-key {account._private_key}.')

    monitor = ProviderEventsMonitor(keeper, web3, storage_path, account)
    monitor.start_agreement_events_monitor()
    while True:
        time.sleep(5)


if __name__ == '__main__':
    run_events_monitor()
