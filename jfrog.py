import requests


def upload_jar_to_artifactory(jfrog_repo_url, username, password, jar_file_path):
    try:
        # Constructing the upload URL
        upload_url = f"{jfrog_repo_url}/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar"

        # authentication
        auth = (username, password)

        # Read the JAR file
        with open(jar_file_path, "rb") as jar_file:
            # Upload the JAR file to Artifactory
            response = requests.put(upload_url, auth=auth, data=jar_file)

        if response.status_code == 201:
            return f"Successfully pushed {jar_file_path} to JFrog Artifactory."
        else:
            return f"Failed to push {jar_file_path} to Artifactory. Status code: {response.status_code}\n{response.text}"
    except Exception as e:
        return f"An error occurred: {str(e)}"


# main:
vm_external_ip = "54.91.124.159"
jfrog_repo_url = f"http://{vm_external_ip}:8082/artifactory/jar-push-using-python"
username = "admin"
password = "Pass@123"
pipeline_name = "java-docker-build-ci"
jar_file_path = f"/var/lib/jenkins/workspace/{pipeline_name}/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar"

result = upload_jar_to_artifactory(jfrog_repo_url, username, password, jar_file_path)
print(result)
