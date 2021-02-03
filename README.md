# aws-lesson

## About
This is an educational project intended to introduce basic concepts of running flask on aws. It is by no means secure or production grade.

## Instructions

### clone this repo
```
git clone https://github.com/mrivantan/aws-lesson.git
```

### Create a new **blank** repo in your own github account
- no readme
- no .gitignore
- nothing

### Change the origin to your repo
```
git remote set-url origin http://github.com/YOU/YOUR_REPO.git
```

### Create a new EC2 instance
- ubuntu 20.04
- instance type: t2.micro
- security > add the following
    - port range: 5000
    - source: 0.0.0.0/0::/0
- launch the instance

### Connect to shell
- Click the new instance to get to "instance summary" page
- Click "connect" button at the top right
- Click orange "Connect" button
- a new terminal window will appear in your browser

### Install tools
- `python3-pip` is the pip package manager
- `git` lets us clone from our repo
- `tmux` lets us run the flask server in the background
```
sudo apt update
sudo apt install python3-pip git tmux
```

### Clone the repo into your aws instance
change the address to **Your own repo address**
```
git clone https://github.com/mrivantan/aws-lesson.git
```

### Create a virtual environment
```
cd aws-lesson
pip3 install virtualenv
python3 -m virtualenv -p python3 env
source env/bin/activate
```

### Install dependency packages
This will install all packages described in the `requirements.txt` file
```
pip install -r requirements.txt
```

### Create a new session
If we were to run our flask app currently, the app will shutdown when we close the terminal. By creating a tmux session, we can run the flask app even after the terminal is closed.
https://github.com/tmux/tmux/wiki/Getting-Started

https://tmuxcheatsheet.com/
```
tmux new -s app_session
```

### Start the flask app
```
cd deployment
export FLASK_ENV=development
export FLASK_APP=app.py
flask run --host=0.0.0.0
```

### Try your new API
```
http://YOUR_EC2_PUBLIC_URL:5000/api/diabetes?x=0,1,2,3,4,5,6,7,8,9

for example:
http://ec2-18-191-183-22.us-east-2.compute.amazonaws.com:5000/api/diabetes?x=0,1,2,3,4,5,6,7,8,9
```