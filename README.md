#Assignment 2 scripts: retrive-metadata-json

What it does?
Query the metadata of an ec2 instance within AWS and provide a json formatted output.
Retrieve the value of a particular data key.

How to run ?
Open the src folder
cd retrive-metadata-json/src

Run below scripts to fetch instance metadata and to retrive perticular key. 

python3 get_metadata.py  
python3 get_key.py

-------------------------------------------------

#Assignment 3 script: query-json-object  

What it does? 
it returns value from nested json object for perticular key.
sample json object used in script: 
JSON = {"a":{"b":{"c":"d"}},"x":{"y":{"z":"a"}}}

How to run ?

$ cd query-json-object

$ python3 reduce.py

Enter your key: x/y/z

value:  a

$ python3 reduce.py 

Enter your key: a/b/c

value:  d
 



