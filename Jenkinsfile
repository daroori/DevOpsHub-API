pipeline {
    agent any
    environment {
        DOCKER_USER = 'daroori'
        IMAGE_NAME = 'devopshub-api'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                echo "Building Image for Build #${env.BUILD_NUMBER}..."
                sh "docker build -t ${env.DOCKER_USER}/${env.IMAGE_NAME}:${env.BUILD_NUMBER} ."
            }
        }
        stage('Test Health') {
            steps {
                echo 'Verifying Container...'
                // Run a quick temporary container to check python version
                sh "docker run --rm ${env.DOCKER_USER}/${env.IMAGE_NAME}:${env.BUILD_NUMBER} python --version"
            }
            }
        stage('Push Docker Image') {
            steps {
                echo "Pushing Image ${env.DOCKER_USER}/${env.IMAGE_NAME}:${env.BUILD_NUMBER} to Docker Hub..."
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                    sh "echo ${DOCKER_PASSWORD} | docker login -u ${DOCKER_USERNAME} --password-stdin"
                    sh "docker push ${env.DOCKER_USER}/${env.IMAGE_NAME}:${env.BUILD_NUMBER}"
                    sh "docker tag ${env.DOCKER_USER}/${env.IMAGE_NAME}:${env.BUILD_NUMBER} ${env.DOCKER_USER}/${env.IMAGE_NAME}:latest"
                    sh "docker push ${env.DOCKER_USER}/${env.IMAGE_NAME}:latest"
                    sh "docker logout"
                }
            }
        }
        stage('Deploy top Kubernetes') {
            steps {
                echo 'Deploying to K3s Cluster...'
               // This command updates the existing K8s deployment with the new image tag.
                // We will fix the 'kubectl' setup in the next step.
                sh "kubectl set image deployment/devopshub-api devopshub-api=${env.DOCKER_USER}/${env.IMAGE_NAME}:${env.BUILD_NUMBER} -n default"
            }
        }
    }
}