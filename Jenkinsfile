pipeline {
    agent any
    stages {
        stage('Checkout GitHub') {
            steps {
                // Explicitly checkout a repository from a URL
                git url: 'https://github.com/Nermineagili/devops_project.git', branch: 'master'
            }
        }

        stage('Build Images') {
            steps {
                // Change to the directory where the Dockerfile is located and build the image
                bat 'cd app/svm_service && docker build -t svm .'
            }
        }

        stage('Run Image') {
            steps {
                // Stop and remove the existing container if it exists
                bat 'docker rm -f svm || echo "No existing container to remove"'

                // Run the container in detached mode with the name 'svm'
                bat 'docker run -d -p 8002:8000 --name svm svm'
            }
        }

        stage('Run Tests') {
    steps {
        // Run the tests inside the running Docker container
        bat 'docker exec svm pytest /app/test_svm_service.py -v'
    }
}


        stage('Deploy') {
            steps {
                echo 'App deployed'
            }
        }
    }
}
