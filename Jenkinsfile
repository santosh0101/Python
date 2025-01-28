pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                script {
                    sh 'python -m venv venv'
                    sh './venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh './venv/bin/activate && pytest'
                }
            }
        }
        stage('Build') {
            steps {
                echo 'Build step (optional for Python projects)'
            }
        }
    }
}

