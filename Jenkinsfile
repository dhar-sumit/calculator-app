pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/dhar-sumit/demo-repo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("calculator-app")
                }
            }
        }

        stage('Run Tests in Container') {
            steps {
                script {
                    docker.image("calculator-app").inside {
                        sh 'python -m unittest discover -v'
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh 'docker system prune -f'
        }
    }
}
