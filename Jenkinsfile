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
                // Run the container in detached mode, exposing the necessary ports
                bat 'docker run -d -p 8001:8000 svm'
            }
        }

        // stage('Install Test Dependencies') {
        //     steps {
        //         // Install the required dependencies (like pytest) inside the Docker container
        //         bat 'docker exec svm pip install pytest'  // Assuming you need to install pytest
        //     }
        // }

        stage('Run Tests') {
            steps {
                // Run the tests inside the running Docker container
                bat 'docker exec svm pytest app/svm_service/test_svm_service.py -v'  // Replace with the actual path to the tests
            }
        }

        stage('Deploy') {
            steps {
                echo 'App deployed'
            }
        }
    }
}
