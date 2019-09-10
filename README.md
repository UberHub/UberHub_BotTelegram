# [UberHubBot Telegram](http://telegram.me/UberHub_bot) 

![](https://github.com/UberHub/UberHub_BotTelegram/blob/master/assets/UberHub.jpg?raw=true)

## Sobre

Este é o projeto aberto do Bot no [Telegram](http://telegram.org/) para a comunidade o Ecossistema de Inovação de Uberlândia/MG

[Try it!](http://telegram.me/Uberhub_bot)

## Requisitos

1. Python 3
2. Node.js v6.5.0 ou superior
3. Conta na AWS com acesso administrativo
4. Conta no Google Cloud com acesso administrativo
5. Conta no Telegram 

## Deploying

1. Clone o repositório
2. Instale o serverless framework

```js
npm install -g serverless
```

3. Gere as Keys do serviço na AWS  e configure em seu computador. Mais informações [aqui](https://serverless.com/framework/docs/providers/aws/guide/credentials#using-aws-access-keys).
4. Gere as Keys no Google Cloud para uso da API Sheets e Calendar por [aqui](https://console.developers.google.com/apis/enabled). 
5. Crie o seu Bot do Telegram, guarde o Token. Mais informações [aqui](https://core.telegram.org/bots#3-how-do-i-create-a-bot).
6. Edite o arquivo serverless.yml substituindo as variáveis:

```markdown
environment:
    TELEGRAM_TOKEN: Token do Bot Telegram
    GOOGLE_API_KEY: Api Key do Google
```

7. Faça o deploy na AWS com o comando: (A partir da pasta *uberhub-telegram-bot*)

```
serverless deploy
```

8. Copie o endpoint gerado (Exemplo: https://endpoint-xpto.execute-api.us-west-2.amazonaws.com/prod/message) 
9. Vincule o bot ao endpoint gerado com o POST: (Substitua o Token do bot  e o Endpoint ) 

```curl
curl --request POST --url [https://api.telegram.org/bot](https://api.telegram.org/botTOKENDOBOT/setWebhook)`459903168:APHruyw7ZFj5qOJmJGeYEmfFJxil-z5uLS8`[/setWebhook](https://api.telegram.org/botTOKENDOBOT/setWebhook) --header 'content-type: application/json' --data '{"url": "https://endpoint-xpto.execute-api.us-west-2.amazonaws.com/prod/message"}'
```

Caso o vinculo do endpoint com o bot esteja correto o retorno será:

```json
{
  "ok": true,
  "result": true,
  "description": "Webhook was set"
}
```

## Como Contribuir?

1. 🍴 Faça um Fork neste repo 
2. 🔨 Faça suas contribuições
3. 👥 Adicione seu nome e seu perfil nos créditos
4. 🔧 Faça um pull request [aqui](https://github.com/UberHub/UberHub_BotTelegram/compare)
5. 🎉 Analisamos as contribuições e aprovamos! Sucesso!

Ou se quiser [crie issues](https://github.com/UberHub/UberHub_BotTelegram/issues/new) para melhorarmos os projetos!! 😊

## Contribuidores

- [CrudTec](https://github.com/crudtec)
- [Wladimir Neto](https://github.com/orgs/crudtec/people/wladneto)

