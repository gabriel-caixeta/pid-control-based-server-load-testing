
# PID control inspired Server Load Testing</h1>
This is a template for an automated server testing tool,
that adapts to the server load, so that it does not impact other simultaneous tests.</h3>


## How it works
Given an initial test frequency, it slowly increases the frequency while monitoring the results.
If an error is returned from the host server, the tool decreases the speed and slowly increases the speed.
It uses a PID control based optimization logic, to smoothly find the ideal testing speed at a given time.

### PID control
>A proportional–integral–derivative controller (PID controller or three-term controller) is a control loop mechanism employing feedback that is widely used in industrial control systems and a variety of other applications requiring continuously modulated control. A PID controller continuously calculates an error value *e(t)* as the difference between a desired setpoint (SP) and a measured process variable (PV) and applies a correction based on proportional, integral, and derivative terms (denoted P, I, and D respectively), hence the name.
> [Source-wikipedia](https://en.wikipedia.org/wiki/PID_controller)
