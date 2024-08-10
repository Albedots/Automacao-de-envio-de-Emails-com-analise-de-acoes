# Automação de Envio de E-mails com Análise de Ações

### Este projeto foi criado como parte do curso intensivo de **Python** da **EmpowerData**. O programa realiza a automação do envio de e-mails com dados de ações financeiras. Ele coleta informações sobre uma ação específica em um intervalo de datas definido pelo usuário e envia um e-mail com essas informações usando o Gmail.

## Funcionalidades
- **Coleta de dados**: Obtém dados históricos de ações usando a biblioteca `yfinance`.
- **Análise de Dados**: Calcula e exibe a cotação máxima, mínima e média da ação.
- **Envio de E-mail**: Preenche e envia um E-mail automaticamente com as informações disponibilizadas. 


## Instalação
 - Clone o repositório ou baixe apenas o `main.py`
 - Certifique-se de que você tem o Python instalado em seu sistema e/ou
 Interpretador Python. Este projeto foi testa numa versão 3.x do Python
 - Instale as bibliotecas necessarias usando o `pip`:
```bash
    pip install yfinance pyautogui pyperclip
```

## Limitações
- O script assume uma tela de resolução 1080p e pode precisar de ajustes de coordenadas para outras resoluções.
- O envio do E-mail depende da interface gráfica do Gmail, oque pode mudar com atulizações do site.

## Contribuição
Se você deseja contribuir com o projeto, por favor, faça um fork do repositório e envie um pull request com suas melhorias.

## Uso
Abra o arquivo `arquivo.py` com um interpretador ou IDE e siga as intruções do programa.


## Manutenção
Pretendo consertar as limitações do projeto no futuro.