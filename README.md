This is a template for an automated server testing,
that adapts to the server load, so that it does not impact other simultaneous tests.

How it works:
Given an initial test frequency, it slowly increases the frequency while monitoring the results.
If an error is returned from the host server, the tool decreases the speed and slowly increases the speed.
It uses an optimization logic, to find the ideal testing speed at a given time.
