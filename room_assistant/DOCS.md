# room-assistant

## Getting Started

This room-assistant add-on will store its configuration in a subfolder of the Home Assistant config, `/config/room_assistant`.
If this folder does not exist or contains no files it will be created with a sample configuration when you start the add-on.
You can drop your [YAML configuration](https://www.room-assistant.io/guide/configuration.html) in there like for any other room-assistant instance.

The connection to Home Assistant will be established automatically if you use one of the Home Assistant MQTT add-ons.

## Known Limitations

- On some Home Assistant installations the auto-discovery functionality of the cluster may not work. This is primarily the case for manual Home Assistant installations. You will see an error about this in the logs. In this case you need to [define the peers manually](https://www.room-assistant.io/guide/cluster#settings).