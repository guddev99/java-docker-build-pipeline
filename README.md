# Welcome to the Java Docker Build Pipeline Repository!

This repository contains Jenkins pipeline script that automates the build, test, and analysis processes for a Java application. It leverages shared libraries and integrates with various tools such as Maven, SonarQube, and Docker Hub to streamline the development workflow. With stages for compiling, testing, and building Docker images, this pipeline facilitates continuous integration and delivery (CI/CD) practices.

## Requirements

- Jenkins installed and configured
- Docker installed on the Jenkins agent or server
- Maven installed on the Jenkins agent or server
- SonarQube server accessible for static code analysis
- Access to Docker Hub for pushing Docker images

## Setup

1. Import the shared library named 'my-shared-library' into Jenkins. You can find the shared library repository at [guddev99/jenkins_shared_library](https://github.com/guddev99/jenkins_shared_library).
2. Create a new Jenkins pipeline job and configure it to use this pipeline script.
3. Ensure that the necessary plugins for Maven, Docker, and SonarQube integration are installed in Jenkins.


## Jenkins Shared Library

The Jenkins pipeline script in this repository utilizes a shared library named 'my-shared-library'. The shared library is maintained separately at [guddev99/jenkins_shared_library](https://github.com/guddev99/jenkins_shared_library). Make sure to import this shared library into Jenkins as part of the setup process.


## Pipeline Overview

### Parameters

- `action`: Choose between 'create' and 'delete' to specify whether to create or destroy resources.
- `ImageName`: Name of the Docker image to build.
- `ImageTag`: Tag of the Docker image.
- `DockerHubUser`: Docker Hub username for pushing Docker images.

### Stages

1. **Git Checkout**: Checks out the source code from the specified Git repository.
2. **Unit Test Maven**: Executes unit tests using Maven.
3. **Integration Test Maven**: Executes integration tests using Maven.
4. **Static code analysis: Sonarqube**: Runs static code analysis using SonarQube.
5. **Quality Gate Status Check: Sonarqube**: Checks the quality gate status using SonarQube.
6. **Maven Build**: Builds the project using Maven.
7. **Docker Image Build**: Builds a Docker image with the specified parameters.
8. **Docker Image Scan: Trivy**: Scans the Docker image for vulnerabilities using Trivy.
9. **Docker Image Push: DockerHub**: Pushes the Docker image to Docker Hub.
10. **Docker Image Cleanup: DockerHub**: Cleans up the Docker image from Docker Hub.

### Usage

- Run the Jenkins pipeline job and select the desired parameters.
- The pipeline will execute the specified stages based on the chosen action.
- Monitor the Jenkins console output for build progress and any errors.
- Review the generated artifacts and Docker images in Docker Hub.

---

**Note**: This README provides a high-level overview of the Jenkins pipeline script. Ensure that all tools and configurations are set up correctly before running the pipeline. For detailed instructions on Jenkins setup and configuration, refer to the official documentation.

