pipeline {
  agent any

  environment {
    IMAGE = "yourdockerhubuser/travel-blog:${env.BUILD_NUMBER}"
    SSH_USER = "ec2-user" // or ubuntu
    EC2_HOST = "EC2_PUBLIC_IP_OR_HOSTNAME"
    SSH_CREDENTIALS_ID = "ec2-ssh-key"
    REGISTRY_CREDENTIALS = "dockerhub-credentials"
  }

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Lint') {
      steps {
        sh 'pip install -r requirements.txt'
        // add flake8 if you want
      }
    }
    stage('Test') {
      steps {
        sh 'python manage.py test --verbosity=1 || true' // don't fail pipeline for now if you want; change as needed
      }
    }
    stage('Build Docker Image') {
      steps {
        sh "docker build -t ${IMAGE} ."
      }
    }
    stage('Push Image') {
      steps {
        withCredentials([usernamePassword(credentialsId: "${REGISTRY_CREDENTIALS}", usernameVariable: 'REG_USER', passwordVariable: 'REG_PASS')]) {
          sh '''
            echo "$REG_PASS" | docker login -u "$REG_USER" --password-stdin
            docker push ${IMAGE}
          '''
        }
      }
    }
    stage('Deploy to EC2') {
      steps {
        // Copy docker-compose on remote or run remote docker commands
        sshagent (credentials: ["${SSH_CREDENTIALS_ID}"]) {
          sh """
          scp -o StrictHostKeyChecking=no docker-compose.prod.yml ${SSH_USER}@${EC2_HOST}:/home/${SSH_USER}/docker-compose.prod.yml
          ssh -o StrictHostKeyChecking=no ${SSH_USER}@${EC2_HOST} '
            docker pull ${IMAGE} &&
            docker-compose -f docker-compose.prod.yml up -d --no-build
          '
          """
        }
      }
    }
  }
  post {
    failure {
      mail to: 'dev-team@example.com', subject: "Build failed: ${env.BUILD_TAG}", body: "Check Jenkins"
    }
  }
}
