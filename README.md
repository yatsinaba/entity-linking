# entity-linking
Project of entity linking in contracts

Забрати контейнер з братом

```bash
docker pull cassj/brat
```
Добавити volume щоб не втратити данні
```bash
docker volume create --name brat-data
docker volume create --name brat-cfg
```
Скопіювати данні в brat-data та brat-cfg

Запустити brat
```bash
docker run --name=brat -d -p 80:80 -v $(pwd)/brat-data:/bratdata -v $(pwd)/brat-cfg:/bratcfg -e BRAT_USERNAME=brat -e BRAT_PASSWORD=brat -e BRAT_EMAIL=brat@example.com cassj/brat
```

Підєднатися до контейнеру якщо необхідно
```bash
docker exec -it brat /bin/bash
```
