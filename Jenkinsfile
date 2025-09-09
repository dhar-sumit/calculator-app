pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/dhar-sumit/calculator-app.git'
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

        stage('Build Python Package') {
            steps {
                // Assuming you have setup.py in your repo
                bat 'docker run --rm -v %CD%:/app -w /app calculator-app python setup.py sdist bdist_wheel'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            bat 'docker ps -a'
        }

        success {
            echo 'CI pipeline finished successfully!'
        }
        
        failure {
            echo 'CI pipeline failed!'
        }
    }
}

