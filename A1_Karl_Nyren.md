#Assignment 1 - Karl Nyrén
In this lab we will go through the basic usage of Hadoop/MapReduce models.

## Part 1

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

We were to extract the number of times a character started a word using the altered version of WordCount java script. The altered version can be found [here](https://github.com/kethuth/LDSA/blob/A1/Scripts/FirstLetterCount.java), and the results from reading in the example text is plotted below in the graph.

![Frequency of word starting characters](https://github.com/kethuth/LDSA/blob/A1/Figures/word_counts.png)

As we can see the Java code is not sensitive to what a definition of a character is, it accepts special characters such as #, [ etc. and only start a new word on blank spaces. 

## Part II

1. I would say that they are semi-structured data in the sense that their meta data is structured - such as date posted, the id etc. - however the texts themselves will be very unstructured. They key part of using RDBMs is to be able to store the items with their unique keys, however if we want to analyse the tweets we cannot get any further than the meta-data in an RDBM before things starts to get very slow. By using key values and MapReduction one could analyse the content as well without slowing down the process to much. 

The task is to extract the number of occurences of the swedish pronouns han, hon, det, den, denna, denne and hen in tweets. We are to only use the unique tweets and normalize the counts of the pronouns by the number of tweets. The mapper and reducer can be found [here](https://github.com/kethuth/LDSA/blob/A1/Scripts) and the result gained from the analysis of the Twitter data supplied to us is plotted below. 

![Frequency of Swedish nouns in subset of tweets](https://github.com/kethuth/LDSA/blob/A1/Figures/noun_frequency.png)

## Part III
```sql
hive> CREATE EXTERNAL TABLE if NOT EXISTS Tweets (
    > text STRING,
    > retweeted_status STRING)
    > ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe' STORED AS TEXTFILE;
hive> LOAD DATA LOCAL INPATH '/home/ubuntu/tweet_data/tweets/files/*' OVERWRITE INTO TABLE Tweets;
hive> select noun, count(noun)
hive> select count(*) from Tweets where retweeted_status IS NULL AND LOWER(text) rlike '\\bhon\\b'; # select texts with hon
# The same query was repeated for all pronouns, then normalized using
hive> select count(*) from Tweets where retweeted_status IS NULL; # Count number of unique tweets
```

The number of tweets gained containing the pronouns came out different from the streaming framework. This is most likely due toS that my python code did not stop when it encountered one noun, instead it counts all occurances of the nouns in a tweet, whiclst hive will return when it finds the word once in the text string, thus counting it more properly in my opinion. I know very well that some retweeted_status might contain an original text in the tweet as well 
but I count that every retweet regardless of added text is a non-unique tweet.

 


1. 
