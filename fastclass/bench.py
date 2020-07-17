from tqdm import tqdm


def bench_creation(sc, cc, data):
    n = 10_000_000
    print("Benchmarking object creation")
    for _ in tqdm(range(n), desc=str(sc)):
        inst = sc(1, 1)
    for _ in tqdm(range(n), desc=str(cc)):
        inst = cc(1, 1, 1)


def bench_calls(sc, cc, data):
    n = 10_000_000
    inst = sc(1, 1)
    print("Benchmarking object method calling and usage")
    for _ in tqdm(range(n), desc=str(sc)):
        inst.add()
        inst.sub()
        inst.div()
    inst = cc(1, 1, 1)
    for _ in tqdm(range(n), desc=str(cc)):
        inst.add()
        inst.sub()
        inst.div()


n = 100

data = [(i, j, k) for i in range(1, n) for j in range(1, n) for k in range(1, n)]

from fastclass.regular import SomeClass, ChildClass

bench_creation(SomeClass, ChildClass, data)
bench_calls(SomeClass, ChildClass, data)

from fastclass.func import SomeClass, ChildClass

bench_creation(SomeClass, ChildClass, data)
bench_calls(SomeClass, ChildClass, data)
