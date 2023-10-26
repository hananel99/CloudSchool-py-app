pipeline {
    agent any
    triggers {
        // Define a webhook trigger for GitHub pushes to your repository.
        githubPush()
    }
    stages {
        stage('Checkout SCM') {
            steps {
                // Your existing code for checking out the repository.
                // This remains unchanged.
                script {
                    def scmVars = checkout([
                        $class: 'GitSCM',
                        branches: [[name: 'main']],
                        userRemoteConfigs: [[
                            url: 'https://github.com/hananel99/CloudSchool-py-app',
                            credentialsId: '',
                        ]]
                    ])
                    env.GIT_COMMIT = scmVars.GIT_COMMIT
                }
            }
        }
        stage('updatesConsulKey') {
            steps {
                // You can use Git to determine the list of changed files.
                // If 'app.py' is among the changed files, update the Consul key.
                script {
                    def changedFiles = sh(script: 'git diff --name-only HEAD~1', returnStatus: true)
                    if ('app.py' in changedFiles) {
                        echo "Updating Consul key with new version"
                        sh "curl \
                            --request PUT \
                            --data ${env.GIT_COMMIT} \
                            main.services:8500/v1/kv/app/version/APPLICATION_VERSION"
                    } else {
                        echo "No changes to 'app.py', skipping Consul update"
                    }
                }
            }
        }
    }
}
