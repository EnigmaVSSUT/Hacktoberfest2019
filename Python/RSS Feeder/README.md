# RSSFeeder
This is an RSS feeder that broadcasts an RSS feed if some kind of Linux terminal task fails. You can use it for Android ROM compilation, kernel compilation, or any other task that can be either successful or a failure in the Linux terminal.<br><br>
To use the RSS feeder, <b>modify the variables' values in lines 10,25, and 28 to be your RSS server’s URL</b>. Then, add “|| . feeder” to the end of the respective command, leaving a space.<br><b>For example, if you have to use the RSS feeder for an Android ROM compilation, you have to type the command “make -j32 || . feeder” where “make -j32” is used to compile the ROM. Apart from that, you’ll need to make sure that the files are in the same directory as the current directory of the terminal executing the job.</b><br><br>
Additionally, while this broadcasts an RSS feed, it also stores every job’s status in the “jobstatus” text file.<br><br>
Personally, I use this to check whether an Android ROM build fails. If it does, the script broadcasts an RSS feed which, when combined with a simple applet in IFTTT, notifies me on my phone that the build failed.

