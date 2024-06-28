pipeline {
    agent any
    parameters {
        string(name: 'LIMIAR_DISTANCIA', defaultValue: '3', description: 'Limiar de distância para considerar uma pergunta semelhante')
        string(name: 'PERGUNTAS', defaultValue: 'Quem e voce?|qual o planeta mais quente do sistema solar?', description: 'Perguntas separadas por |')
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
                    def perguntas = params.PERGUNTAS.split('\\|').collect { it.trim() }
                    perguntas.each { pergunta ->
                        bat "python chat_bot.py ${params.LIMIAR_DISTANCIA} \"${pergunta}\""
                    }
                }
            }
        }
    }
    post {
        always {
            script {
                def buildStatus = currentBuild.currentResult
                emailext (
                    subject: "${env.JOB_NAME} - Build #${env.BUILD_NUMBER} - ${buildStatus}",
                    body: """
                        <p>Build Status: ${buildStatus}</p>
                        <p>Job: ${env.JOB_NAME}</p>
                        <p>Build Number: ${env.BUILD_NUMBER}</p>
                        <p>Build URL: ${env.BUILD_URL}</p>
                    """,
                    recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']],
                    to: 'marcos.viniciushespanholo@gamil.com' // Substitua pelo email desejado
                )
            }
        }
    }
}
