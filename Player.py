class Player :
    ''' A player class '''
    squad, goalscharts, pointscharts, assistcharts, interceptioncharts = 0, {}, {}, {}, {}
    
    def __init__(self, name, position) :
        self.name = name
        self.position = position
        Player.goalscharts[self.name] = 0
        Player.pointscharts[self.name] = 0
        Player.assistcharts[self.name] = 0
        Player.interceptioncharts[self.name] = 0
        
    def intro(self) :
        print('Hello Coach! , My name is {0} and I play as a {1}'.format(self.name, self.position))
    
    def goal(self) :
        Player.goalscharts[self.name] += 1
        if self.position == 'GoalKeeper' :
            Player.pointscharts[self.name] += 60
        elif self.position == 'Defender' :
            Player.pointscharts[self.name] += 50
        elif self.position == 'MidFielder' :
            Player.pointscharts[self.name] += 50
        elif self.position == 'Winger' :
            Player.pointscharts[self.name] += 50
        elif self.position == 'Attacker' :
            Player.pointscharts[self.name] += 100
            
    def assist(self) :
        Player.assistcharts[self.name] += 1
        if self.position == 'GoalKeeper' :
            Player.pointscharts[self.name] += 60
        elif self.position == 'Defender' :
            Player.pointscharts[self.name] += 70
        elif self.position == 'MidFielder' :
            Player.pointscharts[self.name] += 80
        elif self.position == 'Winger' :
            Player.pointscharts[self.name] += 100
        elif self.position == 'Attacker' :
            Player.pointscharts[self.name] += 50
    
    def interception(self) :
        Player.interceptioncharts[self.name] += 1
        if self.position == 'GoalKeeper' :
            Player.pointscharts[self.name] += 60
        elif self.position == 'Defender' :
            Player.pointscharts[self.name] += 100
        elif self.position == 'MidFielder' :
            Player.pointscharts[self.name] += 80
        elif self.position == 'Winger' :
            Player.pointscharts[self.name] += 20
        elif self.position == 'Attacker' :
            Player.pointscharts[self.name] += 10   
            
    def PrintStats(self) :
        print('Player Name : {}'.format(self.name))
        print('Player Position : {}'.format(self.position))
        print('Player Goals : {}'.format(Player.goalscharts[self.name]))
        print('Player Assists : {}'.format(Player.assistcharts[self.name]))
        print('Player Interception(s) : {}'.format(Player.interceptioncharts[self.name]))
        print('Player Points : {}'.format(Player.pointscharts[self.name]))
    
            
