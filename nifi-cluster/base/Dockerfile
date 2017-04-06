FROM mkobit/nifi

COPY nars $NIFI_HOME/lib
ADD ./start-nifi.sh .
ADD ./start-master-nifi.sh .
ADD ./credentials credentials
RUN sed -i 's/nifi\.remote\.input\.socket\.port=/nifi\.remote\.input\.socket\.port=8081/g' $NIFI_HOME/conf/nifi.properties && \
    sed -i 's/nifi\.remote\.input\.secure=.*/nifi\.remote\.input\.secure=false/g' $NIFI_HOME/conf/nifi.properties && \
    sed -i 's/nifi.zookeeper.connect.string=.*/nifi.zookeeper.connect.string=zoo1:2181/g' $NIFI_HOME/conf/nifi.properties && \
    sed -i 's/nifi.cluster.node.protocol.port=.*/nifi.cluster.node.protocol.port=8082/g' $NIFI_HOME/conf/nifi.properties && \
    sed -i 's/nifi.cluster.is.node=.*/nifi.cluster.is.node=true/g' $NIFI_HOME/conf/nifi.properties && \
    echo "# Custom conf for cluster mode" >> $NIFI_HOME/conf/nifi.properties && \
    echo "nifi.cluster.flow.election.max.wait.time=10 sec" >> $NIFI_HOME/conf/nifi.properties && \
    echo "nifi.cluster.flow.election.max.candidates=" >> $NIFI_HOME/conf/nifi.properties

EXPOSE 8080 8081 8082

CMD ["./start-nifi.sh"]
