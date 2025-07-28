#!/bin/sh
token=$(jq -r '.token' /data/options.json)

APP_URL='https://fw.koolcenter.com/binary/ddnsto/linux'
app_aarch64='ddnsto.arm64'
app_x86='ddnsto.amd64'
bin_path='/data/ddnsto'

if echo `uname -m` | grep -Eqi 'x86_64'; then
    arch='x86_64'
    URL="${APP_URL}/${app_x86}"
elif  echo `uname -m` | grep -Eqi 'aarch64'; then
    arch='aarch64'
    URL="${APP_URL}/${app_aarch64}"
else
    error "The program only supports x86_64 & aarch64."
    exit 1
fi

if [ -f "/data/ddnsto" ];then
echo `ddnsto exist`
else
curl -sSLk ${URL} -o ${bin_path}
fi
chmod +x /data/ddnsto
/data/ddnsto  -u $token 