#FROM openjdk:17-jdk-slim
#WORKDIR /app
#COPY build/libs/load-0.0.1-SNAPSHOT.jar /app/load-test.jar
#CMD ["java", "-jar", "/app/load-test.jar"]
# EXPOSE 8081
FROM openjdk:17-jdk-slim
ARG JAR_FILE=build/libs/*.jar
COPY ${JAR_FILE} app.jar
ENTRYPOINT ["java", "-jar", "/app.jar"]

