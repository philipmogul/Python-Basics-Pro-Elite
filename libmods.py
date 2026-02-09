import sys

def main():
    print(f"PYTHON LIBRARY MODULES.")
    print("Example: sys modulde")
    print("Python Version = {}.{}.{}".format(*sys.version_info))
    print(sys.platform)

    import os
    print(os.name)
    #print(os.getenv('PATH'))
    print(os.getcwd())


    import urllib.request
    #page = urllib.request.urlopen('http://domain.com') # Will fetch domain
    #for line in page:
    #    print(str(line, encoding='utf-8'), end ='')
    
    import random
    print(random.randint(1, 200)) # Random number btwn 1 & 200 
    x = list(range(20))
    print(x)
    random.shuffle(x)
    print(x) # Shuffling x 


    import datetime
    now = datetime.datetime.now()
    print(now)
    print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)



if __name__ == "__main__":
    main()