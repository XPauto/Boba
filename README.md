# Boba

Boba is a python software which allows users to either create "bubbles" or connect to one.

It is very easy to create a bubble.

Download the zip file of this repository, then extract all.

Simply open the "server.py" file, and change the IP & PORT variables
to "localhost" & set the PORT to a 4 digit number, such as 9999 (the preset value, reccommended).

Now, open up "client.py", & set the IP & PORT variables to the values set before.

Run both of these files at the same time, and check it out!


How to host a bubble online:

Go to https://ngrok.com/download, where you will find a download for the hosting software, (DONT USE CHOCOLATEY).

In your command line, run "ngrok.exe tcp 5001" without the quotation marks.

Once this runs, check the "Forwarding" line to find your IP address, something like: "4.tcp.ngrok.io:4869"
& your port.

Change these values in "server.py" & "client.py" now, and you are all set!

(c) Copyright XPauto

NOTE: ALL DISTRIBUTIONS HAVE TO COME WITH THE LICENSE.

