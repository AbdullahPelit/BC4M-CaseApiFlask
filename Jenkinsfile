pipeline {
    agent { dockerfile true } //dockerfile true yapmamızın sebebi docker hubdan çekmek yerine dockerfiledan yeni bir konteynır oluşturması
    stages {
        stage('test') {
            steps {
                sh """
                    docket build -t test_bestcloud .
                """


                
            }
        }
        stage("run"){
            steps{
                sh """
                    docker run -rm test_bestcloud
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

