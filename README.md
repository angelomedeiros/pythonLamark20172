# Projeto Algoritmos e Programação

## Avaliação Terceiro Estágio

Para a execução do projeto serão necessárias apenas duas coisas, ter o python3 instalado e o pip, provavelmente você já terá os dois em sua máquina. Para verificar se eles estão instalados basta digitar no terminal:


```sh
$   python --version
Python 3.6.3
```
 e

 ```sh
$   pip --version
pip 9.0.1
```
Se a o terminal retornar algo semelhante, então sua máquina está apta a executar a aplicação.

**Obs.:** As versões não precisam ser necessariamente as mesmas. Apenas que o python tenha uma versão igual ou superior a 3.

### Antes de rodar a aplicação...

Antes de rodar a aplicação você terá que fazer as instalações dos pacotes via *pip*. Após efetuar as instalações serão realizadas algumas alterações sobre o arquivo */Email/EnviarEmail.py*.

#### Instalando os pacotes

O primeiro passo para a instalção dos pacotes é você estar com o terminal tendo o *workdir* sendo a pasta do projeto, ou seja, abrir um terminal na pasta do projeto. Feito isso você irá digitar o seguinte comando:

```sh
/ProjetoLamark:$   pip install -r requirements.txt
```

#### Alterando arquivo /Email/EnviarEmail.py

As linhas que você deve realizar alterações estão comentadas:

```python
Arquivo: EnviarEmail.py

smtp_server = 'smtp-mail.outlook.com' # Substitua pelo smtp....
smtp_port = 587 # Substitua pela porta do smtp de hospedagem do seu email
acc_addr = 'seu@email.com' # Substitua pelo seu email
acc_pwd = 'suaSenha' # Senha do email

to_addr = 'destinatario@email.com' # Altere o destinatário
subject = 'Assunto' # Altere o assunto
body = 'Conteudo' # Altere o conteúdo
```

## **Avisos:**


* O arquivo que a aplicação ler é o arquivo "convidados.txt", então se você renomear esse arquivo você deve alterar no script também;

* O arquivo que a aplicação lê tem que ter a estrutura semelhante ao do arquivo "convidados.txt".
