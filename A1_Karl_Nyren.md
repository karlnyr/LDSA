#Assignment 1 - Karl Nyrén
In this lab we will go through the basic usage of Hadoop/MapReduce models.

## Task 1

### Task 1.1
In the follwoding answer I ran the following code:

```shell
$ usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/mapreduce/hadoop*examples*.jar wordcount input output
```

Questions:
1. Lets look at the directory in output:
```shell
$ ls /home/ubuntu/output
_SUCCESS  part-r-00000
$ less part-r-00000
"A"      2
"Alpha"  1
"Alpha,"        1
"An"     2
"And"    1
"BOILING"       2
"Batesian"      1
"Beta"   2
"Beta"  1
.
..
...
```

1. The _SUCCESS file is an automatic output from MapReduce runtime, inticating that everything has gone as planned. The part-r-00000 file is containing the counted words inside the input document, probably only seen as separated by white spaces. 
2. __Standalone__ mode is used more for debugging of the process, and is not using HDSF or YARN to create a cluster like environment. __Pseudo-Distributed__ mode is going to act more like an actual cluster environment, initiation a master and slave setup, where the Java process is run on the backend.

### Task 1.2

1. The core-site.xml will tell hadoop where the NameNode is running in the cluster, it is also containging information about the input and output of the Hadoop Core. The file HDFS contains information about how the HDFS daemons are to be run. These daemons are such as the NameNode, secondary NameNode and the DataNodes. It is also here that one can specify replication settings, but if left untouched the default setting is used. 
2. So what are the following:
  
    - NameNode - Manages file system namespace, regulates client's access to files, and in HDFS it executes operations such as naming, closing & opening files and directories. 
    - Secondary NameNode - Specially dedicated node in th HDFS cluster that will take checkpoints of the metadata on the NameNode's file system namespace. These are used to help the NameNode perform its work, but it is not an replacement for the main NameNode. 
    - DataNode -  this is the machinery in HDSF that will store data, and this data store is often replicated amongst multiple hadoop nodes.  
    - JPS -  Java Virtual Machine Process Status Tool, which is a command to check all Hadoop daemons running on the curent machine. 

### Task 1.3

1.  There are two found classes inside WordCount.java; Map and Reduce.
    - Map: the map class has at purpose to mark some value with a key
    - Reduce: will use the keys from the mapper in order to aggregate/reduce the data in some manner. 
2. HDSF - Hadoop Distributet File system - is the horizontal data storage in Hadoop applications. HDSF can be accessed by multiple slave nodes in order to compute and is also distributing its data across multiple DataNodes to optimize storage.

### Task 1.4

Beneath is graph attached:

![alt text](https://github.com/kethuth/LDSA/blob/A1/word_counts.png)
