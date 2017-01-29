from threading import Thread

def resFun(fun):
    def int_wrapper(*args):
        args1 = args[0]
        res = args[1]
        res.append(fun(*args1))
    return int_wrapper

def split_and_merge(n_threads, reduce_f):
    def decorator(fun):
        def wrapper(*args):
            my_fun = resFun(fun)
            list_ = args[0]
            list_of_lists = []
            div = len(list_) // n_threads
            for i in range(0, n_threads):
                start = i*div
                if i == n_threads-1:
                    end = len(list_)
                else:
                    end = (i+1)*div
                list_n = list_[start:end]
                list_of_lists.append((list_n, []))
            #print(list_of_lists)
            list_of_threads = [Thread(target=my_fun, args=((list_n,), res)) for list_n, res in list_of_lists]
            for instance in list_of_threads:
                instance.start()
            list_of_threads = [instance.join() for instance in list_of_threads]
            list_of_results = [res[0] for list_n, res in list_of_lists]
            return reduce_f(list_of_results)
        return wrapper
    return decorator
