from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/2024/05/06/blog-post-1/") #  --->  http://localhost/2024/05/06/blog-post-1/
        self.client.get("/2024/05/06/blog-post-2/") #  --->  http://localhost/2024/05/06/blog-post-2/
        self.client.get("/2024/05/06/blog-post-3/") #  --->  http://localhost/2024/05/06/blog-post-3/


