//Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any 
    stages {
        stage('Build') {
            steps {
                // git url: 'https://github.com/thisfeather/wiley-C279.git', branch: 'main'
                echo "\n\n### This is a Build stage designed by Group 2:\n"
		echo "building the application...\n"
                echo "\n\nThis is the outcome of running the 1st Python script, inventoryClass.py:\n"
                sh 'python3 ./pythonJobsJenkins/inventoryClass.py'
                echo "\n\nThis is the outcome of running the 2nd Python script, animalClass.py:\n"
                sh 'python3 ./pythonJobsJenkins/animalClass.py'
                echo "\n\nEnd of Python scripts\n"
            }
        }
        
        stage('Test'){
            steps {
                echo "\n\n### This is a Test stage designed by Group 2.\n"
		echo "testing the application...\n"
            }
        }
        
        stage('Deploy'){
            steps {
                echo "\n\n### This is a Deploy stage designed by Group 2.\n"
		echo "deploying the application...\n"
            }
        }
    }
}
