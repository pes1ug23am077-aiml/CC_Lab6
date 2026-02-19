pipeline {
    agent any

    stages {

        stage('Build Backend Image') {
            steps {
                sh 'docker build -t backend-app backend'
            }
        }


        stage('Create Network') {
            steps {
                sh '''
                docker network rm labnet || true
                docker network create labnet
                '''
            }
        }


        stage('Run Backend Containers') {
            steps {
                sh '''
                docker rm -f backend1 backend2 || true

                docker run -d --name backend1 --network labnet backend-app
                docker run -d --name backend2 --network labnet backend-app

                sleep 5
                '''
            }
        }


        stage('Run NGINX Load Balancer') {
            steps {
                sh '''
                docker rm -f nginx-lb || true

                docker run -d \
                --name nginx-lb \
                --network labnet \
                -p 80:80 nginx

                sleep 5

                docker cp nginx/default.conf nginx-lb:/etc/nginx/conf.d/default.conf

                docker exec nginx-lb nginx -s reload
                '''
            }
        }

    }

    post {
        success {
            echo "Pipeline deployed successfully"
        }

        failure {
            echo "Pipeline failed"
        }
    }

}
