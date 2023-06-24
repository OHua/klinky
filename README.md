### local develop
```shell
docker build -t klinky/develop:v1 .
docker run -e DISCORD_BOT_TOKEN=abcd1234 klinky/develop:v1
```

### deploy
steps when you want to deploy on fly.io manually
```shell
curl -L https://fly.io/install.sh | sh
flyctl launch
flyctl tokens create deploy -x 999999h
flyctl deploy
flyctl status
flyctl open
flyctl ips list
```

### reference
- https://fly.io/docs/hands-on/install-flyctl/
- https://fly.io/docs/app-guides/continuous-deployment-with-github-actions/