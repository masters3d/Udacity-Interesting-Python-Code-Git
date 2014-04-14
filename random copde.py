hey=("hey","what")
#print hey[1]

(7 - 2) / (3 ** 2)
(8 + (1 + (2 * 4) - 3))
8 / -2

MYnumber=1
__number__=1
#my.number=1
#my-number=1
ounces=1
number123=1

x=1
y=2
x = x + y
x += x + y
y += x
x += y

p=False
q=False  

#print not (p or not q)

n=123
#print ((n - n % 10) % 100) / 10
#print (n % 10) / 10
#print (n % 100 - n % 10) / 10

import random
#print random.randint(0, 10)
#print random.randrange(0, 10) 
import math

def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)    
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale
    
#project_to_distance(2, 7, 4)


def outx(x):
  print -5*x**5+69*x**2-47
  
#outx(0)
#outx(1)
#outx(2)
#outx(3)


def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    return present_value*((1+rate_per_period)**periods)

#print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)

    
#print future_value(500, .04, 10, 10)

# n s^2 / tan(/n)

import math
def area(n,length):
  top=((1.00/4)*n*(length**2))
  print top
  low=math.tan(math.pi/n)
  print low
  print top/low
  
#area(7,3)


#def rpsls(name):
  
    
#print rpsls("rock")

guate = "Guatemala is awasome"

print """heye what thf sdfasdfas %s"""%guate

###
wikientries = db.GqlQuery("""SELECT * 
                            FROM WikiEntry
                            WHERE title='%s'
                            ORDER BY
                            created DESC
                            """%wikititle)
if wikientries:
  lastentry=wikientries[0]
  
if wikientries==False:
  self.redirect("/wiki/_edit"+wikititle)
  


