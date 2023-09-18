pipeline {
    agent any
    tools{
        maven 'MAVEN3'
    }

    stages {
        stage('Build') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/MdSahariarMandal/DemoPipe.git']])
            }
        }
        stage("Build-Docker"){
            steps{
                 script{
                  bat 'docker build -t Hello.py .'
                  bat 'docker run Hello.py'
                }
            }
               
        }
    }
}
