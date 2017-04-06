#!/bin/sh

sed -i "s|^nifi.web.http.host=.*$|nifi.web.http.host=$(hostname)|" $NIFI_HOME/conf/nifi.properties
sed -i "s|^nifi.cluster.node.address=.*$|nifi.cluster.node.address=$(hostname)|" $NIFI_HOME/conf/nifi.properties
sed -i "s|^nifi.remote.input.host=.*$|nifi.remote.input.host=192.168.1.28|" $NIFI_HOME/conf/nifi.properties

$NIFI_HOME/bin/nifi.sh run
