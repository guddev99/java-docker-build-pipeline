# Use the official OpenJDK 8 Alpine image as base
FROM openjdk:8-jdk-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the JAR file from the host machine to the container's working directory
COPY ./target/*.jar /app.jar

# Define the command to run the application when the container starts
CMD ["java", "-jar", "app.jar"]
