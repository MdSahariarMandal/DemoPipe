pipeline {
agent any
stages {
     stage('Hello') {
        steps {
        checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/MdSahariarMandal/DemoPipe.git']])
    }
     stage("Build") {
        steps {
          bat 'python app.py'  // Adjust the path as needed
    }
}
     stage("Test"){
        steps{
            echo "The job is tested"
        }
    }
}
}
