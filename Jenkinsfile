pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                echo 'Building Backend Image...'
                // We use the docker socket from the host
                sh 'docker build -t devopshub-api:latest .'
            }
        }
        stage('Test Health') {
            steps {
                echo 'Verifying Container...'
                // Run a quick temporary container to check python version
                sh 'docker run --rm devopshub-api:latest python --version'
            }
        }
    }
}