# Section C

## C.1
As larger datasets are getting more and more popular we need a processing of the data before we can go into application analyzed data, such processing could include feature extraction or simple calculations needed to be done in parallel. All in all, Map-Reduce offers a "simple" programming model that due to its simplicity requires low range hardware, applicable for scaling solutions and able to work in the concept of move the code to the data instead of moving the data to the code. 

## C.2 
Spark uses master and worker nodes, where the worker nodes will do the computations and send it back to the master for visualization after undergone aggregation. Thus, the print statement will be performed on the worker node.

## C.3
If the RDD that you are trying to collect is larger than the memory available on the single driver machine it won't be able to process this data, thus freeze and the kernel will have to restart. To avoid this you can either take parts of the RDD back or aggregate the data further before you collect(). 

## C.4
Partitions is what builds up the RDDs used inside spark. These RDDs are immutable, meaning that the data they represent is not able to be changed. However, in order to manage the data properly, say that we feel that the computations could be optimized by spreading out the data to more worker nodes, then we can repartition the data. However, this operation will be a copy for the IMMUTABLE partition, onto the new partitions and then the old one will be removed. This is usable to create fault tolerant processes as well as containing data integrity.

## C.5
RDDs are resilient in the way that they assure that the computations that are to be done will be done, even if some computations fail along the way. RDDs are able to achieve this by lineage graphs of computations done on their atomic partitions. Meaning, if one of the partitions fails, the RDD is able to recompute the exact same result because that the process is made deterministic. 

# Section D
__“A colleague has mentioned her Spark application has poor performance, what is your advice?”__

One way to optimize your performance is to see if the actions performed are creating an abnormal amount of stages for a task. When creating a job, spark will try to distribute the job properly over the worker node cluster. Most commonly you see this annotated as "shuffle", which is an transformation performed on RDDs to either join or aggregate the partitions being processed. These processes are very I/O costly, thus either making use that partitions are distributed better(on same or closely placed node) could be crucial for better performance. 

Another thing to consider is the function of caching data. There is a risk that caching causes the nodes to place the cache in a less obtainable/poor performance location, but the gains of caching can be great as well. When one should do this is probably for intermediates of your computations, when you don't want to read in the whole data frame once again every time you want to do a subset analysis. But as said, one need to configure this for their data, sometimes reading in the data set every time is better performing than caching it. 

One could also use the proper usage of Broadcast Variables, which are variables that is saved and kept over nodes in the worker cluster. This is a way to either share information on the data to be processed and instead of sending this message every time for each computation.

Depending on the tasks to be computed there are ways to increase the processing power of each API initiated for a task in spark. The APIs will be done by a driver and executor core, where you can increase the memory capacity for higher computational demands. For instance if your applications will use caching you may want to increase the fraction of storage or if the applications will perform mostly reductions then execution memory could be increased to prevent an exceeded usage of heap space.
