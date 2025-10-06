class Student:
    def __init__(self,x,y,z):
        self.p = x
        self.q = y
        self.r = z
    def watch_videos(A):
        A.s = ''
        print(A.p,A.q,A.r)
name = 'Md Abdul Alim'
email = 'alim@gmail.com'
alim_obj = Student(name,email,50) 
alim_obj.watch_videos()
print(alim_obj.__dict__)
# ahnaf_obj = Student()

# #how to access


# print(alim_obj.name,alim_obj.email) 

# #dunder or magic methods

# ahnaf_obj.name = 'Md Ahnaf Tazwar'
# ahnaf_obj.email = 'ahnaf@gmail.com'

# print(ahnaf_obj.name,ahnaf_obj.email) #dunder or magic methods
