"Task 1"
"-------------------------------------------------------"

def make_date(year,month,day):
    '''
function returns date sections according to given message:
year - the year in number
month - from number to word
day - the day in number
str - string representation of the date
    '''
    def dispatch(m):
        if m =='day':
            return day
        elif m == 'month':
            return months(month)
        elif m =='year':
            return year

    def months(msg):    
        if msg==1:
            return 'January'
        elif msg==2:
            return 'February'    
        elif msg==3:
            return 'March'
        elif msg==4:
            return 'April'       
        elif msg==5:
            return 'May'        
        elif msg==6:
            return 'June'        
        elif msg==7:
            return 'July'        
        elif msg==8:
            return 'August'        
        elif msg==9:
            return 'September'
        elif msg==10:
            return 'October'
        elif msg==11:
            return 'November'
        elif msg==12:
            return 'December'  
    return dispatch
       
def year(f):
    return f('year')

def month(f):
    return f('month')

def day(f):
    return f('day')

def str_date(f):
    return '{0}th of {1}, {2}'.format(year(f),month(f),day(f))
    
    

d = make_date(2016, 12, 26)
print(d)
print(year(d))
print(month(d))
print(day(d))
print(str_date(d))


"-------------------------------------------------------------"
""" Task 2 """
"-------------------------------------------------------------"

def data_preprocessing_file_types(str):
    "enumerating the data + cleaning the data + complete missing values"
    str=map(lambda x: x if x[-1:]!='.' else x+"txt" ,map(lambda x: ".".join(x.split("..")),str.split(";")))
    str=tuple(map(lambda x: x.split("."),(filter(lambda x: "." in x,str))))
    return Counter(map(lambda x: x[1],str)).most_common()

def data_preprocessing_tree(str):
    "enumerating the data + cleaning the data + complete missing values"
    str=map(lambda x: x if x[-1:]!='.' else x+"txt" ,map(lambda x: ".".join(x.split("..")),str.split(";")))
    "creates pairs of file path and file name"
    str=map(lambda x: tuple(x),map(lambda x:"".join(x).replace('/f',"/ f").split() if x.count(".") == 1 else (x, None),str))
    "creates the files tree"
    str=map(lambda x:(x[0],tuple(map(lambda x: x[1],filter(lambda file: True if file[0] == x[0] else False, str)))), str)
    return list(set(str))

data="/User/someuser/file.py;/tmp/download/file.zip;/tmp/download/file2.zip;/;/usr/local/bin;/User/someuser/file..py;/tmp/file.;/usr//some;"


"-------------------------------------------------------------"
""" Task 3 """
"-------------------------------------------------------------"

def make_currency(amount,symbol):
    '''
 function returns sections according to given message:
 get_value - value of amount/symbol  
 set_value - update value of amount
 str - string of type
 convert - convert given amount to another currency
    '''
    def dispatch(msg):
        if msg == 'get_value':
            return get_value
        elif msg == 'set_value':
            return set_value
        elif msg == 'str':
            return str(amount,symbol)
        elif msg == 'convert':
            return convert
            
    def get_value(m):
        nonlocal amount,symbol
        if m =='amount':
            return amount
        elif m =='symbol':
            return symbol

    def set_value(m,new):
        nonlocal amount
        if m == 'amount':
            amount = new
            
    def str(symbol,amount):
        return repr('{0}{1}'.format(symbol,amount))
    
    def convert(func,symbol):
        nonlocal amount
        amount = func(amount)    

    return dispatch

c = make_currency(10.50, '$')
print(c('get_value')('amount'))
print(c('get_value')('symbol'))
c('set_value')('amount', 50)
print(c('get_value')('amount'))
print(c('str'))
c('convert')(lambda x: x*3.87,'Shekel')
print(c('str'))

"""----------------------------------------"""
""" Task 4 """
"""----------------------------------------"""
def get_reverse_map_iterator(s = [],g = lambda x:x):
    '''
function input: sequence and lambda function
return value: dictionary with messages: 
next - next value in the Iterator 
has_more - boolean funcion which return T/F if there is next value      
    '''
    index = 0
    records = list(s)
    records.reverse
    def next():
        nonlocal index
        if index>= len(records):
            return 'no more items'
        item = g(records[index])
        index+=1
        print(item)
        return item
        
    def has_more():
       return index < len(records)

    dispatch = {'next': next, 'has_more': has_more}
    return dispatch

it = get_reverse_map_iterator((1,3,6), lambda x: 1/x)
while it['has_more']():
    it['next']()

it = get_reverse_map_iterator((1,3,6))
for i in range(1,6):
    it['next']()

"""-------------------------------------------------"""
"""Task 5"""
"""-------------------------------------------------"""
import copy

empty_rlist = None
def make_rlist(first, rest):
    """Make a recursive list from its first element and the rest."""
    return (first, rest)
def first(s):
    """Return the first element of a recursive list s."""
    return s[0]
def rest(s):
    """Return the rest of the elements of a recursive list s."""
    return s[1]
def len_rlist(s):
    """Return the length of recursive list s."""
    length = 0
    while s != empty_rlist:
        s, length = rest(s), length + 1
    return length
def getitem_rlist(s, i):
    """Return the element at index i of recursive list s."""
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)

def make_mutable_rlist(tcopy = None):
    """Return a functional implementation of a mutable recursive list."""
    contents = empty_rlist 
    if tcopy != None:
        rlist = make_mutable_rlist()
        L=tcopy['str']()
        tmp=[]
 
        for i in range(len(L)):
            tmp.append(L[i])
        tmp.reverse()
        
        for i in range(len(L)):
            rlist['push_first'](tmp[i])
        return rlist
    
    def length():
        """return the length of the list."""
        return len_rlist(contents)
    
    def get_item(ind):
        """returns the item that in index ind of the list"""
        return getitem_rlist(contents, ind)
    
    def push_first(value):
        """"puts the beginning of the list"""
        nonlocal contents
        contents = make_rlist(value, contents)
        
    def pop_first():
        """removes and returns the first element in the list"""
        nonlocal contents
        f = first(contents)
        contents = rest(contents)
        return f

    def str():
        """ creat list from mutable_rlist"""
        L=[]
        for x in range(length()):
            L.append(get_item(x))
        return L 

    def extend(rlist):
        """ get list from  typy mutable_rlist make hem list,
        extend the old and the new list and return as mutable_rlist """
        nonlocal contents
        lst= str() + rlist['str']()
        lst.reverse()
        contents=None
        
        for i in range(len(lst)):
            push_first(lst[i])
     
    def Slice (First,Last):
        """ get first an last pacth creat a mutable_rlist and empty list,
        slice the list type and then return to new mutable_rlist var"""
        sliced = make_mutable_rlist()
        tmp=[]
        
        for i in range(First,Last):
            tmp.append(str()[i])
        tmp.reverse()
        
        for i in range(First,Last):
            sliced['push_first'](tmp[i])
        return sliced
      
    def get_iterator():
        L=str()
        i = 0
        
        def hasNext():
            nonlocal i
            return (i < len(L))
        
        def next():
            nonlocal i,L
            if hasNext():
                nextt = L[i]
                i+=1
                return nextt
            return None
                
        return {'next': next, 'hasNext': hasNext}
         
    return {'length':length, 'get_item':get_item, 'push_first':push_first, 
             'pop_first': pop_first, 'str':str, 'slice':Slice,'extend':extend,'get_iterator':get_iterator}

# "print"
# my_list= make_mutable_rlist()
# for x in range(4):
#     my_list['push_first'](x)
# print(my_list['str']())
# ext= make_mutable_rlist(my_list)
# my_list['extend'](ext)
# print(my_list['str']())
# print(my_list['slice'](0,2)['str']())
# yout_list = make_mutable_rlist(my_list)
# print(yout_list['str']())
# it=my_list['get_iterator']()
# while it['hasNext']():
#     print(it['next']())