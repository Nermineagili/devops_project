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
                // Run the container in detached mode with a name
                bat 'docker run -d -p 8001:8000 --name svm svm'
            }
        }

        stage('Wait for Container') {
            steps {
                script {
                    // Wait for the container to be ready
                    sh '''
                    echo "Waiting for the container to be ready..."
                    while ! docker exec svm curl -s http://localhost:8000; do
                        echo "Waiting for container to be ready..."
                        sleep 5
                    done
                    '''
                }
            }
        }

        stage('Install Test Dependencies') {
            steps {
                // Install pytest on the container if it's not already installed
                bat 'docker exec svm pip install pytest'
            }
        }

        stage('Run Tests') {
            steps {
                // Run the tests inside the running Docker container
                bat 'docker exec svm pytest /app/svm_service/test_svm_service.py -v'  // Full path to test inside the container
            }
        }

        stage('Deploy') {
            steps {
                echo 'App deployed'
            }
        }
    }
}
