wget http://d3kbcqa49mib13.cloudfront.net/spark-1.6.0-bin-hadoop2.6.tgz
tar xzf spark-1.6.0-bin-hadoop2.6.tgz
rm *.tgz
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-pip python-dev build-essential python3-pip \
python3-dev python-setuptools python3-setuptools python-numpy python-scipy \
python-matplotlib ipython ipython-notebook python-pandas python-sympy \
python-nose python3-numpy python3-scipy python3-matplotlib ipython3 \
ipython3-notebook python3-pandas python3-nose libtiff5-dev libjpeg8-dev \
zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev \
tk8.6-dev python-tk default-jre \
&& sudo pip install -U Pillow scikit-learn \
&& sudo pip3 install -U Pillow scikit-learn
