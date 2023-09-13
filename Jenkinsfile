pipeline {
agent any

stages {
    stage('Hello') {
        steps {
          checkout scmGit(branches: [[name: '*/python']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/MdSahariarMandal/DemoPipe.git']])
        }
    }
    
    stage("Test"){
        steps{
            echo "The job is tested"
        }
    }
}
}
