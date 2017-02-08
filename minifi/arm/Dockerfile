FROM wiii/arm-java
LABEL maintainer="Mal Thirus <malcolm.thirus@gmail.com>"

ARG MINIFI_VERSION=0.1.0
ENV MINIFI_HOME=/opt/minifi

RUN set -x \
        && curl -kLf https://dist.apache.org/repos/dist/release/nifi/KEYS -o /tmp/nifi-keys.txt \
        && gpg --import /tmp/nifi-keys.txt \
        && curl -kLf https://archive.apache.org/dist/nifi/minifi/$MINIFI_VERSION/minifi-$MINIFI_VERSION-bin.tar.gz -o /tmp/minifi-bin.tar.gz \
        && curl -kLf https://archive.apache.org/dist/nifi/minifi/$MINIFI_VERSION/minifi-$MINIFI_VERSION-bin.tar.gz.asc -o /tmp/minifi-bin.tar.gz.asc \
        && curl -kLf https://archive.apache.org/dist/nifi/minifi/$MINIFI_VERSION/minifi-$MINIFI_VERSION-bin.tar.gz.md5 -o /tmp/minifi-bin.tar.gz.md5 \
        && curl -kLf https://archive.apache.org/dist/nifi/minifi/$MINIFI_VERSION/minifi-$MINIFI_VERSION-bin.tar.gz.sha1 -o /tmp/minifi-bin.tar.gz.sha1 \
        && gpg --verify /tmp/minifi-bin.tar.gz.asc /tmp/minifi-bin.tar.gz \
        && echo "$(cat /tmp/minifi-bin.tar.gz.md5) /tmp/minifi-bin.tar.gz" | md5sum -c - \
        && echo "$(cat /tmp/minifi-bin.tar.gz.sha1) /tmp/minifi-bin.tar.gz" | sha1sum -c - \
        && mkdir -p $MINIFI_HOME \
        && tar -z -x -f /tmp/minifi-bin.tar.gz -C $MINIFI_HOME --strip-components=1 \
        && rm /tmp/minifi-bin.tar.gz /tmp/minifi-bin.tar.gz.asc /tmp/minifi-bin.tar.gz.md5 /tmp/minifi-bin.tar.gz.sha1 \
        && rm /tmp/nifi-keys.txt \
        && rm $MINIFI_HOME/conf/config.yml \
        && groupadd minifi \
        && useradd -r -g minifi minifi \
        && bash -c "mkdir -p $MINIFI_HOME/{database_repository,flowfile_repository,content_repository,provenance_repository}" \
        && chown minifi:minifi -R $MINIFI_HOME

VOLUME ["$MINIFI_HOME/database_repository", "$MINIFI_HOME/flowfile_repository", "$MINIFI_HOME/content_repository", "$MINIFI_HOME/provenance_repository"]

USER minifi
WORKDIR $MINIFI_HOME
CMD ["bin/minifi.sh","run"]
