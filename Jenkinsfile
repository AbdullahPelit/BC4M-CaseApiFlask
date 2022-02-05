pipeline {
    agent { docker { image 'python3' } } 
//     environment {
//        env.PATH = env.PATH + "C:\Windows\system32"
//    }
    stages {
        stage('test') {
            steps {
                bat 'set +e'
                sh """
                    docker build -t test_bestclouds .
                """


                
            }
        }
        stage("run"){
            steps{
                bat 'set +e'
                sh """
                    docker run -d -p 5000:5000 --name test_bestclouds_container test_bestclouds
                """
            }
        }
        
    }
}
// pipeline {
//   agent any //nerede execute edileceğini söylüyoruz.
//   stages {
//     stage('Build') {
//       parallel {
//         stage('Build') {
//           steps {
//             echo "building the repo"
//           }
//         }
//       }
//     }
  
//     stage('Test') {
//       steps {
//         sh 'python3 app.py'
//         input(id: "Deploy Gate", message: "Deploy ${app.py}?", ok: 'Deploy')
//       }
//     }

//     stage('Deploy')
//     {
//       steps {
//         echo "deploying the application"
//         sh "sudo nohup python3 app.py > log.txt 2>&1 &"
//       }
//     }
//   }
  
  
//     post {
//         always {
//             echo 'The pipeline completed'
//             junit allowEmptyResults: true, testResults:'**/test_reports/*.xml'
//         }
//         success {                   
//             echo "Flask Application Up and running!!"
//         }
//         failure {
//             echo 'Build stage failed'
//             error('Stopping early…')
//         }
//     }
//   }

