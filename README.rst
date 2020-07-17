FastClass
=========


Sometimes a class has a few objects and their methods are called a LOT of
times. Here's an alternative way of doing 'classes' in which method calling is
faster than normal classes in Python.

Of course this comes wiht drawbacks so use it wisely.

Run `python -m fastclass.bench` to get this:

    Benchmarking object creation
    <class 'fastclass.regular.SomeClass'>: 100%|█████████| 1000000/1000000 [00:00<00:00, 2471195.92it/s]
    <class 'fastclass.regular.ChildClass'>: 100%|████████| 1000000/1000000 [00:00<00:00, 2315528.32it/s]
    Benchmarking object method calling and usage
    <class 'fastclass.regular.SomeClass'>: 100%|█████████| 1000000/1000000 [00:00<00:00, 1906948.22it/s]
    <class 'fastclass.regular.ChildClass'>: 100%|█████████| 1000000/1000000 [00:01<00:00, 958928.20it/s]
    Benchmarking object creation
    <function SomeClass at 0x7fdf25a35510>: 100%|████████| 1000000/1000000 [00:00<00:00, 1418685.99it/s]
    <function ChildClass at 0x7fdf25a35bf8>: 100%|████████| 1000000/1000000 [00:01<00:00, 809950.90it/s]
    Benchmarking object method calling and usage
    <function SomeClass at 0x7fdf25a35510>: 100%|████████| 1000000/1000000 [00:00<00:00, 2137436.26it/s]
    <function ChildClass at 0x7fdf25a35bf8>: 100%|███████| 1000000/1000000 [00:00<00:00, 1368512.72it/s]


