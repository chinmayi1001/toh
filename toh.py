#import sys
#define stack class
#define init

#define is_empty
#define push
#define pop



class Stack:
  def __init__(self):
    self.items=[]

  def push(self,item):
    self.items.append(item)
  def pop(self):
    if not self.is_empty():
      return self.items.pop()
  def is_empty(self):
    return len(self.items)==0



##define main function
#initialize stack as stack
#initialize done as done
#while not done
#while n>0 push inthe stack the n,from,to,aux
#n=n-1
#from ,to aux =from,aux ,to 
#after the n is 0
#until stack is empty retrieve elements of stack ,label as n,from,to,aux ,print move disk n from from to to
#n-1
#from to aux=aux to from
#while loop continues untill stack is empty
#after stack is empty set done to true
#while loop ends



def towerofhanoi(n,from_rod,to_rod,aux_rod):
  stack=Stack()
  done=False
  while not done:
    if n>0:
      stack.push((n,from_rod,to_rod,aux_rod))
      n=n-1
      from_rod,to_rod,aux_rod=from_rod,aux_rod,to_rod

    else:
      if not stack.is_empty():
        n,from_rod,to_rod,aux_rod=stack.pop()
        print("move disk",n,"from",from_rod,"to",to_rod)
        n=n-1
        from_rod,to_rod,aux_rod=aux_rod,to_rod,from_rod
      else:
        done=True

towerofhanoi(3,0,2,1)