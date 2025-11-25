pipeline {
  agent any
  environment {
    DEPLOY_SERVER = "ubuntu@13.220.92.71" // or use ssh in credentials/sshagent
  }
  stages {
    stage('Checkout') {
      steps {
        // checkout using the repository's Jenkins credentials (credentialId must match)
        git branch: 'main',
            url: 'https://github.com/NarasimhaKini/DJ_travel_app.git',
            credentialsId: 'git-ssh-key'
      }
    }
    stage('Build & Push') {
      steps {
        sh 'echo "build/test steps here"'
      }
    }
    stage('Deploy') {
      steps {
        // Use the ssh-agent plugin with a separate Jenkins SSH credential (for EC2 deploy user)
        sshagent (credentials: ['git-ssh-key']) {
          sh "ssh -o StrictHostKeyChecking=no ubuntu@13.220.92.71 'cd /home/ubuntu/DJ_travel_app && docker-compose pull && docker-compose up -d --remove-orphans'"
        }
      }
    }
  }
}
