#!/bin/sh
echo "----------------------------------------"
echo "请认准公众号【老王杂谈说】，其它未标明出处的均为侵权"
echo "恶意未标明出处，占为己有，与偷窃无异，令人不齿"
echo "唯一官方网站：https://www.hasscn.top"
echo "----------------------------------------"
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