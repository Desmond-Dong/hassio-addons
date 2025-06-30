from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import logging
import base64
import requests
import paho.mqtt.client as mqtt

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
try:
    with open('/data/options.json', 'r', encoding='utf-8') as options_file:
        options = json.load(options_file)
except FileNotFoundError:
    log.error("Configuration file '/data/options.json' not found.")
    options = {}
except json.JSONDecodeError:
    log.error("Configuration file '/data/options.json' contains invalid JSON.")
    options = {}
# Read MQTT configuration from environment variables
mqtt_broker = options.get("mqtt_broker", "127.0.0.1")
mqtt_port = options.get("mqtt_port", 1883)
mqtt_topic = options.get("mqtt_topic", "EZVIZ")
mqtt_username = options.get("mqtt_username", "user")
mqtt_password = options.get("mqtt_password", "passwd")

# Home Assistant Discovery configuration
def publish_ha_discovery(device_id):
    # Battery Sensor Discovery
    discovery_topic = f"homeassistant/sensor/{device_id}_battery/config"
    payload = {
        "name": "Doorbell Battery Level",
        "state_topic": f"{mqtt_topic}/{device_id}/ys.devicestatus/reported/powerRemaining",
        "unit_of_measurement": "%",
        "value_template": "{{ value | int }}",
        "device_class": "battery",
        "unique_id": f"ezviz_battery_sensor_{device_id}",
        "device": {
            "identifiers": [device_id],
            "name": f"EZVIZ {device_id}",
            "manufacturer": "EZVIZ"
        }
    }
    mqtt_client.publish(discovery_topic, json.dumps(payload), retain=True)
    log.info("Published Home Assistant discovery config to topic: %s", discovery_topic)

    # Doorbell Charging Status Discovery (for any device_id)
    charging_discovery_topic = f"homeassistant/sensor/{device_id}_charging_status/config"
    charging_payload = {
        "name": "Doorbell Charging Status",
        "state_topic": f"{mqtt_topic}/{device_id}/ys.devicestatus/reported/powerType",
        "unique_id": f"doorbell_charging_status_{device_id}",
        "value_template": "{% if value == '0' %}Charging{% elif value == '1' %}On Battery{% else %}Unknown{% endif %}",
        "icon": "mdi:battery-charging",
        "device": {
            "identifiers": [device_id],
            "manufacturer": "EZVIZ",
            "model": "Doorbell",
            "name": f"EZVIZ {device_id}",
        }
    }
    mqtt_client.publish(charging_discovery_topic, json.dumps(charging_payload), retain=True)
    log.info("Published Doorbell Charging Status discovery config to topic: %s", charging_discovery_topic)

    # Alarm Time Discovery (device_id variable)
    alarm_time_discovery_topic = f"homeassistant/sensor/{device_id}_alarm_time/config"
    alarm_time_payload = {
        "name": "Alarm Time",
        "unique_id": f"alarm_time_{device_id}",
        "state_topic": f"{mqtt_topic}/{device_id}/ys.alarm/alarmTime",
        "value_template": "{{ value | as_timestamp | timestamp_local }}",
        "device_class": "timestamp",
        "icon": "mdi:alarm-light",
        "device": {
            "identifiers": [device_id],
            "manufacturer": "EZVIZ",
            "model": "Doorbell",
            "name": f"EZVIZ {device_id}",
        }
    }
    mqtt_client.publish(alarm_time_discovery_topic, json.dumps(alarm_time_payload), retain=True)
    log.info("Published Alarm Time discovery config to topic: %s", alarm_time_discovery_topic)

    # Calling Time Discovery (device_id variable)
    calling_time_discovery_topic = f"homeassistant/sensor/{device_id}_calling_time/config"
    calling_time_payload = {
        "name": "Calling Time",
        "unique_id": f"calling_time_{device_id}",
        "state_topic": f"{mqtt_topic}/{device_id}/ys.calling/timestamp",
        "value_template": "{{ value | as_timestamp | timestamp_local }}",
        "device_class": "timestamp",
        "icon": "mdi:phone",
        "device": {
            "identifiers": [device_id],
            "manufacturer": "EZVIZ",
            "model": "Doorbell",
            "name": f"EZVIZ {device_id}",
        }
    }
    mqtt_client.publish(calling_time_discovery_topic, json.dumps(calling_time_payload), retain=True)
    log.info("Published Calling Time discovery config to topic: %s", calling_time_discovery_topic)

    # EZVIZ 报警图片 Discovery 

    alarm_picture_discovery_topic = f"homeassistant/camera/{device_id}_alarm_picture/config"
    alarm_picture_payload = {
        "name": "Alarm Picture",
        "unique_id": "alarm_picture_{device_id}",
        "topic": f"{mqtt_topic}/{device_id}/ys.alarm/pictureList/0/url",
        "image_encoding": "b64",
        "device_class": "camera",
        "device": {
            "identifiers": [device_id],
            "manufacturer": "EZVIZ",
            "model": "Doorbell",
            "name": f"EZVIZ {device_id}",
            }
        }
    mqtt_client.publish(alarm_picture_discovery_topic, json.dumps(alarm_picture_payload), retain=True)
    log.info("Published EZVIZ Alarm Picture discovery config to topic: %s", alarm_picture_discovery_topic)

    # EZVIZ Calling Picture Discovery 

    calling_picture_discovery_topic = f"homeassistant/camera/{device_id}_calling_picture/config"
    calling_picture_payload = {
        "name": "Calling Picture",
        "unique_id": "calling_picture_{device_id}",
        "topic": f"{mqtt_topic}/{device_id}/ys.calling/coverUrl/url",
        "image_encoding": "b64",
        "device_class": "camera",
        "device": {
            "identifiers": [device_id],
            "manufacturer": "EZVIZ",
            "model": "Doorbell",
            "name": f"EZVIZ {device_id}",
            }
        }
    mqtt_client.publish(calling_picture_discovery_topic, json.dumps(calling_picture_payload), retain=True)
    log.info("Published Calling Picture discovery config to topic: %s", calling_picture_discovery_topic)

# MQTT callbacks
def on_connect(client, userdata, flags, rc, properties=None):
    log.info("Connected to MQTT broker with result code: %s", rc)

def on_publish(client, userdata, mid, *args, **kwargs):
    log.info("on_publish called with mid: %s, args: %s, kwargs: %s", mid, args, kwargs)

# Initialize MQTT client with versioned callback API
mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqtt_client.on_connect = on_connect
mqtt_client.on_publish = on_publish
mqtt_client.username_pw_set(mqtt_username, mqtt_password)
mqtt_client.connect(mqtt_broker, mqtt_port, 60)
mqtt_client.loop_start()

# Helper function to recursively publish JSON to MQTT
def publish_json(client, base_topic, key, value, retain=True):
    if isinstance(value, dict):
        for sub_key, sub_value in value.items():
            if sub_key == "url" and isinstance(sub_value, str) and sub_value.startswith("https"):
                # 通过request读取sub_value的链接，并把这个链接的内容用base64编码，重新赋值给sub_value
                try:
                    response = requests.get(sub_value)
                    response.raise_for_status()
                    encoded_content = base64.b64encode(response.content).decode('utf-8')
                    sub_value = value[sub_key] = encoded_content
                    log.info("Fetched and base64-encoded content from URL: %s", sub_value[:60])
                except Exception as e:
                    log.error("Failed to fetch or encode URL %s: %s", sub_value, e)

            log.info("Publishing key: %s, sub_key: %s, sub_value: %s to MQTT", key, sub_key, sub_value[:60])
            publish_json(client, base_topic, f"{key}/{sub_key}", sub_value, retain)
    elif isinstance(value, list):
        if not value:  # If the list is empty
            topic = f"{base_topic}/{key}"
            result, mid = client.publish(topic, "[]", retain=retain)
            if result == mqtt.MQTT_ERR_SUCCESS:
                log.info("Published empty list to topic: %s", topic)
            else:
                log.error("Failed to publish to topic: %s", topic)
        else:
            for index, item in enumerate(value):
                publish_json(client, base_topic, f"{key}/{index}", item, retain)
    else:
        topic = f"{base_topic}/{key}"
        payload = str(value)  # Convert value to string
        log.info("Publishing to topic: %s with payload: %s", topic, payload)
        result, mid = client.publish(topic, payload, retain=retain)
        if result == mqtt.MQTT_ERR_SUCCESS:
            log.info("Published to topic: %s with payload: %s", topic, payload)
        else:
            log.error("Failed to publish to topic: %s", topic)

# HTTP server request handler
class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode('utf-8')
        headers = self.headers

        log.info("Message received at %s, Headers: %s, Body: %s",
                 self.log_date_time_string(),
                 json.dumps(dict(headers)),
                 body)

        try:
            receive_message = json.loads(body)  # Parse JSON body

            # Extract deviceId and type from the header
            device_id = receive_message.get('header', {}).get('deviceId', 'unknown')
            message_type = receive_message.get('header', {}).get('type', 'unknown')

            # Construct the base MQTT topic dynamically
            base_topic = f"{mqtt_topic}/{device_id}/{message_type}"
            log.info("Constructed base MQTT topic: %s", base_topic)

            # Home Assistant discovery: 只在首次收到该device_id时推送discovery配置
            # 这里简单处理：每次都推送一次（可根据实际需求优化为只推送一次）
            if device_id != "unknown":
                publish_ha_discovery(device_id)

            # Iterate over the body data and publish to MQTT
            body_data = receive_message.get('body', {})
            for key, value in body_data.items():
                log.info("Publishing key: %s, value: %s to MQTT", key, value)
                publish_json(mqtt_client, base_topic, key, value)


        except Exception as e:
            log.error("Error processing message: %s", e)
            self.send_response(500)  # Internal server error
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_response = json.dumps({"error": "Internal Server Error", "message": str(e)})
            self.wfile.write(error_response.encode('utf-8'))
            return

        # Respond to the client
        message_id = receive_message.get('header', {}).get('messageId', '')
        result = {"messageId": message_id}
        response = json.dumps(result)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))
        log.info("Response sent: %s", json.dumps(result))

# Function to run the HTTP server
def run(server_class=HTTPServer, handler_class=RequestHandler, port=7777):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Listening on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
