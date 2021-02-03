# aws-lesson

### clone this repo
```
git clone https://github.com/mrivantan/aws-lesson.git
```



```
sudo apt update
sudo apt install python3-pip git tmux
```


```
git clone https://github.com/mrivantan/aws-lesson.git
cd aws-lesson
```

```
pip3 install virtualenv
python3 -m virtualenv -p python3 env
source env/bin/activate
```

```
pip install -r requirements.txt
```

```
tmux new -s app_session
```

```
cd deployment
export FLASK_ENV=development
export FLASK_APP=app.py
flask run --host=0.0.0.0
```