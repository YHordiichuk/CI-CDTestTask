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
                        sh 'git checkout main'
                        sh 'git merge origin/${RELEASE_NUMBER}'	
                        sh 'git pull origin dev'
                        sh 'git push https://${creds}@github.com/YGordiychuk/CI-CDTestTask'
					
				}
			}
		}
}
