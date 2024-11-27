pipeline {
    agent any
    stages {
        stage('checkout github') {
    steps {
        // Explicitly checkout a repository from a URL
        git url: 'https://github.com/Nermineagili/devops_project.git', branch: 'master'  // Replace 'main' with the correct branch name if needed
    }
}

        stage('build images') {
            steps {
                bat 'docker build -t ./app/svm_service/svm:latest .'
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
