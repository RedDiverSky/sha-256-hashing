# Project 3: Working with SHA-256
## Task 1
The first goal of this task was to determine, for files of various lengths, how many times the 
files could be hashed within one second using SHA-256 and another hash function, which I chose to
 be MD5. Sample output looked like this:
 
    file0 was hashed 3679 times by SHA-256 in 1 sec
    file0 was hashed 2978 times by MD5 in 1 sec
    file1 was hashed 4942 times by SHA-256 in 1 sec
    file1 was hashed 5082 times by MD5 in 1 sec
    file2 was hashed 4716 times by SHA-256 in 1 sec
    file2 was hashed 4639 times by MD5 in 1 sec
    file3 was hashed 4739 times by SHA-256 in 1 sec
    file3 was hashed 4864 times by MD5 in 1 sec
    file4 was hashed 4662 times by SHA-256 in 1 sec
    file4 was hashed 5058 times by MD5 in 1 sec
    
Generally, the hash functions seemed to have around the same performance.

The second goal of this task was to determine how long it would take to find a collision for a 
particular hash value by brute-forcing both hash algorithms. So far it has been over two hours 
and I still haven't gotten a result for the first algorithm. For context, I am operating on a 
laptop with 4.00 GB of RAM and a 1.70 GHz CPU.

---
## Task 2
The goal of this task was to determine how long it would take to generate a hash whose prefix 
included as much of my birth date as possible. Since my birth date is 11/22/1996, I wanted to 
find a hash value that started with 11221996; however, I wasn't sure how long this would take, so I 
approached the problem by trying to generate a hash value that began with 1, then with 11, and 
so on up to 11221996. These were the times I recorded for each prefix size:
 
- Found first 1 digits in 0.0 sec (1...)
- Found first 2 digits in 0.001001119613647461 sec (11...)
- Found first 3 digits in 0.0009982585906982422 sec (112...)
- Found first 4 digits in 0.25190043449401855 sec (1122...)
- Found first 5 digits in 0.24581646919250488 sec (11221...)
- Found first 6 digits in 70.79688620567322 sec (112219...)
- Found first 7 digits in 70.60717701911926 sec (1122199...)
- Found first 8 digits in 457.21379828453064 sec (11221996...)

It took almost 8 minutes to find a hash that matched my chosen 8-character sequence.

---
## Task 3
The goal of this task was to find the lowest hash value produced from a string in a given amount of
 time--10, 20, and 30 seconds. For each time interval, the minimum value was calculated by 
 averaging the lowest hash value produced in 10 trials. A sample set of the results I obtained was:
 
    The avg lowest hash value produced in 10 sec was 0x154030b3bdde2c0000000000000000000000000000000000000000000000
    The avg lowest hash value produced in 20 sec was 0xbbc9cc7af84488000000000000000000000000000000000000000000000
    The avg lowest hash value produced in 30 sec was 0x66086c9964ec04000000000000000000000000000000000000000000000

The lowest hash value generally decreased for longer intervals as it theoretically should have, but 
it was difficult to determine a trend in the relationship between the lowest hash value and 
the amount of time in which to perform hashes. However, I noticed that the lowest hash value 
decreased by an entire order of magnitude from the 10-second time interval to the 20-second time 
interval. I predict that this decrease would continue as the time interval increased, but that 
the increase would have to be much steeper in order to generate the same amount of change in the 
lowest hash value.