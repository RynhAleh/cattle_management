cd backend/
deactivate
source .venv/bin/activate
nohup python manage.py runserver 0.0.0.0:8000 > ../backend.log &
cd ../frontend/
nohup npm run serve -- --host=0.0.0.0 --port=8080 > ../frontend.log &
