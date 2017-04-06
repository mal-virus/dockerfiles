FROM mkobit/nifi

COPY nars /opt/nifi/lib
ADD credentials .
RUN sed -i 's/nifi\.remote\.input\.host=/nifi\.remote\.input\.host=192.168.1.28/g' $NIFI_HOME/conf/nifi.properties && \
    sed -i 's/nifi\.remote\.input\.socket\.port=/nifi\.remote\.input\.socket\.port=8082/g' $NIFI_HOME/conf/nifi.properties && \
    sed -i 's/nifi\.remote\.input\.secure=.*/nifi\.remote\.input\.secure=false/g' $NIFI_HOME/conf/nifi.properties

EXPOSE 8082
