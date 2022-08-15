pipeline {
  agent any
  stages {
    stage("Deploying and testing from release branch") {
      steps {
        withPythonEnv('python') {
          sh 'pip install -r requirements.txt'
          sh 'python ./apply_scripts.py'
          sh 'pytest ./tests/main.py'
        }
      }
    }
    
    stage ('Merging release and develop'){
			steps{
            withCredentials([sshUserPrivateKey(credentialsId: 'f82a0f39-31af-4bb8-9da5-fe26429fb5b5', keyFileVariable: 'SSH_KEY')]) {
                sh 'git checkout dev'
                sh 'git pull'
                sh 'git merge origin/main'
                sh 'GIT_SSH_COMMAND="ssh -i $SSH_KEY" git push git@github.com:YGordiychuk/CI-CDTestTask.git'
            }
        }
	}
	}
}


