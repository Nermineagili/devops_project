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
        // Change to the directory where the Dockerfile is located and build the image
        bat 'cd app/svm_service && docker build -t svm .'
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
