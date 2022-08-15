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
            withCredentials([sshUserPrivateKey(credentialsId: 'f37d4cca-f21b-4b0e-8e5d-6163ec297273', keyFileVariable: 'SSH_KEY')]) {
                sh 'git checkout develop'
                sh 'git pull'
                sh 'git checkout -b release_${RELEASE_NUMBER} develop'
                sh 'git merge develop'
                sh 'GIT_SSH_COMMAND="ssh -i $SSH_KEY" git push git@github.com:BedinovOleksandr/CI-CD_home_task.git'
            }
        }
	}
	}
}


