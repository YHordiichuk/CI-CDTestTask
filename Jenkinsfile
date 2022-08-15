pipeline {
    agent any
    stages  {
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
				git config --global user.email "yura1234gor@gmail.com"
 				git config --global user.name "Yurii Hordiichuk"			
			
					
				withCredentials([gitUsernamePassword(credentialsId: '91ff1c95-9d6b-409f-a5a5-db3029ef8eb0', gitToolName: 'Default')]) {
    			 	
				sh 'git checkout dev'
				sh 'git merge origin/main'
				sh 'git pull origin dev'
				ssh 'git push https://${creds}@github.com/YGordiychuk/CI-CDTestTask'
			}
				
					
					
				}
			}
		}
}
