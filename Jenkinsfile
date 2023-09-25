pipeline {
agent any
tools{
    maven 'MAVEN3'
}

stages {
     stage('Hello') {
        steps {
          checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/MdSahariarMandal/DemoPipe.git']])
        }
    }
     stage("Build") {
        steps {
          git branch: 'main', url: 'https://github.com/MdSahariarMandal/DemoPipe.git'
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
