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