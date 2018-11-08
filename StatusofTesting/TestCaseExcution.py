class Resource():
    
    total_count = 0
    total_duration = 0
    def __init__(self, name, age, country):
        self.name=name
        self.age=age
        self.country=country

    def execute(self, number_of_case, duration):
        Resource.total_count += number_of_case
        Resource.total_duration +=  duration
        
class Manager(Resource):

    def __init__(self, name, age, country):
        super(Manager, self).__init__(name, age, country)
    
    def reporting(self):
        print('Team executed ' + str(Resource.total_count) +' cases in '+ str(Resource.total_duration) + ' hours.')
        
class TeamMember(Resource):
    
    def __init__(self, name, age, country):
        super(TeamMember, self).__init__(name, age, country)
    
        
arif=TeamMember('Arif', '45', 'USA') 
niranjan=TeamMember('Niranjan', '43', 'India' )
kamal=TeamMember('Kamal',  '65', 'Bangladesh')    
fatima=TeamMember('Fatima',  '50', 'USA')
mallika=TeamMember('Mallika' , '35', 'USA')

arif.execute(50, 1)
niranjan.execute(50, 2)
kamal.execute(20, 4)
fatima.execute(10, 2)
mallika.execute(60, 1)


manager=Manager('Zarif', '18', 'Bangladesh')
mallika.execute(80, 2)

manager.reporting()