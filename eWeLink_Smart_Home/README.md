# eWeLink Smart Home

## Help

-   如果遇到`Failed to call service xxxxx/xxxxxxx. Service not found.`的问题。建议使用 HomeAssistant 自带的 Addon`File editor`编辑`configuration.yaml`。在文件尾部追加以下内容：

```
switch:
  - platform: template
    switches:
      ewelink_virtual_switch:
        turn_on:
          service: switch.turn_on
        turn_off:
          service: switch.turn_off

cover:
  - platform: template
    covers:
      ewelink_virtual_cover:
        open_cover:
          service: cover.open_cover
        close_cover:
          service: cover.close_cover
        stop_cover:
          service: cover.stop_cover
        set_cover_position:
          service: cover.set_cover_position

fan:
  - platform: template
    fans:
      ewelink_virtual_fan:
        value_template: "{{ states('input_boolean.state') }}"
        turn_on:
          service: fan.turn_on
        turn_off:
          service: fan.turn_off
        set_preset_mode:
          service: fan.set_preset_mode

light:
  - platform: template
    lights:
      ewelink_virtual_light:
        turn_on:
          service: light.turn_on
        turn_off:
          service: light.turn_off
```

保存成功后重启 HomeAssistant 即可
