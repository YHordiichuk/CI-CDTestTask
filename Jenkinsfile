pipeline {
  agent any
  stages {
    stage("Environment setup and test execution") {
      steps {
        with PythonEnv('python') {
          sh 'pip install -r requirements.txt'
          sh 'pytest ./tests/main.py'
        }
      }
    
    }
  
  }
}
