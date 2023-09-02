def img
pipeline {
    environment {
                registry = 'pkogolo1/nfldocker'
                dockerImage = ''
    }
    agent any
    stages {
        stage('Checkout') {
                steps {
                git branch: 'main',
                url: 'https://github.com/pkogolo/nfl_headline_news.git'
                }
        }

        stage('Test') {
                steps {
                sh 'cat app.py'
                }
        }

        stage('Clean Up') {
            steps {
                sh returnStatus: true, script: 'docker stop $(docker ps -a | grep ${JOB_NAME} | awk \'{print $1}\')'
                sh returnStatus: true, script: 'docker rmi $(docker images | grep ${registry} | awk \'{print $3}\') --force'
                sh returnStatus: true, script: 'docker rm ${JOB_NAME}'
            }
        }

        stage('Build Image') {
            steps {
                script {
                    img = registry + ":${env.BUILD_ID}"
                    println("${img}")
                    dockerImage = docker.build("${img}")
                }
            }
        }

        stage('Deploy') {
            steps {
                sh label: '', script: "docker run -d --name ${JOB_NAME} -p 9000:9000 ${img}"
            }
        }
    }
}