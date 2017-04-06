#!/bin/bash
if [ -z ${1+x} ]; then
  exit 1
fi

echo "remote $PUBLIC_IP 1194" > $1
cat <<EOF >> $1
client
dev tun
cipher BF-CBC
proto tcp
resolv-retry infinite
nobind
;user nobody
;group nobody
persist-key
persist-tun
ca ca.crt
cert client.crt
key client.key
comp-lzo
verb 3
EOF
