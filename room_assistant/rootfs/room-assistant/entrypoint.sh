#!/usr/bin/env bashio
MQTT_CONFIG=$(bashio::services 'mqtt')
if bashio::var.has_value "${MQTT_CONFIG}"; then
    bashio::log.info "Setting up Home Assistant configuration"
    echo "${MQTT_CONFIG}" | jq '{homeAssistant: {mqttUrl: "mqtt://\(.host):\(.port)", mqttOptions: {username: .username, password: .password}}}' > /room-assistant/config/default.json
fi

if [ -z "$(ls -A /config/room_assistant 2>/dev/null)" ]; then
    bashio::log.info "Creating default room-assistant configuration under /config/room_assistant"
    mkdir -p /config/room_assistant
    tee /config/room_assistant/local.yml <<EOF > /dev/null
# You don't need to add the MQTT details for Home Assistant with the add-on installation, it will be auto-discovered!
global:
  instanceName: changeme
  integrations:
    - homeAssistant
EOF
fi

bashio::log.info "Copying room-assistant configuration from /config/room_assistant"
cp /config/room_assistant/* /room-assistant/config/

bashio::log.info "Starting room-assistant"
exec room-assistant --digResolver