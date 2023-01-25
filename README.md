# KAIMYON暫定環境構築

## 前提
- Docker, node, docker-composeがインストールされていること

## 実行

```
# 適当な場所にcloneしてくる
git clone https://github.com/Suginoki/KAIMYON.git

# かいみょんの中に移動
cd KAIMYON

# イメージをビルドしてくる
docker-compose build

# コンテナを起動
docker-compose up -d

# データベースのマイグレーション
docker exec -it backend bash
python manage.py migrate
python manage.py createsuperuser
# 適当なrootユーザーを作ってパスワードを設定する
```

[http://localhost:8000/admin]() ←ログイン画面が出てくるはず<br>
[http://localhost:3000]() ←React画面が出てくるはず
