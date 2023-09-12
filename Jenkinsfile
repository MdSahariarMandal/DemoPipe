pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Script') {
            steps {
               script {
                     env.PATH = "${tool name: 'Python', type: 'Tool'}:$env.PATH"
                     sh 'python C:/ProgramData/Jenkins/.jenkins/workspace/Hello.py'
            }
        }
    }
}
