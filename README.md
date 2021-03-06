# ssh-crypto

__ssh-crypto__ is a Python3 program to read ssh debugging and identify who has logged in and what settings were used.  It expects a file name, which is a text file that contains ssh logging output.

When run, it parses a log file.  First, edit /etc/ssh/sshd_config.  Change the logging section as shown below (these are commented out by default).  Note that SSH supports different levels of logging, all the way up to DEBUG3.  The lines we need are all DEBUG1.

> \# Logging  
> SyslogFacility AUTH  
> LogLevel DEBUG1  

Restart the SSH service for the new logging setting to take effect.
> sudo service sshd restart

This program analyzes a text file.  Keep in mind that the crypto fields won't be populated for logins before the loggin change takes effect.  Prepare the file by running:
> journalctl -u ssh > ~/ssh.txt

This pulls all logging for the ssh unit into a text file.  __ssh-crypto__ then reviews the file and outputs a table of logins and crypto used.

## Assumptions recap
* Python3
* Systemd
* Debug1
* Prepped file

## Usage
     pop  pop-os  ~  $  ~/git/ssh-crypto/ssh-crypto.py ~/ssh.txt
    -------------------------------------------------------------------------------------------------------------------
    | # |       User        |       IP       |     Algorithm      |        Host        |            Cipher            |
    -------------------------------------------------------------------------------------------------------------------
    |  0|pop                |192.168.25.2    |undefined           |undefined           |undefined                     |
    |  1|pop                |192.168.25.72   |undefined           |undefined           |undefined                     |
    |  2|pop                |192.168.25.81   |undefined           |undefined           |undefined                     |
    |  3|pop                |192.168.25.81   |undefined           |undefined           |undefined                     |
    |  4|pop                |192.168.25.81   |undefined           |undefined           |undefined                     |
    |  5|pop                |192.168.25.81   |curve25519-sha256   |ecdsa-sha2-nistp256 |chacha20-poly1305@openssh.com |
    |  6|pop                |192.168.25.81   |curve25519-sha256   |ecdsa-sha2-nistp256 |chacha20-poly1305@openssh.com |
    -------------------------------------------------------------------------------------------------------------------

    Read more about this utility on my blog at https://www.nextpertise.net/ssh-crypto/.