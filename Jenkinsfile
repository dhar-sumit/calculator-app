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
                bat 'docker build -t calculator-app .'
            }
        }

        stage('Run Tests in Container') {
            steps {
                // run container and execute tests
                bat 'docker run --rm calculator-app python -m unittest discover -s tests'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            bat 'docker ps -a'
        }
    }
}
