pipeline {
agent any

stages {
     stage('Hello') {
        steps {
          checkout scmGit(branches: [[name: '*/python']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/MdSahariarMandal/DemoPipe.git']])
        }
    }
     stage("Build") {
        steps {
          git branch: 'python', url: 'https://github.com/MdSahariarMandal/DemoPipe.git'
          bat 'python C:\Users\sahariar.mandal\Desktop\Demo.py'  // Adjust the path as needed
    }
}
     stage("Test"){
        steps{
            echo "The job is tested"
        }
    }
}
}
