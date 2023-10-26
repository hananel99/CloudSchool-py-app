pipeline {
    agent any
    triggers {
        // Define a webhook trigger for GitHub pushes to your repository.
        githubPush()
    }
    stages {
        stage('Checkout SCM') {
    steps {
        script {
            withCredentials([string(credentialsId: 'GITHUB_APP_INSTALLATION_TOKEN', variable: 'AppCredentials')]) {
                def scmVars = checkout([
                    $class: 'GitSCM',
                    branches: [[name: 'main']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/EliranKasif/CloudSchool-PythonRestApi',
                        credentialsId: '',
                    ]]
                ])
                env.GIT_COMMIT = scmVars.GIT_COMMIT
            }
        }
    }
}

        stage('updatesConsulKey') {
            steps {
                echo "Updating Consul key with new version"
                sh "curl \
                    --request PUT \
                    --data ${env.GIT_COMMIT} \
                    main.services:8500/v1/kv/app/version/APPLICATION_VERSION"
            }
        }
    }
}
