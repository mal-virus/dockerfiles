FROM ubuntu:16.04

ENV DAITAKU_HOME=/opt/daitaku DAITAKU_PORT=11000 DAITAKU_VERSION=4.0.1

RUN apt-get update && apt-get upgrade -y && apt-get install curl -y && \
    mkdir /usr/local/daitaku && \
    curl -Lf https://downloads.dataiku.com/public/studio/$DAITAKU_VERSION/dataiku-dss-$DAITAKU_VERSION.tar.gz -o /tmp/daitaku.tar.gz && \
    tar xzf /tmp/daitaku.tar.gz -C /usr/local/daitaku --strip-components=1 && \
    mkdir $DAITAKU_HOME && \
    adduser --disabled-password --gecos "" daitaku && \
    chown -R daitaku: $DAITAKU_HOME /usr/local/daitaku && \
    /usr/local/daitaku/scripts/install/install-deps.sh -yes && \
    su - daitaku -c "/usr/local/daitaku/installer.sh -d $DAITAKU_HOME -p $DAITAKU_PORT" && \
    rm -rf /tmp/daitaku.tar.gz

USER daitaku

WORKDIR $DAITAKU_HOME

CMD ["bin/dss","run"]
