## backend
```
apt install python3.12-venv
python3 -m venv .venv
source .venv/bin/activate
cd backend/
pip install -r requirements.txt
nohup python3 manage.py runserver 0.0.0.0:8000 &
```
## frontend
```
cd ../frontend/
apt install npm
npm install -g @vue/cli
nohup npm run serve -- --host 0.0.0.0 --port 8080 &
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```
