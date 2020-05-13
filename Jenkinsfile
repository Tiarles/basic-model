pipeline {
    agent any

    stages {
        stage('Download') {
            steps {
                sh 'echo "artifact file" > generatedFile.txt'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'generatedFile.txt', onlyIfSuccessful: true
        }
    }
}