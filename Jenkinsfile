pipeline {
  agent any
  stages {
    stage("Environment setup and test execution") {
      steps {
        withPythonEnv('python') {
          sh 'pip install -r requirements.txt'
          sh 'pytest ./tests/main.py'
        }
      }
    
    }
  
  }
}
