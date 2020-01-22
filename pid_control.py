import math

'''
P: proportional to the errors
I:
D:
'''

def response(errors, speed, limit, error_prior, integral_prior):
    # Kp = 0.3
    # Kl = 0.2
    # Kd = 0.2

    Kp = 0.3
    Kl = 0.2
    Kd = 0.1

    error = limit - speed
    integral = integral_prior + error
    derivative = (error-error_prior)
    # derivative = (error-error_prior)/speed if speed!=0 else (error-error_prior)/0.01

    speed = Kp*error + Kl*integral + Kd*derivative

    return speed, error, integral

# while True:
#     error = desired_value - actual_value
#     integral = integral_prior + error*iteration_time
#     derivative = (error-error_prior)/iteration_time
#
#     output = Kp*error + Kl*integral + Kd*derivative + bias
