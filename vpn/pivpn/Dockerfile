FROM ubuntu:16.04

RUN apt-get update && apt-get -y -q install curl iproute net-tools apt-utils whiptail && apt-get -y -q upgrade && \
    curl -L https://install.pivpn.io > /install.pivpn && \
    sed -i "s|^#checkForDependencies$|checkForDependencies|" /install.pivpn && \
    chmod +x /install.pivpn

ENTRYPOINT ["/install.pivpn"]
