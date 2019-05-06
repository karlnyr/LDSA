create vm, small flawor, bionic beaver, add spark-cluster-client to security groups.

Set the ~/.ssh/config host to your new ip

Host 130.238.x.y
  User ubuntu
  IdentityFile ~/.ssh/id_rsa
  LocalForward 8888 localhost:8888
  LocalForward 4040 localhost:4040
  LocalForward 4041 localhost:4041
  LocalForward 4042 localhost:4042
  LocalForward 4043 localhost:4043


```shell
#!/bins/bash
sudo sed -ie 's/nova.clouds.archive.ubuntu.com/se.archive.ubuntu.com/' /etc/apt/sources.list 
sudo apt update
sudo apt-get install -y openjdk-8-jdk
for i in {1..255}; do echo "192.168.1.$i host-192-168-1-$i-ldsa" | sudo tee -a /etc/hosts; done
for i in {1..255}; do echo "192.168.2.$i host-192-168-2-$i-ldsa" | sudo tee -a /etc/hosts; done
sudo hostname host-$(hostname -I | awk '{$1=$1};1' | sed 's/\./-/'g)-ldsa ; hostname
echo "export PYSPARK_PYTHON=python3" >> ~/.bashrc
source ~/.bashrc
sudo apt-get install -y git
sudo apt-get install -y python3-pip
python3 -m pip --version
python3 -m pip install pip
sudo apt install -y jupyter-notebook
python3 -m pip install pyspark --user
python3 -m pip install pandas --user
python3 -m pip install matplotlib --user
jupyter-notebook ~/LDSA/Scripts
```
