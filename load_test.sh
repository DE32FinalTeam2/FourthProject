#!/bin/bash

docker exec -it spark-master /opt/bitnami/spark/bin/spark-submit \
  --class org.apache.spark.examples.SparkPi \
  --master spark://spark-master:7077 \
  /opt/bitnami/spark/examples/jars/spark-examples_2.12-3.5.3.jar 1000

