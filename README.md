# Modos de Execução no Docker

Principais modos de execução de containers no Docker. Cada modo pode ser utilizado de acordo com a necessidade do projeto — seja para testes interativos, execução de serviços, ou comandos pontuais.

---

## 📌 1. Modo Interativo (`-it`)

Permite interagir com o container através do terminal, simulando um ambiente shell dentro do container.

```bash
docker run -it ubuntu bash
````

📍 Ideal para:

* Testes manuais
* Depuração de containers
* Exploração de imagens

---

## 📌 2. Modo em Segundo Plano (`-d`)

Executa o container em **background**, liberando o terminal para outras tarefas.

```bash
docker run -d nginx
```

📍 Ideal para:

* Aplicações que rodam como serviço (servidores, bancos de dados)
* Execução contínua sem interação

Você pode visualizar a saída com:

```bash
docker logs <id ou nome>
```

---

## 📌 3. Modo Interativo + Background (`-dit`)

Executa o container em segundo plano, mas mantém o terminal alocado, permitindo reconexão posterior.

```bash
docker run -dit ubuntu
```

Para retomar a interação com o container:

```bash
docker attach <id ou nome>
```

---

## 📌 4. Execução Única e Automática (`--rm`)

Executa um comando rapidamente e remove o container logo após a execução.

```bash
docker run --rm ubuntu echo "Olá, Docker"
```

📍 Ideal para:

* Execução de scripts
* Tarefas pontuais
* Containers temporários

---

## 📌 5. Execução de Comandos em Containers Ativos (`docker exec`)

Permite executar comandos adicionais em um container já em execução.

```bash
docker exec -it <id ou nome> bash
```

📍 Ideal para:

* Acesso ao shell de containers ativos
* Execução de tarefas dentro de aplicações em execução

---

## 📌 6. Retomando Containers com `docker attach`

Permite retomar a interação com um container que está em execução com terminal ativo.

```bash
docker attach <id ou nome>
```

---

## 📋 Tabela Comparativa

| Modo                    | Opções/Comando  | Finalidade Principal                      |
| ----------------------- | --------------- | ----------------------------------------- |
| Interativo              | `-it`           | Terminal interativo dentro do container   |
| Em segundo plano        | `-d`            | Executa como serviço, sem terminal        |
| Interativo + background | `-dit`          | Executa em background, mas com TTY ativo  |
| Execução única          | `--rm`          | Executa e remove o container              |
| Execução em containers  | `docker exec`   | Roda comandos em containers já ativos     |
| Reatachar container     | `docker attach` | Reanexa terminal a containers em execução |

---

## ✅ Exemplo Prático

```bash
# Executar um container Ubuntu com terminal interativo
docker run -it ubuntu bash

# Em outro terminal: listar containers em execução
docker ps

# Executar um comando dentro do container ativo
docker exec -it <container_id> ls /

# Parar o container
docker stop <container_id>
```

---

Fazendo um paralelo com o conceito de orientação a objetos, podemos pensar nas imagens Docker como classes, onde cada container é objeto instanciado.

