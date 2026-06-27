# Atividades

### 1. Sobre os Diretórios

- No Linux, costumamos dizer que "tudo é arquivo de texto" e "tudo é arquivo". Baseado nessa premissa, qual é a diferença fundamental entre o conteúdo armazenado em `/etc` e o conteúdo de `/dev`? Além disso, qual é o papel do diretório `/home`?

#### R:

`/etc` é onde contém arquivos de configuração dos sistema e serviços
`/dev` é onde contém arquivos de hardware
`/home` é onde ficam os arquivos pessoais do usuário

### 2. Sobre AAA

- Defina o conceito de segurança AAA. Para ilustrar, dê um exemplo prático de como a Autenticação (Authentication) e a Autorização (Authorization) se diferenciam durante o acesso de um usuário via SSH.

#### R:

AAA é parte de um framework de segurança que trabalha nos conceitos:
"Quem é você?"
"O que você tem permissão para fazer?"
"O que você fez enquanto esteve aqui?"
Ele prova sua identidade, verifica se você pode interagir com X arquivo e rastreia o que você fez ou tentou fazer.

Um exemplo seria fazer login em um servidor ssh como em nossa aula, nesse passo já estamos sendo identificados como alunos, essa é a parte de autenticação. Após isso, se tentamos usar por exemplo o comando cat para ver a pasta `/etc/shadow`, não teremos permissão porque não somos super usuários, essa é a parte de autorização. E por fim, tudo o que fazemos ou tentamos fazer, foi registrado em um arquivo em `/var/log/auth.log`.

### 3. Sobre o Servidor da Aula

- Como você investigaria se o servidor que estamos acessando utiliza autenticação local, LDAP ou NIS? (Responda qual é o método utilizado na nossa máquina e qual pista/comando o levou a essa conclusão).

#### R:

Usando o comando cat common-password dentro de `/etc/pam.d`, se conter o arquivo `pam.sss.so`, é sinal de que o servidor usa autenticação LDAP ou NIS.

### 4. Sobre o SSH

- Quando um usuário tenta fazer login remoto, o SSH não checa o arquivo `/etc/shadow` diretamente. Qual é o nome do sistema intermediário responsável por receber esse pedido do SSH e decidir como e onde a senha será validada?

#### R:

PAM

### 5. Sobre o SSSD

- Qual é a função do serviço SSSD (System Security Services Daemon) no Linux?

#### R:

Ser um intermediário inteligente entre o sistema operacional local e os provedores de indentidade remotos.
