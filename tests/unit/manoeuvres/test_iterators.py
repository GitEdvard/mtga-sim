import pytest


@pytest.mark.skip('')
class TestIterators:
    def test_first(self):
        gen = self.my_gen()
        for i in gen:
            print(i)
        assert True

    def my_gen(self):
        for i in range(3):
            yield i

    def test_next(self):
        gen = self.my_gen()
        next(gen)
        next(gen)
        next(gen)
        next(gen)

    def test_iterator1(self):
        it = MyIterator()
        iter(it)
        print(next(it))
        print(next(it))
        print(next(it))

        assert False

    def test_iterator2(self):
        it = Iterator2()
        for i in it:
            print(i)

        assert False

    @pytest.mark.now
    def test_recursive_iterator(self):
        it = Iterator3()
        for i in it:
            print(i)

        assert False

    def test_iter(self):
        it = Iterator3()
        print(next(iter(it)))
        assert False


    def test_len(self):
        it = Iterator3()
        length = len([i for i in it])
        assert length == 3

    def test_dict(self):
        it = Iterator3()
        it2 = iter(it.mydict)
        print(next(it2))
        print(next(it2))
        print(next(it2))

        assert False


class Iterator3:
    def __init__(self):
        self.my_list = [i for i in range(3)]
        self.mydict = dict()
        self.gen = None
        self.build()

    def build(self):
        for i in range(3):
            self.mydict[i] = [10 * i + j for j in range(3)]

    def subset_of(self, adict, exclude_key):
        return {key: adict[key] for key in adict if not key == exclude_key}

    def __iter__(self):
        self.gen = self.my_gen_rec(self.mydict, [], 0)
        return self

    def __next__(self):
        return next(self.gen)

    def my_gen_rec(self, adict, prev_items, level):
        try:
            key = next(iter(adict))
            next_dict = self.subset_of(adict, key)
        except StopIteration:
            yield prev_items
            return
        for item in self.mydict[key]:
            next_items = prev_items + [item]
            yield from self.my_gen_rec(next_dict, next_items, level + 1)


class Iterator2:
    def __init__(self):
        self.my_list = [i for i in range(3)]
        self.mydict = dict()
        self.gen = None
        self.build()

    def build(self):
        for i in range(3):
            self.mydict[i] = [10 * i + j for j in range(3)]

    def __iter__(self):
        self.gen = self.my_gen()
        return self

    def __next__(self):
        return next(self.gen)

    def my_gen(self):
        for key in self.mydict:
            for i in self.mydict[key]:
                yield i


class MyIterator:
    def __init__(self):
        self.gen = None

    def __iter__(self):
        self.gen = self.my_gen()
        return self

    def __next__(self):
        return next(self.gen)

    def my_gen(self):
        for i in range(3):
            yield i
