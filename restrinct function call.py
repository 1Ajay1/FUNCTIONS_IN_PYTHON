def onecall(func):
             call={}
             def inner():
                          if func in call:
                                       print("Can not call")
                          else:
                                       call[func]=1
                                       func()
             return inner
def sample():
             print("sample is called")
sample=onecall(sample)
sample()
sample()
sample()

                          
