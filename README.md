# cs643-853-pa2-mb2332

## Docker Repository
https://hub.docker.com/repository/docker/manasbhut/cs643-pa2-aws-spark/general

## Create S3 bucket

1. Go to the **S3 bucket** page in the AWS Console.
2. Create a new bucket named `winemodelbucket`.
3. Upload both datasets into this bucket using the **Add File** option.


## Part-1 Training the ML Model with `TrainingDataset`

### Create an EMR Cluster

1. Go to the **EC2** instance page in AWS.
2. Connect to the **master node**.

### Install Git on EC2 Instance

Run the following command to install `git`:
```
sudo yum install git 
```

### Clone the GitHub Repository

Clone the repository to the EC2 instance 
```
git clone https://github.com/Manas1227/cs643-853-pa2-mb2332
cd cs643-853-pa2-mb2332
```

### Install Required Dependencies

Run the following command to install the necessary dependencies:
```
sudo pip3 install -r requirements.txt
```

### Execute the Training File

Run the `training.py` script to start model training:
```
sudo spark-submit training.py
```
This will create the ML model in the S3 bucket with the name `trainingmodel`.


## Part 2: Using the Created Model to Predict Wine Quality

### Create an EMR Cluster
1. Go to the EC2 instance page in AWS.
2. Connect to the master node.

### Install Git on EC2 Instance
Run the following command to install `git`:
```
sudo yum install git 
```

### Clone the GitHub Repository
Clone the repository to the EC2 instance:
```
git clone https://github.com/Manas1227/cs643-853-pa2-mb2332
cd cs643-853-pa2-mb2332
````

### Check Python and Install Required Versions
Check Python version and install it if necessary:
```
python3 --version
python3.9 -m ensurepip --upgrade
```

### Install Dependencies
Install the required dependencies:
```
pip3 install -r requirements.txt
```

### Install Java on EC2 Instance
Install Java using the following command:
```
sudo yum install java-11-amazon-corretto-devel
```

### Set Path for Java
1. Open the .bashrc file for editing:
```
nano ~/.bashrc
```

2. Add the following two lines at the end of the file (make sure the Java path matches your system’s installation):
```
export JAVA_HOME=/usr/lib/jvm/java-11-amazon-corretto.x86_64
export PATH=$PATH:$JAVA_HOME/bin
```

3. Save and close the file.

### Install Required JAR Files
Download the necessary JAR files:
```
wget https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.1/hadoop-aws-3.3.1.jar -P ~/libs/
wget https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.11.1000/aws-java-sdk-bundle- 1.11.1000.jar -P ~/libs/
```

### Execute the Prediction File
Run the prediction.py script with the necessary JAR files:
```
spark-submit --jars /home/ec2-user/libs/hadoop-aws-3.3.1.jar,/home/ec2-user/libs/aws-java-sdk-bundle-1.11.1000.jar prediction.py
```

## Part-3 Create Docker Image and Push It to Docker Repository

### Build the Docker Image
Build the Docker image:
```
docker build -t aws-spark-training
```

List all Docker images:
```
docker images
```

### Push the Image to Docker Repository
1. Login to Docker:
```
docker login
```

2. Tag the image:
```
docker tag aws-spark-training manasbhut/cs643-pa2-aws-spark:latest
```

3. Push the image to the repository:
```
docker push manasbhut/cs643-pa2-aws-spark:latest
```

## Part-4 Run Docker Image on a New EC2 Instance

### Install and Run Docker on EC2 Instance
1. Install Docker:
```
sudo yum install docker -y
```

2. Start the Docker service:
```
sudo service docker start
```

3. Add the EC2 user to the Docker group:
```
sudo usermod -aG docker ec2-user
```

4. Check if Docker is installed and running. If not, try exiting the terminal and logging in again:
```
docker info
```

### Pull the Latest Docker Image
Pull the image from the Docker repository:
```
docker pull manasbhut/cs643-pa2-aws-spark:latest
```

### Verify the Image
List the Docker images to verify:
```
docker images
```

### Run the Docker Image
Run the image as a container:
```
docker run -d --name spark-container manasbhut/cs643-pa2-aws-spark:latest
```

### Check Running Containers
List all containers:
```
docker ps -a
```

### Check Console Output of Running Container
View logs from the container:
```
docker logs spark-container
```

## vi Editor Commands
- To start inserting code, press `i`.
- To save the file, press `Esc` first, then type `:wq` to save and exit.