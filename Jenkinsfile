pipeline {
    agent any

    environment {
        PATH = "C:\\Windowns\\System32;C:\\Users\\Marco\\AppData\\Local\\Programs\\Python\\Python312;C:\\Users\\Marco\\AppData\\Local\\Programs\\Python\\Python312\\Scripts;${env.PATH}"
    }
        stages {
        stage('Preparação do Ambiente') {
            steps {
                echo 'ja instalado'
                //bat 'pip install -r requisitos.txt'
            }
        }

        stage('Execução do Teste Levenshtein') {
            steps {
                bat 'python3 levenshtein_teste.py'
            }
        }

        stage('Verificação do Arquivo de Perguntas') {
            steps {
                script {
                    if (fileExists('perguntas.txt')) {
                        echo 'Arquivo perguntas.txt encontrado!'
                    } else {
                        error('Arquivo perguntas.txt não encontrado. Interrompendo o pipeline.')
                    }
                }
            }
        }

        stage('Execução do Chatbot') {
            steps {
                bat 'python chat_bot.py'
            }
        }
    }
}
