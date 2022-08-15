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
			git branch: 'main', credentialsId: '91ff1c95-9d6b-409f-a5a5-db3029ef8eb0', url: 'https://github.com/YGordiychuk/CI-CDTestTask'
			
					
			
					
			withCredentials([gitUsernamePassword(credentialsId: '91ff1c95-9d6b-409f-a5a5-db3029ef8eb0', gitToolName: 'Default')]) {
    			 	sh 'git checkout dev'
				sh 'git merge main'
				sh 'git push origin'
			}
				
					
					
				}
			}
		}
}
