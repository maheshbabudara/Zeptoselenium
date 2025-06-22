from locust import User,task,constant

class Base(User):
    wait_time=constant(1)

    @task
    def say_hello(self):
        print('Hi Mahesh')

    @task
    def gud(self):
        print('Rony')
    @task
    def cool(self):
        print('Cooling')

