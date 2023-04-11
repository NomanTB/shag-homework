class Gen():
    def __init__(self,numb,):
        self.numb = numb

    def __iter__(self):
        for i in range(0,self.numb):
            yield i * 10




for i in Gen(numb = 10):
    print(i)







