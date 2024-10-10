echo "BACKEND:"
ps aux|grep '[0-9/ ]python manage.py runserver 0.0.0.0:8000'|awk '{print $2}'
echo "FRONTEND:"
ps aux|grep '[0-9/ ]npm run serve --host=0.0.0.0 --port=8080'|awk '{print $2}'
ps aux|grep '[0-9/ ]vue-cli-service serve --host=0.0.0.0 --port=8080'|awk '{print $2}'  
      