pipeline {
    agent any

    stages {

        stage('Clone Repo Check') {
            steps {
                sh 'echo "Repo cloned successfully"'
            }
        }

        stage('Build Backend Image') {
            steps {
                sh '''
                docker build -t backend-app backend
                '''
            }
        }

        stage('Run Backend Containers') {
            steps {
                sh '''
                docker rm -f backend1 backend2 || true

                docker run -d --name backend1 backend-app
                docker run -d --name backend2 backend-app

                sleep 3
                '''
            }
        }

        stage('Run NGINX Load Balancer') {
            steps {
                sh '''
                docker rm -f nginx-lb || true

                docker run -d --name nginx-lb -p 80:80 nginx

                sleep 2

                docker cp nginx/default.conf nginx-lb:/etc/nginx/conf.d/default.conf

                docker exec nginx-lb nginx -s reload
                '''
            }
        }

    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check console logs.'
        }
    }
}
