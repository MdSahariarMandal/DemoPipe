// pipeline {
// agent any
// tools{
// maven 'MAVEN3'
// }
// stages {
//      stage('Hello') {
//         steps {
//         checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/MdSahariarMandal/DemoPipe.git']])
//     }
//      stage("Build") {
//         steps {
//           bat 'python app.py'
//     }
// }
//      stage("Test"){
//         steps{
//             echo "The job is tested"
//         }
//     }
// }
// }

pipeline {
    agent any
    
    parameters {
        string(name: 'IMAGE_NAMES', defaultValue: '', description: 'Comma-separated image names')
    }

    stages {   
        stage('Hello') {
         steps {checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/MdSahariarMandal/DemoPipe.git']])
    }}
        stage('Generate YAMLs') {
            steps {
                script {
                    // Get the IMAGE_NAMES parameter passed from Python script
                    def selectedImageNames = params.IMAGE_NAMES.split(',')
                    
                    // Read the template content from YamlJenkins.yml file
                    def templateContent = readFile('YamlJenkins.yml')
                    
                    // Generate YAML files for each selected image name
                    selectedImageNames.each { imageName ->
                        def modifiedContent = templateContent.replaceAll('\\$\\(image_name\\)', imageName.trim())
                        def fileName = "ModifiedTemplate_${imageName.trim()}.yaml"
                        writeFile file: fileName, text: modifiedContent
                        echo "Modified YAML file created with image name: ${imageName.trim()} - File: ${fileName}"
                    }
                }
            }
        }
    }
}

