pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                git 'https://github.com/KanG98/python-email-service.git'
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}