import self as self


class coder:
    loc=100
    def __init__(self):
        self.error=20

suriya=coder()
print(suriya.error)

'''approach 3'''

sunday=("sleep","eat","sleep")

print(sunday[2])

'''approach 4'''

sunday={"morning":"dosa","afternoon":"fish","evening":"snacks"}
print(sunday["afternoon"])

'''approach 2'''

class friday:
    __work="python"
    def __init__(self):
        self.__milk=3
    def display(self):
        print(self.__milk)

suriya=friday()
suriya.display()

'''approach 5'''

for i in sunday.values() :
    print(i)
for i in sunday.keys():
    print(i)

'''approach 6'''

friends=[{"id":23,"name":"sasi","branch":"school"},{"id":24,"name":"john","branch":"college"},{"id":25,"name":"nava","branch":"college"}]
print(friends[0],friends[1])

for i in friends:
    if i["name"]=="sasi":
        print("sasi is available")
    if i["branch"]=="college":
        print("college")


class disys:
    def __init__(self,vacc):
        self.vac=[]
        self.vac.append(vacc)
        self.count=0
    def logic(self, continue = None):5
         for i in self.vac:
             if i ["vaccine"]== none:
                 s1elf.count = self.count+1
         else:
             continue
         print(self.vac)
    def __del__(self):
        print("de allocation")
        del self.vac
        del self.count

sp=disys({"name":"suriyaprakash","empid":"007","vaccine":"none"})
s=disys({"name":"sneha","empid":"005","vaccine":"1st dose"})
s.logic()