pipeline {
    agent any
    stages  {
        stage("Environment setup and test execution") {
      steps {
        withPythonEnv('python') {
          sh 'pip install -r requirements.txt'
          
          sh 'python ./apply_scripts.py'
          sh 'pytest ./tests/main.py'
                                }
        
              }
            }
  }
}
