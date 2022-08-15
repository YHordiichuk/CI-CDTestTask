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
                        sh 'git checkout main'
                        sh 'git add .'	
                        sh "git commit -m 'Merging last release'"
                        sh 'git remote'
			sh 'git push origin'		
				}
			}
		}
}
