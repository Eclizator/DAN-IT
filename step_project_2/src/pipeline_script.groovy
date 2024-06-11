pipeline {
    agent {
        label "worker"
    }
    
    environment {
        DOCKER_REGISTRY_URL = 'https://registry.hub.docker.com/'
        DOCKER_CREDENTIALS_ID = 'docker_cred'
        DOCKER_IMAGE = 'eclizator/steptwo:latest'
        
        GIT_URL = 'https://github.com/Eclizator/stepProject_2.git'
        GIT_BRANCH = 'main'
        GIT_CRED = 'git_cred'
    }
    
    stages {
        stage('Git pull') {
            steps {
                script {
                    git url: "${GIT_URL}",
                        branch: "${GIT_BRANCH}",
                        credentialsId: "${GIT_CRED}"
                }
            }
        }
        stage('Build and run docker image'){
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}")
                    
                    try { 
                        sh 'docker run ${DOCKER_IMAGE} run test'
                    }
                    catch (Exception e) {
                        echo 'Tests failed'
                        currentBuild.result = 'FAILURE'
                        error('Stopping pipeliune due to Docker Image tests failed!')
                    }
                }
            }
        }
        stage('Login and push docker') {
            steps {
                script {
                    try {
                        docker.withRegistry("${DOCKER_REGISTRY_URL}", "${DOCKER_CREDENTIALS_ID}") {
                            echo 'Logged in Docker Hub'
                            
                            docker.image("${DOCKER_IMAGE}").push()
                            echo 'Docker image pushed'  
                        } 
                    }
                    catch (Exception e) {
                        echo 'Dockerhub errors'
                        currentBuild.result = 'FAILURE'
                        error('Stopping pipeliune due to Docker login failure!')
                    }
                }
            }
        }
    }
}