pipeline {
    agent any
    environment {
        DOCKER_USER = 'daroori'
        IMAGE_NAME = 'devopshub-api'
        IMAGE_TAG = "${env.BUILD_NUMBER}"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                echo 'Building Backend Image...'
                sh "docker build -t ${DOCKER_USER}/${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }
        stage('Test Health') {
            steps {
                echo 'Verifying Container...'
                // Run a quick temporary container to check python version
                sh "docker run --rm ${DOCKER_USER}/${IMAGE_NAME}:${TAG} python --version"
            }
            }
        stage('Push Docker Image') {
            steps {
                echo "Pushing Image ${DOCKER_USER}/${IMAGE_NAME}:${TAG} to Docker Hub..."
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                    sh "echo ${DOCKER_PASSWORD} | docker login -u ${DOCKER_USERNAME} --password-stdin"
                    sh "docker push ${DOCKER_USER}/${IMAGE_NAME}:${TAG}"
                    sh "docker tag ${DOCKER_USER}/${IMAGE_NAME}:${TAG} ${DOCKER_USER}/${IMAGE_NAME}:latest"
                    sh "docker push ${DOCKER_USER}/${IMAGE_NAME}:latest"
                    sh "docker logout"
                }
            }
        }
        stage('Deploy top Kubernetes') {
            steps {
                echo 'Deploying to K3s Cluster...'
               // This command updates the existing K8s deployment with the new image tag.
                // We will fix the 'kubectl' setup in the next step.
                sh "kubectl set image deployment/devopshub-api devopshub-api=${DOCKER_USER}/${IMAGE_NAME}:${TAG} -n default"
            }
        }
    }
}