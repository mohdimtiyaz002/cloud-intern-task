pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
        stage('setup') {
      steps {
        
 sh '''
                    python -m venv myenv
                    source myenv/bin/activate  

                    pip install -r requirements.txt
                '''

      }
    }
    stage('hello') {
      steps {
        sh 'python3 test_my_website.py'
      }
    }
  }
}
