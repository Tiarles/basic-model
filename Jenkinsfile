pipeline {
    agent any

    stages {
        stage('Download') {
            steps {
                echo "Hi"
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'allure-html/', onlyIfSuccessful: true
            archiveArtifacts artifacts: 'report/', onlyIfSuccessful: true
            archiveArtifacts artifacts: 'open_report.cmd', onlyIfSuccessful: true
        }
    }
}