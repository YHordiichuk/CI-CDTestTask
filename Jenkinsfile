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
			steps {
        			sh 'git config --global user.email yura1234gor@gmail.com'
				sh 'git config --global user.name "YGordiychuk"'
			withCredentials([sshUserPrivateKey(credentialsId: '032f3853-cc19-4a2b-971a-4f8dc596157a', keyFileVariable: 'creds1', passphraseVariable: 'hello', usernameVariable: 'creds')]) {
			
					sh 'git checkout dev'
					sh 'git merge origin/main'	
					sh 'git pull origin dev'
					sh 'git push git@github.com:${creds1}YGordiychuk/CI-CDTestTask.git'
					
					}
				}
			}

  }
}
