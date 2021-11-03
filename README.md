# ra-algo

This program implements Ricart-Agrawala Algorithm for Distributed Mutual Exclusion.
Assignment is done in Python Programming langauge.

Preffered Operating System for running the proram : Linux running on 64 bit Processor
Minimum CPU needed : 2
Minimum RAM needed : 4GB

Python Version needed for running the program : 2.7.18

It consists of 2 files.
1. process.py
2. ricartagrawala.py

This program can be run on the single computer or multiple computers.

How to Run the Program ?
Following are the Options available when -h is passed as argument to the program.
 --firstprocess_addr FIRSTPROCESS_ADDR, -r FIRSTPROCESS_ADDR
                        firstprocess address
  --firstprocess_port FIRSTPROCESS_PORT, -i FIRSTPROCESS_PORT
                        firstprocess port
  --cs_time CS_TIME, -u CS_TIME
                        critical section time [ unit - seconds ]
  --wait_time WAIT_TIME, -w WAIT_TIME
                        Idle time
  --name NAME, -n NAME  Unique Node Name
  --addr ADDR, -a ADDR  node address
  --port PORT, -p PORT  node port

Explaination of the the arguments.
* firstprocess_addr is the ip address of the first process which will be used ny other processes to connect to. by default is 127.0.0.1
* firstprocess_port is the port number of the first process which will be used ny other processes to connect to. by default is 0.
* cs_time is the time to be spent by a given process in Critical Section. Unit is seconds.
* wait_time is the idle time or wait time before a process makes next Critical Section Request. Unit is seconds.
* name is the unique name to be given to process for identification
* addr is the Address to which process to be binded to . default is 127.0.0.1
* port is the Port on which process should listen to. default is 0

Step1: Start he First Process by using below command:
Command will spawn first process with name "proces1" with critical section time of 5 seconds and wait or idle time of 10 seconds and on port 12345

python process.py --name "process1" --cs_time 5 --wait_time 10 -p 12345

Step2 : From the other linux shells start other processes with different names and required Critical section time/ idle times as below.
python process.py --name "process2" --cs_time 5 --wait_time 10 -p 54321 -i 12345 
python process.py --name "process3" --cs_time 15 --wait_time 5 -p 16785 -i 12345
python process.py --name "process4" --cs_time 10 --wait_time 8 -p 54123 -i 12345


Each Process will clearly mention :
1. Current Deffered list of Processes.
2. Current Awaiting Reply list
3. If process if idle mode or Critical section mode
4. If process has come out of the Critical section by releasing resource

