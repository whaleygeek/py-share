# py-share
A simple Python library to share values via local publish and subscribe


## What is it?

py-share is a Python library that provides a quick and simple way to share
data between running Python programs.

With it, you can run multiple programs, in different versions of Python,
on the same computer, and communicate signals and values between them.

You might want to use this if you have some old code that only runs in
Python 2, and some newer code that you want to run in Python 3. Before
taking on the pain of trying to integrate those two bits of code together,
you might want to just 'try something quick' with your code. py-share
allows you to do this.


## What can I do with it?

py-share is very simple, almost too simple. But it gives you a way to
send small messages between different running programs. Typically you
might have two or more shell windows open, each running a different
instance of the Python interpreter, running a different program.

Think of it a bit like a procedure call, but in a way that the procedure
you are calling is inside a different running program. In program A
you 'share' (possibly with some data), and in program B it detects this
'share' and actions it.


## How do I test it?

The first thing to do is to try the share_test.py program, to check
that the code works, and to help you understand what it does (and
also to understand what it doesn't do!)

In terminal window A:

    python share_test.py rx
    
In terminal window B:

    python share_test.py tx
    
Note that you could use python version 2 (python) in one terminal,
and python version 3 (python3) in another terminal.

The tx tester will share 10 messges. The rx tester will receive and
display those messages. That's it!


## How do I use it to trigger something?

Start with this:

    import share
    
Inside your sending program, use this to trigger something has happened
on a share name (e.g. the share name below is 'fred'):
    
    share.fred()
    
Inside your receiving program, use this to check if fred has been 'triggered'

    if share.isfred():
    
Inside your receiving program, use this to clear the triggered share, which
will 'unblock' the sending program.

    share.getfred()
    
The sender is blocking - so it will trigger a signal, then wait for it to
be processed.


## How do I transfer data?

If you also want to transfer some data when triggering the share, just put the
data in the parameters like this:

    share.fred("I am happy")
    
On the receiving end, you can get the data from the return result like this:

    if share.isfred():
        mood = share.getfred()
        print(mood)
        

## How does it work?

It's almost too simple. 

When you share, it creates a small data file in the current directory. 
If there is data included in the share, the data goes inside that file.

When the receiving end checks to see if the share has been triggered,
it just checks for the presence or absence of a file of that name
in the current directory. So, if you use a share name of 'fred'
then the file created will be called 'fred.share'. If the receiving
end wants to read some data, it just reads it from the file.

When the receiving end calls share.getfred() on the fred share,
first it copies out any data from the file, and finally it deletes
the file. The file being deleted signals to the sender that it can
continue.

That's it!


## What's the clever bit?

There is a bit of Python magic in there to make the interface
really easy to use, and it's all based around what you call the
method when you call the share module.

    share.fred()
    # actually calls share.send("fred", None)
    
    share.fred("is happy")
    # actually calls share.send("fred", "happy")
    
    share.isfred()
    # actually calls share.check("fred")
    
    share.getfred()
    # actually calls share.get("fred")

So, you can have any number of shares sending messages between any number
of programs. Just think of a name, and share on that name.

If you want to use a string as the name of the share, then you can always 
use the send() check() and get() methods directly if you need to.


## Why did I write py-share?

This code was written really quickly to solve a single problem that I had.
I had some code that only worked with Python2, and some code that only
worked with Python3. I had to find a very quick way to get the two pieces
of code to work together. 


## What are the limitations?

There are lots of limitations. Some of these will be fixed, some of them
won't be fixed. For the ones that won't be fixed, I recommend you use a
more robust pub/sub mechanism like MQTT. But in the simple case, py-share
might get you out of a hole.

* The sender is blocking

Just like when you call a procedure in Python, the calling program
waits until the procedure completes before continuing. It's just
like a synchronous control flow, or a blocking function.

* The receiver is polled

There are no threads, and no proper concurrency. There are no callbacks
(new coders often struggle to understand callbacks, and where threads
are in use they create some interesting concurrency problems for new
users to understand). So the only way to check if a share is triggered,
is to poll it with the 'is' method.

* There can only be one sender on a share

Because the underlying implementation creates a file to trigger the share,
you can't have two separate programs triggering the same share, or two
threads in the same program triggering the same share. Besides, once you
trigger a share, the calling program is blocked until the share is
released.

* There can only be one receiver on a share

Because the underlying implementation deletes the share file once the
get() returns, the share is single use - so you cannot have two separate
programs receiving from a share, and cannot have two separate threads
receiving from a share.

* The programs have to run in a shared file system

The implementation triggers and sends data via files in the file system.
So that file system has to be shared. You could use an nfs mount between
machines, but then you'd probably be better using something like MQTT
instead.

* The programs have to be running in the same directory

To keep things simple, there is no configuration. Share files are
created in the current working directory of the running programs,
so the running programs must all have the same working directory.

*. The data transfer might not be completely lock safe at the moment

I've tested the triggering mechanism and it works really well. However
there is not a platform independent way of opening files for exclusive
write, so if you transfer data via a share, it might not work properly
at the moment. I plan to solve this one by adding in a number of different
exclusive lock mechanisms for different platforms, and hiding that detail
from you. So it's possible you might send() an large object, and the
get() end might sense the trigger file, read half the object, and then
try to delete the file. I will fix that.


## What's next?

Apart from the first one, I might never do any of the others. Perhaps use
MQTT or some other pub/sub mechanism if you need those features.

* Writing a test case to expose the non-locking issue for data transfer,
  and writing and testing a solution on all platforms (Windows, OSX, Linux)
  
* Deciding whether to add an optional transmit queue for a share, so that it is
  possible to have asynchronous sharing as well as synchronous sharing.
  
* Deciding whether to add per-process receive queuing for a share, so that it is
  possible to have multiple receivers from a single share transmitter.
  
* Deciding whether to support multiple transmitters on a share.

* Deciding whether to separate the transport mechanism from the interface,
  and providing bindings to other transports other than a local file,
  such as MQTT, or a simple network multicast message.
  
* Deciding whether to add callbacks and a loop(). The loop() could either
  be called cooperatively, or via a thread. This would allow multiple share
  watches to be set up in the background and each wired up to their own
  custom handler function.
  
* Deciding whether to support a richer argument passing syntax in the
  share.send - multiple arguments passed could be wrapped together in
  the data sent in the file (e.g. one per line), and unwrapped at the
  get() end (e.g. returned as a tuple). This would make it possible
  to turn this into an arbitrary remote procedure call mechanism,
  because the unwrapped parameters at the receiving end could be
  interpreted as function_name(*args) and dispatched to any function
  at the receiving end.

David Whale

@whaleygeek

April 2016
