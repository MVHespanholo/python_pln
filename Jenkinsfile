pipeline {
    agent any
    parameters {
        string(name: 'LIMIAR_DISTANCIA', defaultValue: '3', description: 'Limiar de distância para considerar uma pergunta semelhante')
        string(name: 'PERGUNTAS', defaultValue: 'Quem e voce?', description: 'Perguntas separadas por |')
    }
    environment {
        PATH = "C:\\Windows\\System32;C:\\Users\\Marco\\AppData\\Local\\Programs\\Python\\Python312;C:\\Users\\Marco\\AppData\\Local\\Programs\\Python\\Python312\\Scripts;${env.PATH}"
    }
    stages {
        stage('Preparação do Ambiente') {
            steps {
                bat 'chcp 65001'  // Mudar a codificação do console para UTF-8
                bat 'pip install -r requisitos.txt'
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
                    def perguntas = params.PERGUNTAS.split('\\|').collect { it.trim() }.join(' ')
                    bat "python chat_bot.py ${params.LIMIAR_DISTANCIA} ${perguntas}"
                }
            }
        }
    }
}
