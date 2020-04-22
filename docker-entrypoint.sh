#!/bin/sh

export CONFIG_FILE=/nevermind_gateway_events/config.ini
envsubst < /nevermind_gateway_events/config.ini.template > /nevermind_gateway_events/config.ini
if [ "${LOCAL_CONTRACTS}" = "true" ]; then
  echo "Waiting for contracts to be generated..."
  while [ ! -f "/usr/local/nevermind-contracts/ready" ]; do
    sleep 2
  done
fi

/bin/cp -up /usr/local/nevermind-contracts/* /usr/local/artifacts/ 2>/dev/null || true

/nevermind_gateway_events/start_events_monitor.sh

tail -f /dev/null
