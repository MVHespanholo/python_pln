pipeline {
    agent any
    parameters {
        string(name: 'LIMIAR_DISTANCIA', defaultValue: '3', description: 'Limiar de distância para considerar uma pergunta semelhante')
        string(name: 'PERGUNTAS', defaultValue: 'Como você está?|Qual é o seu nome?', description: 'Perguntas separadas por |')
    }
    environment {
        PATH = "C:\\Windows\\System32;C:\\Users\\Marco\\AppData\\Local\\Programs\\Python\\Python312;C:\\Users\\Marco\\AppData\\Local\\Programs\\Python\\Python312\\Scripts;${env.PATH}"
    }
    stages {
        stage('Preparação do Ambiente') {
            steps {
                bat 'pip install -r requisitos.txt'
                bat 'pip install python-Levenshtein'
            }
        }
        stage('Execução do Teste Levenshtein') {
            steps {
                bat 'python levenshtein_teste.py'
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
                script {
                    def perguntas = params.PERGUNTAS.split('|').collect { it.trim() }.join(' ')
                    bat "python chat_bot.py ${params.LIMIAR_DISTANCIA} ${perguntas}"
                }
            }
        }
    }
}
