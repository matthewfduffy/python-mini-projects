def logger(func):
    from datetime import datetime
    def wrapper(*args, **kwargs):
        print('_' * 25)
        print(f"Ran on: {datetime.today().strftime('%Y-%m-%d %H:%M:%S')}")
        print(func.__name__)
        print(*args, **kwargs)
        print('_' * 25)
    return wrapper


@logger
def shutdown():
    print("System shutdown")

@logger
def restart():
    print("System restarts")

shutdown()
restart()