[![banner](https://raw.githubusercontent.com/nevermined-io/assets/main/images/logo/banner_logo.png)](https://nevermined.io)

# Nevermined Gateway Events
Provider's events handler agent dealing with Keeper Contract events


[![Docker Build Status](https://img.shields.io/docker/cloud/build/keykoio/nevermined-gateway-events.svg)](https://hub.docker.com/r/keykoio/nevermined-gateway-events/)
[![Python package](https://github.com/nevermined-io/gateway-events/workflows/Python%20package/badge.svg)](https://github.com/nevermined-io/gateway-events/actions)


## Features
Monitors ServiceExecutionAgreement events and act as a provider agent to 
grant access and release reward for the publisher/provider. This is a critical 
part in the process of consuming data sets in the Nevermined Protocol network. 
Every provider in the network must run some sort of an events-handler to 
be able to fulfill the access condition of an `Access` service in an `SEA` .

This release only supports the `Access` service type that is defined in an 
Ocean `DDO`. More service types will be supported in the events-handler when 
they're added to the Ocean services.

## Prerequisites

Python 3.6

## Running Locally

First, clone this repository:

```bash
git clone git@github.com:nevermined-io/gateway-events.git
cd gateway-events/
```

Start a keeper node and other services of the ocean network:

```bash
git clone git@github.com:nevermined-io/tools.git
cd tools
bash start_nevermined.sh --no-commons --local-spree-node
```


Export environment variables `PROVIDER_ADDRESS`, `PROVIDER_PASSWORD`
and `PROVIDER_KEYFILE` (or `PROVIDER_ENCRYPTED_KEY`). Use the values from the `tox.ini` file, or use 
your own.
Instead of using keyfile and password, you can use the private key directly 
by setting the env var `PROVIDER_KEY`.

The most simple way to start is:

```bash
pip install -r requirements_dev.txt
export CONFIG_FILE=config.ini
./scripts/wait_for_migration_and_extract_keeper_artifacts.sh
./start_events_monitor.sh
```


## Attribution

This project is based in the [Ocean Protocol Events Handler](https://github.com/oceanprotocol/events-handler). 
It keeps the same Apache v2 License and adds some improvements. See [NOTICE file](NOTICE).

## License

```
Copyright 2020 Keyko GmbH
This product includes software developed at
BigchainDB GmbH and Ocean Protocol (https://www.oceanprotocol.com/)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

