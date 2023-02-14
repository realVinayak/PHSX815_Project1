from time import perf_counter


def perf_wrapper(func, message):
    t_init = perf_counter()
    callback_return = func()
    t_final = perf_counter()
    print(t_final - t_init, message)
    return callback_return
