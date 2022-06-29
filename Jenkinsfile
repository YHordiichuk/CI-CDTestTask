pipeline {
    agent any
  
    stages {
    
        stage("build") {
        
            steps {
                echo 'building the sql scipts'
            }
        }
        
        stage("test") {
        
            steps {
                echo 'testing db with new scripts'
            }
        }
         
        stage("deploy") {
        
            steps {
              echo 'deploying scipts'
            }
        }
    }
}
