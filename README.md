# Lego Carousel with Music for the BBC micro:bit

The Wixams Coding Club uses the [32-in-1 Wonder Building Kit from ElecFreaks](https://www.elecfreaks.com/micro-bit-wonder-building-kit-without-micro-bit-board.html) as a tool for learning programming on the BBC micro:bit. The Lego Carousel project started with the [Rotary Chairs](https://elecfreaks.com/learn-en/microbitKit/Wonder_Building_Kit/Case_05.html) case from ElecFreaks.

![Image of the Rotary Chairs project from ElecFreaks](/assets/ElecFreaks-32-in-1-Case-5-Rotary-Chairs.png)

Once built we found the project was very basic and only had a single instruction for the micro:bit which was to set the motor speed to 100, the max speed. 

We decided to improve the project:

* The carousel should speed up and slow down progressively, like a real carousel in the fairground.
* Music should play while it's running.
* In order that the carousel could be started very slowly the Lego project itself was modified to add gearing.

The final project comprised of 3 programs running on 3 micro:bits:

* A controller to start and stop the carousel
* The carousel program which controls the motor speed
* The music player 

A video of the final project is available on YouTube:

[![Watch the video](https://img.youtube.com/vi/vNZ_Xr9Fenk/maxresdefault.jpg)](https://youtu.be/vNZ_Xr9Fenk)

## How it Works
The controller micro:bit allows the user to set a max speed which starts at 10 (lower than this the motor makes a noise but doesn't turn) and can be set in increments of 5 until the max speed of 100. The default speed is 60.

The user presses the A button on the controller to start the carousel. This sends a `start` message via Bluetooth with a desired max speed. The carousel's micro:bit upon receiving this message displays an up arrow while starting up and uses a while loop to control the rate the motor turns. It also in turn sends a `start_music` command via Bluetooth which starts the music player. Once the carousel has reach max speed its micro:bit displays a tick symbol.

To stop the carousel the user presses the B button. This sends a `stop` command to the carousel's micro:bit which in turn sends a `stop_music` command to stop the music. The carousel's micro:bit displays a down arrow whilst slowing down and then a stop symbol (🔲) when it has come to a full stop. One the carousel starts to slow down the music player will finish playing its current verse and then will stop.

## Problems Encountered
The micro:bit runs an event queue but it was found that when a certain type of event has fired no further events will fire until the first has fully completed. This is [described on this page](https://lancaster-university.github.io/microbit-docs/concepts/#queued-events) as detailed below: 

> By default, the runtime will queue any events for your event handler until it has finished what its already doing. As soon as your handler is finished processing an event, the next one will be delivered (any other event handlers will be unaffected though - just because one event handler is busy, doesn't mean that another one can't receive its events!).

This meant that when the carousel has started up via a Bluetooth call, no further messages could be handled and the carousel couldn't be stopped until it had fully started. The solution to this issue is to use a variable in the receiving program, use the Bluetooth event to just set this variable, and then check the state of this property in the `forever` loop.

This solution was used successfully in the music player's program, but the issue was accepted as a limitation in the carousel program itself.

## Possible Improvements:
If attempting this project again the following improvements could be made:
* The carousel program should use a variable for starting and stopping as described above.
* The music currently stops before the carousel has come to a full stop, this could be improved so they stop at the same time.
* The music could speed up and slow down as the carousel is starting or stopping. This could use the `tempo` property.