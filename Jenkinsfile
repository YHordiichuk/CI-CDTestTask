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
			
					sh 'git checkout dev'
					sh 'git merge origin/main'	
					sh 'git pull origin dev'
				
               				 withCredentials([sshUserPrivateKey(credentialsId: '7f5d73bb-48d4-40eb-94df-b57795d8dae5', keyFileVariable: 'creds', passphraseVariable: 'hello', usernameVariable: 'creds')]) {


					sh 'git push git@github.com:YGordiychuk/CI-CDTestTask.git'
					 }
					
				}
			}

  }
}
