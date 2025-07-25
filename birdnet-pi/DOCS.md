# 麦克风注意事项

关键要素是麦克风质量：一个 Boya By-lm 40 或 Clippy EM272（带有一个非常好的辅助USB转换器）对于提高检测质量至关重要。

这里是一些我做的示例测试（整个线程也非常有趣）：

- <https://github.com/mcguirepr89/BirdNET-Pi/discussions/39#discussioncomment-9706951>
- <https://github.com/mcguirepr89/BirdNET-Pi/discussions/1092#discussioncomment-9706191>

**我的建议：**

- **最佳入门级系统（<50欧元）：** Boya By-lm40（30欧元）+ deadcat（10欧元）
- **最佳中端系统（<150欧元）：** Clippy EM272 TRS/TRRS（55欧元）+ Rode AI micro trs/trrs to usb（70欧元）+ Rycote deadcat（27欧元）
- **最佳高端系统（<400欧元）：** Clippy EM272 XLR（85欧元）或 LOM Ucho Pro（75欧元）+ Focusrite Scarlet 2i2 4th Gen（200欧元）+ Bubblebee Pro Extreme deadcat（45欧元）

**欧洲高端麦克风的来源：**

- Clippy (EM272): <https://www.veldshop.nl/en/clippy-xlr-em272z1-mono-microphone.html>
- LOM (EM272): <https://store.lom.audio/collections/basicucho-series>
- Immersive sound (AOM5024): <https://immersivesoundscapes.com/earsight-standard-v2/>

# 应用设置建议

我通过并行运行两个版本的我的HA birdnet-pi附加程序，使用相同的RTSP源，并比较参数的影响，测试了大量的设置。我的结论并非普遍适用，因为这似乎高度依赖于地区和使用的麦克风类型。例如，旧型号在澳大利亚似乎更好，而新型号在欧洲更好。

- **型号**
  - **版本：** 6k_v2.4 _(至少在欧洲表现更好，6k在澳大利亚表现更好)_
  - **物种范围模型：** v1 _(取消勾选v2.4；在欧洲似乎更稳健)_
  - **物种出现阈值：** 0.001 _(使用v2.4时为0.00015；使用物种列表测试器检查您正确的值)_
- **音频设置**
  - **默认**
  - **通道：** 1 _(由于分析是在单声道信号上进行的，所以这并不重要；1允许减少保存的音频大小，但在我 Experience 中似乎会稍微弄乱频谱图)_
  - **录制长度：** 18 _(这是因为我使用0.5的重叠；所以它分析0-3秒，2.5-5.5秒，5-8秒，7.5-10.5秒，10-13秒，12.5-15.5秒，15-18秒)_
  - **提取长度：** 9秒 _(可以是6，但我喜欢听到我的鸟儿 :-))_
  - **音频格式：** mp3 _(为什么要费心使用其他格式)_
- **Birdnet-lite设置**
  - **重叠：** 0.5秒
  - **最小置信度：** 0.7
  - **Sigmoid灵敏度：** 1.25 _(我试过1.00，但它产生了更多的误报；降低此值会增加灵敏度)_

# 设置RTSP服务器

灵感来自：<https://github.com/mcguirepr89/BirdNET-Pi/discussions/1006#discussioncomment-6747450>

<details>
<summary>在你的桌面上</summary>

- 下载imager
- 安装raspbian lite 64

</details>

<details>
<summary>通过ssh，安装必需的软件</summary>

```bash
# 更新
sudo apt-get update -y
sudo apt-get dist-upgrade -y

# 安装RTSP服务器
sudo apt-get install -y micro ffmpeg lsof
sudo -s cd /root && wget -c https://github.com/bluenviron/mediamtx/releases/download/v1.9.1/mediamtx_v1.9.1_linux_arm64v8.tar.gz -O - | sudo tar -xz
```
</details>

<details>
<summary>配置音频</summary>

### 找到正确的设备

```bash
# 列出音频设备
arecord -l

# 检查音频设备参数。例如：
arecord -D hw:1,0 --dump-hw-params
```

### 添加启动脚本

```bash
sudo nano startmic.sh && chmod +x startmic.sh
```

粘贴以下内容：

```bash
#!/bin/bash
echo "Starting birdmic"

# 禁用千兆以太网
sudo ethtool -s eth0 speed 100 duplex full autoneg on

# 检测Scarlett 2i2卡索引 - 如果您使用该卡，则相关
SCARLETT_INDEX=$(arecord -l | grep -i "Scarlett" | awk '{print $2}' | sed 's/://')

if [ -z "$SCARLETT_INDEX" ]; then
    echo "Error: Scarlett 2i2 not found! Using 0 as default"
    SCARLETT_INDEX="0"
fi

# 首先启动mediamtx，并给它一点时间初始化
./mediamtx &
sleep 5

# 运行ffmpeg
ffmpeg -nostdin -use_wallclock_as_timestamps 1 -fflags +genpts -f alsa -acodec pcm_s16be -ac 2 -ar 96000 -i plughw:$SCARLETT_INDEX,0 -ac 2 -f rtsp -acodec pcm_s16be rtsp://localhost:8554/birdmic -rtsp_transport tcp -buffer_size 512k 2>/tmp/rtsp_error &

# 设置麦克风音量
sleep 5
MICROPHONE_NAME="Line In 1 Gain" # 对于Focusrite Scarlett 2i2
sudo amixer -c 0 sset "$MICROPHONE_NAME" 40

sleep 60

# 如果存在，运行focusrite和autogain脚本
if [ -f "$HOME/focusrite.sh" ]; then
    sudo python3 -u "$HOME/focusrite.sh" >/tmp/log_focusrite 2>/tmp/log_focusrite_error &
fi

if [ -f "$HOME/autogain.py" ]; then
    sudo python3 -u "$HOME/autogain.py" >/tmp/log_autogain 2>/tmp/log_autogain_error &
fi
```
</details>

<details>
<summary>可选：使用gstreamer而不是ffmpeg</summary>

```bash
# 安装gstreamer
sudo apt-get update
#sudo apt-get install -y \
#  gstreamer1.0-rtsp \
#  gstreamer1.0-tools \
#  gstreamer1.0-alsa \
#  gstreamer1.0-plugins-base \
#  gstreamer1.0-plugins-good \
#  gstreamer1.0-plugins-bad \
#  gstreamer1.0-plugins-ugly \
#  gstreamer1.0-libav
apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio -y
```

创建一个名为 `rtsp_audio_server.py` 的脚本：

```python
#!/usr/bin/env python3

import gi
import sys
import logging
import os
import signal

gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')

from gi.repository import Gst, GstRtspServer, GLib

# 初始化GStreamer
Gst.init(None)

# 配置日志记录
LOG_FILE = "gst_rtsp_server.log"
logging.basicConfig(
    filename=LOG_FILE,
    filemode='a',
    format='%(asctime)s %(levelname)s: %(message)s',
    level=logging.DEBUG  # 设置为DEBUG以获取全面日志记录
)
logger = logging.getLogger(__name__)

class AudioFactory(GstRtspServer.RTSPMediaFactory):
    def __init__(self):
        super(AudioFactory, self).__init__()
        self.set_shared(True)
        self.set_latency(500)
        self.set_suspend_mode(GstRtspServer.RTSPSuspendMode.NONE)
        logger.debug("AudioFactory initialized: shared=True, latency=500ms, suspend_mode=NONE.")

    def do_create_element(self, url):
        pipeline_str = (
            "alsasrc device=plughw:0,0 do-timestamp=true buffer-time=2000000 latency-time=1000000 ! "
            "queue max-size-buffers=0 max-size-bytes=0 max-size-time=0 ! "
            "audioconvert ! "
            "audioresample ! "
            "audio/x-raw,format=S16BE,channels=2,rate=48000 ! "
            "rtpL16pay name=pay0 pt=96"
        )
        logger.debug(f"Creating GStreamer pipeline: {pipeline_str}")
        try:
            pipeline = Gst.parse_launch(pipeline_str)
            if not pipeline:
                logger.error("Failed to parse GStreamer pipeline.")
                return None
            return pipeline
        except Exception as e:
            logger.error(f"Exception while creating pipeline: {e}")
            return None

class GstServer:
    def __init__(self):
        self.server = GstRtspServer.RTSPServer()
        self.server.set_service("8554")
        self.server.set_address("0.0.0.0")
        logger.debug("RTSP server configured: address=0.0.0.0, port=8554.")

        factory = AudioFactory()
        mount_points = self.server.get_mount_points()
        mount_points.add_factory("/birdmic", factory)
        logger.debug("Factory mounted at /birdmic.")

        self.server.attach(None)
        logger.info("RTSP server attached and running.")

def main():
    server = GstServer()
    print("RTSP server is running at rtsp://localhost:8554/birdmic")
    logger.info("RTSP server is running at rtsp://localhost:8554/birdmic")

    loop = GLib.MainLoop()

    def shutdown(signum, frame):
        logger.info(f"Shutting down RTSP server due to signal {signum}.")
        print("\nShutting down RTSP server.")
        loop.quit()

    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    try:
        loop.run()
    except Exception as e:
        logger.error(f"Main loop encountered an exception: {e}")
    finally:
        logger.info("RTSP server has been shut down.")

if __name__ == "__main__":
    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, 'w').close()

    main()
```
</details>

<details>
<summary>可选：自动启动</summary>

```bash
chmod +x startmic.sh
crontab -e # 选择nano作为你的编辑器
```
粘贴以下内容：

```bash
@reboot $HOME/startmic.sh
```

然后保存并退出nano。
重启Pi并使用VLC再次测试，以确保RTSP流是活跃的。

</details>

<details>
<summary>可选：禁用不必要的元素</summary>

- **优化config.txt**

```bash
sudo nano /boot/firmware/config.txt
```

粘贴以下内容：

```ini
# 启用音频和USB优化
dtparam=audio=off          # 禁用默认的板载音频以防止冲突
dtoverlay=disable-bt        # 禁用板载蓝牙以减少USB带宽使用
dtoverlay=disable-wifi      # 禁用板载wifi
# 将以太网限制在100 Mbps（禁用千兆以太网）
dtparam=eth_max_speed=100
# USB优化
dwc_otg.fiq_fix_enable=1    # 启用FIQ（快速中断）处理以改善USB性能
max_usb_current=1           # 增加可用的USB电流（如果Scarlett通过USB供电则需要）
# 额外的音频设置（用于低延迟操作）
avoid_pwm_pll=1             # 使用更稳定的PLL为音频时钟
# 可选：如果不需要，可以关闭HDMI和其他设置
hdmi_blanking=1             # 禁用HDMI（节省电源并减少干扰）
```

- **禁用无用的服务**

```bash
# 禁用无用的服务
sudo systemctl disable hciuart
sudo systemctl disable bluetooth
sudo systemctl disable triggerhappy
sudo systemctl disable avahi-daemon
sudo systemctl disable dphys-swapfile
sudo systemctl disable hciuart.service

# 禁用蓝牙
for element in bluetooth btbcm hci_uart btintel btrtl btusb; do
    sudo sed -i "/$element/d" /etc/modprobe.d/raspi-blacklist.conf
    echo "blacklist $element" | sudo tee -a /etc/modprobe.d/raspi-blacklist.conf
done

# 禁用您的树莓派的视频（包括V4L2）
for element in bcm2835_v4l2 bcm2835_codec bcm2835_isp videobuf2_vmalloc videobuf2_memops videobuf2_v4l2 videobuf2_common videodev; do
    sudo sed -i "/$element/d" /etc/modprobe.d/raspi-blacklist.conf
    echo "blacklist $element" | sudo tee -a /etc/modprobe.d/raspi-blacklist.conf
done

# 禁用WiFi电源管理
sudo iw dev wlan0 set power_save off
for element in brcmfmac brcmutil; do
    sudo sed -i "/$element/d" /etc/modprobe.d/raspi-blacklist.conf
    echo "blacklist $element" | sudo tee -a /etc/modprobe.d/raspi-blacklist.conf
done

# 禁用USB电源管理
echo 'on' | sudo tee /sys/bus/usb/devices/usb*/power/control

# 防止树莓派进入省电模式
sudo apt update
sudo apt install -y cpufrequtils
echo 'GOVERNOR="performance"' | sudo tee /etc/default/cpufrequtils
sudo systemctl disable ondemand
sudo systemctl stop ondemand
```
</details>

<details>
<summary>可选：安装Focusrite驱动程序</summary>

```bash
sudo apt-get install make linux-headers-$(uname -r)
curl -LO https://github.com/geoffreybennett/scarlett-gen2/releases/download/v6.9-v1.3/snd-usb-audio-kmod-6.6-v1.3.tar.gz
tar -xzf snd-usb-audio-kmod-6.6-v1.3.tar.gz
cd snd-usb-audio-kmod-6.6-v1.3
KSRCDIR=/lib/modules/$(uname -r)/build
make -j4 -C $KSRCDIR M=$(pwd) clean
make -j4 -C $KSRCDIR M=$(pwd)
sudo make -j4 -C $KSRCDIR M=$(pwd) INSTALL_MOD_DIR=updates/snd-usb-audio modules_install
sudo depmod
sudo reboot
dmesg | grep -A 5 -B 5 -i focusrite
```
</details>

<details>
<summary>可选：添加RAM磁盘</summary>

```bash
sudo cp /usr/share/systemd/tmp.mount /etc/systemd/system/tmp.mount
sudo systemctl enable tmp.mount
sudo systemctl start tmp.mount
```
</details>

<details>
<summary>可选：Focusrite Scarlett 2i2的配置</summary>

在`$HOME/focusrite.sh`中添加此内容并运行：

```bash
chmod +x "$HOME/focusrite.sh"
```

查看：<https://github.com/alexbelgium/Birdnet-tools/blob/main/focusrite.sh>

</details>

<details>
<summary>可选：麦克风的自动增益脚本</summary>

在`$HOME/autogain.py`中添加此内容并运行：

```bash
chmod +x "$HOME/autogain.py"
```

查看：<https://github.com/alexbelgium/Birdnet-tools/blob/main/autogain.py>

</details>