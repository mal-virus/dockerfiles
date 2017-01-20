FROM mkobit/nifi

COPY nars /opt/nifi/lib
RUN sed -i 's/nifi\.remote\.input\.host=/nifi\.remote\.input\.host=192.168.2.1/g' $NIFI_HOME/conf/nifi.properties && \
    sed -i 's/nifi\.remote\.input\.socket\.port=/nifi\.remote\.input\.socket\.port=10000/g' $NIFI_HOME/conf/nifi.properties && \
    sed -i 's/nifi\.remote\.input\.secure=.*/nifi\.remote\.input\.secure=false/g' $NIFI_HOME/conf/nifi.properties

EXPOSE 10000
