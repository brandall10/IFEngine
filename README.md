Small interactive fiction game && engine I built while going through [Learn Python The Hard Way](http://learnpythonthehardway.org/) some time ago.  

I went a bit beyond the basic exercise and read the first 70 or so pages of [Creating Interactive Fiction With Inform 7](http://www.amazon.com/Creating-Interactive-Fiction-Inform-7/dp/1435455061) for inspiration to make it better.

Basic premise has some shades of similarity to Zork I, which I'll admit I haven't played in twenty years or so (shades I say!).  It does involve a troll who will try to kill you, there is a lamp somewhere which you will need, and it is winnable.

Game Engine Features:
* Easily buildable map, linking rooms together by orientation with the ability to place items and characters.  Reference map.py for an example.
* Basic parser which understands [command], [command->object], and [command->object->source/destination].  Ex. 'look', 'open bag', 'add matches to bag'
* Player object which can carry items, manipulate items, move through the map, interact with other characters (attack so far), have a health that can be depleted, killed... and that's about it.
* Person object which can do much of the same as a player except with a very limited AI (randomly moves and interacts within a confined set of rooms)
* A Room object which can have a description, exits, and contain items and characters
* An Item object, ContainerItem object, and Weapon object


