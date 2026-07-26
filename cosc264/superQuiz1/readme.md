# Superquiz 1: Packet processing with Python

## Brief:
    This quiz focuses on how to manipulate bytearrays through manipulating bits.
    Before you start you may need to brush up on Bitwise Operator's [here](https://www.w3schools.com/python/python_operators_bitwise.asp)

## Code Required:
- Basic Operator's (if, else, for, while etc.)
- 'raise' -> used for error's e.g if i != j: raise ValueError("i does not equal j")
- Create a list that can store tuple's e.g ls = [(1, 2, 3), (1,3,2)...]
- List Slicing e.g ls[location]


# IPv4 Header Composition Breakdown

### 1. Validate Version & Field Bit Limits

* If version does not equal 4, raise ValueError
* Create a list of tuple's for each key value ('name', value, max_bits)
* Run through each parameter checking the value is greater than zero but less than 1 << max_bits

### 2. Create The Header

* Create a bytearray. It's length is determined by hdrlen. (hdrlen is measured in bits so * 4)


### 3. Move Stuff

* this is a pain


### 4. Return the Header



## Question 6:


### 1. Paste both your 'compose_header' & 'checksum' functions above
* Make sure in 'compose_header' that your bytearray's length is equal to your **total** header length.


### 2. Calculate Total Packet Length

* Total length is equal to **total** header length + packet length


### 3. Build the Header

* Set header equal to compose_header() filled in with all relevant information. (Version = 4 & checksum = 0)
* Set 'headerchecksum' from the generated version (checksum(header))
* Set header indices **10** and **11** to 'headerchecksum' using bitwise operations

### 4. Return Finished Header Plus Payload
