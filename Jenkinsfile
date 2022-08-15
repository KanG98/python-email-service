pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'in branch test'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest'
                echo 'llo uuu'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
