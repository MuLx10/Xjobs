sudo python3 -m compileall jobs.py
sudo mv __pycache__/jobs.cpython-35.pyc /usr/bin/Xjobs
sudo chmod 777 /usr/bin/Xjobs
sudo rm -rf __pycache__