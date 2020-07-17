FastClass
=========


Sometimes a class has a few objects and their methods are called a LOT of
times. Here's an alternative way of doing 'classes' in which method calling is
faster than normal classes in Python.

Of course this comes wiht drawbacks so use it wisely.

Run `python -m fastclass.bench` to get this:

    Benchmarking object creation
    <class 'fastclass.regular.SomeClass'>: 100%|█████████| 1000000/1000000 [00:00<00:00, 2442567.71it/s]
    <class 'fastclass.regular.ChildClass'>: 100%|████████| 1000000/1000000 [00:00<00:00, 2235191.86it/s]
    <class 'fastclass.regular.ThirdClass'>: 100%|████████| 1000000/1000000 [00:00<00:00, 1464238.55it/s]
    Benchmarking object method calling and usage
    <class 'fastclass.regular.SomeClass'>: 100%|█████████| 1000000/1000000 [00:00<00:00, 1831228.34it/s]
    <class 'fastclass.regular.ChildClass'>: 100%|█████████| 1000000/1000000 [00:01<00:00, 899841.24it/s]
    <class 'fastclass.regular.ThirdClass'>: 100%|█████████| 1000000/1000000 [00:01<00:00, 594763.71it/s]



    Benchmarking object creation
    <function SomeClass at 0x7febca63e730>: 100%|████████| 1000000/1000000 [00:00<00:00, 1348390.23it/s]
    <function ChildClass at 0x7febca6731e0>: 100%|████████| 1000000/1000000 [00:01<00:00, 754916.36it/s]
    <function ThirdClass at 0x7febca673268>: 100%|████████| 1000000/1000000 [00:01<00:00, 505582.03it/s]
    Benchmarking object method calling and usage
    <function SomeClass at 0x7febca63e730>: 100%|████████| 1000000/1000000 [00:00<00:00, 2008960.64it/s]
    <function ChildClass at 0x7febca6731e0>: 100%|███████| 1000000/1000000 [00:00<00:00, 1279579.04it/s]
    <function ThirdClass at 0x7febca673268>: 100%|████████| 1000000/1000000 [00:01<00:00, 897983.11it/s]
