import csv
import sys


def check(timeslot):
  global assigned_slots
  n = []

  for i in range(len(assigned_slots)):
    if assigned_slots[i]==timeslot:
      n.append(i)

  return n


def allocate_rooms(assigned_slots):
  global room_list

  rooms = []

  #go through list of timeslots,
  #eg if there are 3 rooms each slot should be repeated up to 3x.
  #Put one room for each repeat.

  for i in range(len(assigned_slots)):
    rooms.append(room_list[assigned_slots[:i].count(assigned_slots[i])])  

  return rooms



def pick_next_subject():
  global compulsory, assigned_slots

  for i in range(len(assigned_slots)):
    if (not assigned_slots[i]) and compulsory[i]:
      return i
  
  for i in range(len(assigned_slots)):
    if not assigned_slots[i]:
      return i

    

def output(assigned_slots,assigned_rooms):
  global subjects,output_path
  
  for i in range(len(assigned_slots)):
    print("%s gets timeslot %s in Room %s" %(subjects[i],assigned_slots[i],assigned_rooms[i]))

  with open(output_path,'w',newline='') as opfile:
      
    opwriter = csv.writer(opfile)
    for i in range(len(subjects)):
      opwriter.writerow([subjects[i],assigned_slots[i],assigned_rooms[i]])

  return


def backtrack():

  global domains,compulsory,assigned_slots,num_rooms,done

  if 0 not in assigned_slots:
    assigned_rooms = allocate_rooms(assigned_slots)
    output(assigned_slots,assigned_rooms)

    done = True
    return

  n = pick_next_subject()  #index of next subject to be assigned

  #print(n)

  for timeslot in domains[n]:
    assigned_slots[n] = timeslot
    ok = True

    # check each of the two constraints
    # 2 compulsory subjects cannot have same timeslot
    # only num of subjects equal to num of rooms can share a slot
    
    same_time_subjects = check(timeslot)

    if len(same_time_subjects)>num_rooms:
      ok = False

    if compulsory[n]:
      for subject in same_time_subjects:
        if compulsory[subject] and subject!=n:
          ok = False

    if ok:
      backtrack()

    if done:
      break

    assigned_slots[n] = 0 #this particular assignment failed

    #let it check the next assignment

  #if none of the values in the domain worked, have to go back to previous level
  return


def get_input(path):

    csv_input = []

    with open(path,'r',newline='') as file:
      reader = csv.reader(file)
      for row in reader:
        csv_input.append(row)

    return csv_input

#We have n subjects who must be assigned to a particular room and timeslot

#Global Variables

done = False                  #signifies if all have been assigned
subjects = []           #list of subjects
assigned_slots = []    #timeslot to subject mapping
compulsory = []        #compulsory/optional mapping
domains =[]          #nested list of possible timeslots for each subject
room_list = []         #list of rooms
assigned_rooms = []    #room to subject mapping

input_path = sys.argv[1]
output_path = sys.argv[2]

csv_input = get_input(input_path)

for row in csv_input:
  subjects.append(row[0])

  c = 1 if row[1]=='c' else 0
  compulsory.append(c)

  domains.append(row[2:])

subjects = subjects[:-1]
domains = domains[:-1]
compulsory = compulsory[:-1]

room_list = csv_input[-1]

num_rooms = len(room_list)
assigned_slots = [0 for i in subjects]

backtrack()

if not done:
    print("Problem impossible")
