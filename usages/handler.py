import signal

import openai


class TimeoutException(Exception):
    pass


def timeout_handler(signum, frame):
    raise TimeoutException()


def openai_request(openai_sdk=None, timeout=None, *args, **kwargs):
    print(f'================> openai_request.args: {args}')
    print(f'================> openai_request.kwargs: {kwargs}')

    timeout = timeout or 30  # 定义超时时间
    signal.signal(signal.SIGALRM, timeout_handler)  # 注册信号处理程序
    signal.alarm(timeout)  # 设置超时时间

    try:
        if openai_sdk is not None and callable(openai_sdk):
            print("[ Start requesting OpenAI ]")
            return openai_sdk(*args, **kwargs)
    except (openai.error.APIError, TimeoutException) as err:
        if isinstance(err, openai.error.APIError):
            print(f"[ Request error: {err} ]")
        else:
            print("[ OpenAI request timed out ]")
    else:
        print("[ Successful request ]")
    finally:
        signal.alarm(0)  # 关闭超时计时器
        print("[ Turn off the timeout timer ]")
        print("[ Completed request ]")
