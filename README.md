# cs643-853-pa2-mb2332

## Create S3 bucket
Go to the S3 bucket page on AWS console

Create new bucket with name "winemodelbucket"
Upload both datasets in this bucket with Add File option.

## Part-1 Training ML model with TrainingDataset
Create EMR cluster

go to EC2 instance page

connect with master node

after log in to master node create training program file
```
touch training.py
vi training.py
```
write training program and save the training file

create requirements file to store list of all required libraries 
```
touch requirements.txt
vi requirements.txt
```

install dependencies all together
```
pip install -r requirements.txt
```

now, execute the training file
```
python training.py
```

will create ML model in s3 bucket with "trainingmodel" name

## Part-2 Using created model predict the wine quality
Create EMR cluster

go to EC2 instance page

connect with master node

after log in to master node create prediction program file
```
touch prediction.py
vi prediction.py
```
write prediction program and save the prediction file

create requirements file to store list of all required libraries 
```
touch requirements.txt
vi requirements.txt
```

install dependencies all together
```
pip install -r requirements.txt
```

now, execute the prediction file
```
python prediction.py
```

### vi editor commands
To start inserting code press "i"
To save the file press "Esc" first then ":wq" to save and exit the file