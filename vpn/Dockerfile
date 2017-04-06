FROM ubuntu:16.04

ADD office.conf /etc/openvpn/office.conf
ADD genkeys.sh /usr/share/easy-rsa/genkeys.sh
ADD vars /usr/share/easy-rsa/vars
ADD office.up /etc/openvpn/office.up
ADD openvpn-shutdown.sh /etc/openvpn-shutdown.sh
ADD genclientconfig.sh /usr/share/easy-rsa/genclientconfig.sh

RUN apt-get update && apt-get -y upgrade && \
    apt-get -y -q install openvpn easy-rsa python-pip python-setuptools zip dos2unix && \
    pip install https://s3.amazonaws.com/cloudformation-examples/aws-cfn-bootstrap-latest.tar.gz && \
    /usr/local/bin/cfn-init --stack $StackName --resource VPNInstance --region $region && \
    echo "alias ll='ls -lah --color=auto'" >> /etc/profile && \
    chmod +x /usr/share/easy-rsa/genkeys.sh && \
    chmod +x /usr/share/easy-rsa/genclientconfig.sh && \
    chmod +x /etc/openvpn/office.up && \
    chmod +x /etc/openvpn/openvpn-startup.sh && \
    chmod +x /etc/openvpn/openvpn-shutdown.sh && \
    sed -i 's/exit 0//g' /etc/rc.local && \
    /usr/share/easy-rsa/genkeys.sh && \
    /usr/share/easy-rsa/genclientconfig.sh /usr/share/easy-rsa/keys/$NAME.ovpn && \
    unix2dos /usr/share/easy-rsa/keys/$NAME.ovpn && \
    zip -j VPN.zip /usr/share/easy-rsa/keys/ca.crt /usr/share/easy-rsa/keys/client.crt /usr/share/easy-rsa/keys/client.key /usr/share/easy-rsa/keys/$NAME.ovpn && \
    echo "net.ipv4.ip_forward=1" >> /etc/sysctl.conf && \
    sysctl -p && \
    

ENTRYPOINT ["openvpn","--config","/etc/openvpn/office.conf"]
RUN ["--script-security","2"]
