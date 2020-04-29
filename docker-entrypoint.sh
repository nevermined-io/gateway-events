#!/bin/sh

export CONFIG_FILE=/nevermined_gateway_events/config.ini
envsubst < /nevermined_gateway_events/config.ini.template > /nevermined_gateway_events/config.ini
if [ "${LOCAL_CONTRACTS}" = "true" ]; then
  echo "Waiting for contracts to be generated..."
  while [ ! -f "/usr/local/nevermined-contracts/ready" ]; do
    sleep 2
  done
fi

/bin/cp -up /usr/local/nevermined-contracts/* /usr/local/artifacts/ 2>/dev/null || true

/nevermined_gateway_events/start_events_monitor.sh

tail -f /dev/null
