import json
import os
import pathlib
from urllib.request import urlopen

import pytest
from contracts_lib_py import Keeper
from contracts_lib_py.contract_handler import ContractHandler
from contracts_lib_py.utils import get_account
from contracts_lib_py.web3_provider import Web3Provider

from nevermind_gateway_events.util import (get_config, get_storage_path,
                                           init_account_envvars)


def get_resource_path(dir_name, file_name):
    base = os.path.realpath(__file__).split(os.path.sep)[1:-1]
    if dir_name:
        return pathlib.Path(os.path.join(os.path.sep, *base, dir_name, file_name))
    else:
        return pathlib.Path(os.path.join(os.path.sep, *base, file_name))


@pytest.fixture(autouse=True)
def setup_all():
    config = get_config()
    keeper_url = config.keeper_url
    Web3Provider.get_web3(keeper_url)
    ContractHandler.artifacts_path = os.path.expanduser(
        '~/.nevermind/nevermind-contracts/artifacts')
    init_account_envvars()


@pytest.fixture
def provider_account():
    return get_publisher_account()


@pytest.fixture
def web3():
    return Web3Provider.get_web3(get_config().keeper_url)


@pytest.fixture
def keeper():
    return Keeper.get_instance()


@pytest.fixture
def storage_path():
    return get_storage_path(get_config())


def get_publisher_account():
    return get_account(0)


def get_consumer_account():
    return get_account(0)


def get_sample_ddo():
    return json.loads(urlopen(
        "https://raw.githubusercontent.com/keyko-io/nevermind-docs/master/architecture/specs"
        "/examples/access/v0.1/ddo1.json").read().decode(
        'utf-8'))
