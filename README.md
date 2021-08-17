# parakeet
A python script that calculates the time needed to run a specific program (beta)
# Usage
So first of all the script need to calculate what I call a bytetime which is how much time needed to run one byte
that means when you'll run it the first time ,it will calculate it and write a 'bytetime.txt' file , then you'll have to re-run the script.
To run it ,use:
 ```bash
 python3 parakeet.py [program you wanna calculate]
 ```
 you can remove 'bytetime.txt' but the script we'll have to re-calculate it , and it's recommended to remove it from time to time
 # Notices
 * Parakeet gives more floating points than linux 'time' utility
 * If the program you wanna calculate time for has some user interaction ,the parakeet won't add that
 * If the program isn't an executable parakeet won't be accurate at all
 * If the program sleeps , parakeet won't add that (not tested)
 * You can change the source code to get nanoseconds accuracy instead of miliseconds
 # Contact
 contact : unknown989@protonmail.com
