from celery import Celery

celery = Celery("tasks",
                broker='redis://localhost:6379/0',
                backend='redis')

@celery.task(name="tasks.add")
def add(x, y):
    return x + y

if __name__ == "__main__":
    celery.start()
