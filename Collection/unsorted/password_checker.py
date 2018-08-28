#loops
import sys
MASTER_PASSWORD = 'opensesame'
password = input("Please input your password: ")
attempt_count = 1
while password != MASTER_PASSWORD:
    if attempt_count > 3:
        sys.exit("too many invalid attempts")
    password = input("invalid password, try again: ")
    attempt_count += 1
print("nei så flink")