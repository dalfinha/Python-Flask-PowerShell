# Trabalhando com Flask (Python) e PowerShell
Projetos em Python que usam o framework web Flask para retornar comandos executados localmente em um site.

## 💡 1º Comandos básicos (PROJ1)

## Pré requisitos⭐
- Instale o Flask e sempre atualize seu Python caso necessário. Use:

```pip install flask```

- Ao desenvolver o código em Python, no mesmo diretório crie uma pasta chamada "Templates" para armazenar o HTML/CSS que permitirá a visualização na web.
- Particularmente não achei necessário adicionar JavaScript nas páginas. 

## O que o código faz?⭐

Sobe localmente um site com as informações solicitadas. Neste site é possivel obter todos os processos da máquina, o dia de hoje e os arquivos recursivos de um diretório, adicionando o diretório como requisição. 


**Tela inicial:**

![image](https://user-images.githubusercontent.com/72402847/235573304-bfdd8d2f-a70f-4ef0-9715-85531e5c7529.png)

Construi a tela inicial só com HTML e CSS. 


**Navegando na opção "Processos Ativos":**

![image](https://user-images.githubusercontent.com/72402847/235573478-ce82d03d-8098-4ac4-9b59-976e874956af.png)


**Navegando na opção "Data de hoje":**

![image](https://user-images.githubusercontent.com/72402847/235573570-1d8186b4-0234-4110-a23e-b846809c1d73.png)


Agora, a melhor parte. O input de dados com a opção "Visualizar arquivos de um diretório (local)".

**Input do caminho local:**

![image](https://user-images.githubusercontent.com/72402847/235573751-2c4c4e57-7007-4d72-bb09-80e3a3070bbe.png)


**Resposta:**

![image](https://user-images.githubusercontent.com/72402847/235573836-9e5b1774-78f9-4b22-8312-85314a80a3d0.png)

Retornando meus arquivos do diretório de testes e scripts que crio. 


Ah, o que é legal de usar a lib Flask é que consigo acompanhar o status das minhas solicitações direto no terminal que executei o código:

![image](https://user-images.githubusercontent.com/72402847/235573106-648d8c79-5c08-452b-992e-86e2f7b8c81b.png)

Como pode ver, tive um problema com o decod. do HTML e a página \get-date retornou o status 500, o tal do Bad Request (só porque mudei o nome de uma váriavel rs).


Toda esta jornada de teste para adicionar neste ReadMe.md tiveram essas requisições:

![image](https://user-images.githubusercontent.com/72402847/235573958-4f848af5-cbc0-44ec-b5ce-df597f56200c.png)


