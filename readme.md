iRacePal v0.6
============================================

This tool consists of three different windows.

![Top Window](http://s20.postimg.org/5x433gixp/L79_Start.jpg)

The first is simply a windows that informs you it's looking for iRacing to start.

Nothing really to know about this window, other than if iRacing is already started, you won't see this. Instead, 
depending on the session, it will bring up one of the next windows.

![Practice Window](http://s20.postimg.org/ppm3n5kv1/L79_Fuel.jpg)

This window now has a "Settings" dropdown. If iRacing is already started, you won't see this. Instead, 
depending on the session, it will bring up one of the next windows.

![Settings Window](http://s20.postimg.org/ne9qjmfx9/L79_Settings.jpg)

The Settings window. This is were you can tell the program to automatically create a track folder inside the folder for 
the car you are testing. Also allows you to set the rate at which the program updates. Min = 25ms, Max = 1000ms. 

Next two are the race fuel boxes. As you run laps and accumulate average fuel usage, you can set this box to show
how much fuel you'll need for a race. Simply input the laps, either with the arrows or just putting the cursor in 
the box and type and you'll see the fuel needed.

Also up there you'll see session time left (if applicable) and the current local time.

The next row is pretty self explanatory. 

One thing to know about fuel, it shows whatever you have set in the garage setting for liters or gallons. 
Also, all laps for whatever car and track combo you are running are saved in a .txt file in a folder named /data 
in whatever directory you installed the program to. This allows for a pretty accurate accounting of average fuel for
that car/track over time. It also never stores the first lap from the pits or any other lap that's not within 10% 
of your fuel average. This is to prevent skewing of the average by laps that have a crash, a pit stop, etc. After 
doing some testing, 10% seemed like a good number, and even lower would probably be better. 

The bottom row: Total laps is total laps done in the session, and Laps in Stint are how many laps since pit/reset. 
The various status between them just shows where the driver is. I had them originally for testing the program and 
left it in as it does still have some use now and then. 

![Race Window](http://i.imgur.com/DjtYQRd.jpg)

Finally, the Race Window.

This is broken into three different sections. First is the positional chart, which shows you in relation to the
drivers around you. In addition to showing their most recent lap times and the difference to yours, it will color
the driver names depending on that difference. Red if they are faster than you, Green if you are faster than them. 
This allows you to see who around you is faster, with only a quick glance. 

Second is the weather section. Like the weather in the practice window, this will show you weather info and changes
with any changes during the race. Dynamic weather can sometimes change quite a bit during a session, so this can 
be useful if you follow that sort of thing. 

And third is the race fuel information window. This can be extremely useful in races which require a pit stop. And
even when in a race that doesn't, there's still good info for a driver here. This section will use any practice data 
gathered to calculate average fuel used for information displayed here. Also to note, during a race, the program will 
begin to use the most recent fuel to average fuel. This is setup to 3 laps for a road course, and 5 laps for an
oval. It starts off using any fuel data you might have accumulated earlier in practices, and then will begin using
the 3/5 lap race averages after those laps are complete. It discards fuel used during laps run under caution, and resets
when you make a pit stop. 

Fuel to Finish: This shows how much fuel is needed to finish the race. It's based on your avg fuel use and laps
remaining. 
Laps Until Empty: This takes your avg fuel calculation and shows you how many laps you have until you run out of fuel. 
This of course changes if you have caution laps, etc. It's background will change based on if you can finish the race
with the current amount of fuel in your tank. Red if you don't have enough, Green if you do. 
Lap Remain: Simply how many laps remain in the race. 
Fuel in Car: How much fuel you have in the car. 
Fuel to Add: This shows you how much fuel you need to add to finish the race. It'll show 0 if you can finish, and
it will show the total capacity of your fuel tank if the fuel needed is more than 1 tank of fuel.
Laps Since Pit: How many laps it's been since you pitted last. 


Bugs, issues, etc
==========================================================================
Right now, the program is pretty stable. 
If you do get a crash, check the installation folder for a file, "error.txt". This will record errors and write 
them in there if the program can. Then contact me and send me the file (or just cut/paste the contents I guess). 

What's planned for later?
===========================================================================
I've got other ideas. I might implement something that shows you when the drivers around you last pitted. I could
easily expand the number of drivers shown. For now, this doesn't show classes, just pure positions, but that's something
which might be added later. It also won't work in a spectator session, nor if you ghost race that session.

Updates
===========================================================================
v0.5a - Adds option to have the program auto create a track folder inside the car's setup folder. Only does so if it doesn't 
exist. This is done with the settings option in the first window which asks the user to select their iracing's setup 
folder.

v0.5b - Added code that remembers the window's last position and then will open it next time in that position. Also
added code that improves the way settings are stored and retrieved, along with using a settings.ini file instead.

v0.5c - Fixed bug with creating setups folder

v0.5d - Added better code for handling yellows/pits/race over. Decreased updating from 16ms to 250ms. Will add this
as an option in the future. But 4 times a second should be enough during a race.

v0.5e - Fixed bug with program hanging when looking for iRacing. 

v0.6 - Added water temps to Practice and Race screens. Added Air temperature to Practice and Race. Added an option to
set how often the program updates during the race, found in settings. Defaults to 250ms (4 times a second). 