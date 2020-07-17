from tqdm import tqdm

n = 1_000_000
ncols = 100


def bench_creation(sc, cc, tc):
    print("Benchmarking object creation")
    for _ in tqdm(range(n), desc=str(sc), ncols=ncols):
        inst = sc(1, 1)
    for _ in tqdm(range(n), desc=str(cc), ncols=ncols):
        inst = cc(1, 1, 1)
    for _ in tqdm(range(n), desc=str(tc), ncols=ncols):
        inst = tc(1, 1, 1, 1)


def bench_calls(sc, cc, tc):
    print("Benchmarking object method calling and usage")
    inst = sc(1, 1)
    for _ in tqdm(range(n), desc=str(sc), ncols=ncols):
        inst.add()
        inst.sub()
        inst.div()
    inst = cc(1, 1, 1)
    for _ in tqdm(range(n), desc=str(cc), ncols=ncols):
        inst.add()
        inst.sub()
        inst.div()
    inst = tc(1, 1, 1, 1)
    for _ in tqdm(range(n), desc=str(tc), ncols=ncols):
        inst.add()
        inst.sub()
        inst.div()


from fastclass.regular import SomeClass, ChildClass, ThirdClass

bench_creation(SomeClass, ChildClass, ThirdClass)
bench_calls(SomeClass, ChildClass, ThirdClass)

print()
print()
print()
from fastclass.func import SomeClass, ChildClass, ThirdClass

bench_creation(SomeClass, ChildClass, ThirdClass)
bench_calls(SomeClass, ChildClass, ThirdClass)
