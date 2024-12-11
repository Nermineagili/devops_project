pipeline {
    agent any
    
    stages {
        stage('Checkout GitHub') {
            steps {
                // Explicitly checkout a repository from a URL
                git url: 'https://github.com/Nermineagili/devops_project.git', branch: 'master'
            }
        }

        stage('Build Docker Images') {
            steps {
                // Build Docker images for both the frontend and svm services
                bat 'cd app/svm_service && docker build -t svm .'
                bat 'cd app/Frontend && docker build -t frontend .'
            }
        }

 stage('Start Services with Docker Compose') {
            steps {
                // Use Docker Compose to bring up the services (frontend and svm)
                bat 'docker-compose up -d' // Ensure your docker-compose.yml is properly configured
                // Wait for containers to be ready
                
            }
        }

        stage('Run Tests') {
            steps {
                // Run the backend service tests using pytest in the svm container
                bat 'docker exec devops-svm_service-1 pytest test_svm_service.py -v'



                // Run the Jest tests for the frontend, now targeting the correct tests directory
                //bat 'cd app/tests && npm install && npx jest' // Ensure you're in the tests directory for the frontend
            }
        }

        stage('Deploy') {
            steps {
                echo 'App deployed'
            }
        }

        stage('Stop Services') {
            steps {
                // Use Docker Compose to stop and remove the containers after the tests are done
                bat 'docker-compose -f docker-compose.yml down'
            }
        }
    }
}









































































// pipeline {
//     agent any
//     stages {
//         stage('Checkout GitHub') {
//             steps {
//                 // Explicitly checkout a repository from a URL
//                 git url: 'https://github.com/Nermineagili/devops_project.git', branch: 'master'
//             }
//         }

//         stage('Build Images') {
//             steps {
//                 // Change to the directory where the Dockerfile is located and build the image
//                 bat 'cd app/svm_service && docker build -t svm .'
//             }
//         }

//         stage('Run Image') {
//             steps {
//                 // Stop and remove the existing container if it exists
//                 bat 'docker rm -f svm || echo "No existing container to remove"'

//                 // Run the container in detached mode with the name 'svm'
//                 bat 'docker run -d -p 8002:8000 --name svm svm'
//             }
//         }

//         stage('Run Tests') {
//     steps {
//         // Run the tests inside the running Docker container
//         bat 'docker exec svm pytest /app/tests/test_svm_service.py -v'
//     }
// }


//         stage('Deploy') {
//             steps {
//                 echo 'App deployed'
//             }
//         }
//     }
// }
