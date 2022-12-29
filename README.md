# easyiter
Version 1.0  
Easy way to split and join data using custom chunks


## Table Of Contents
no

## Getting Started (example)
```python
import easyiter as e
e.info_packet = True #Makes the first item in sequece the number of chunks, Useful for sending data over sockets.
e.packet_size = 1 #Specifies how large each chunk should be
result = e.create_from_string("Hello world") # Create chunk
print(result) #See what it looks like
print(e.join_from_string(result)) #See it joined
```
## Functions
### create_from_string(data): 
Creates and returns a packet from a string  
data must be a string, or have the `__str__` attribute that must return a string

### create_from_bytes(data): 
Creates and returns a packet from a bytes  
data must be bytes

### join_from_string(data,info_packet=False): 
Creates and returns a packet from a string
data must be string  
When info_packet is `True` it ignores the first packet (which contains the total amount of blocks)  
returns string

### join_from_bytes(data,info_packet=False): 
Creates and returns a packet from a bytes
data must be bytes  
When info_packet is `True` it ignores the first packet (which contains the total amount of blocks)  
returns bytes

---
## Variables
`info_packet` (bool):  
When set:`True` Makes the first item in sequece the number of chunks, Useful for sending data over sockets.  

`packet_size` (bool):  
When set:`True` Makes the first item in sequece the number of chunks, Useful for sending data over sockets.