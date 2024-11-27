pipeline {
    agent any
    stages {
        stage('checkout github') {
            steps {
                // This will check out the code from the configured Git repository
                checkout scm
            }
        }
        stage('build images') {
            steps {
                bat 'docker build -t app/svm_service/svm .'
            }
        }
        stage('run image') {
            steps {
                bat 'docker run -d -p 8000:8000 svm'
            }
        }
        stage('deploy') {
            steps {
                echo 'app deployed'
            }
        }
    }
}
