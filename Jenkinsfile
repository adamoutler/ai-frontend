pipeline {
    agent {
        node { label 'shark-wrangler' } 
    }

    environment {
        // Setting environment variables from Jenkins credentials and other values
        APIKEY = credentials('ai-hacked-your-info-key')
        BOTID = 'granite3-dense:2b'
        COMPLETIONSURL = 'https://ai.hackedyour.info/api/chat/completions'
        SYSTEMPROMPT = 'You are a helpful bot'
    }

    stages {
        stage('Checkout') {
            steps {
                // Check out the code from the repository
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Building the Docker image for the AI Frontend
                    sh 'docker build -t ai-frontend:latest .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Running the Docker container with environment variables
                    sh 'docker rmi $(docker image --filter=reference="*_ai-frontend_main" -q) || true'
                    sh 'docker-compose down --remove-orphans'
                    sh 'docker-compose -f docker-compose.yaml up -d --force-recreate'

                }
            }
        }
    }
}
