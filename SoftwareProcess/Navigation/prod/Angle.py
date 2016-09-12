'''
    Created on Sep 11, 2016
    @author: Donghuang Li
'''
class Angle():
    def __init__(self):
        self.degrees = 0
        self.minutes = 0
        #self.angle = ...       set to 0 degrees 0 minutes
    
    def setDegrees(self, *degrees):
        # either one or no degrees inputs
        if len(degrees) > 1:
            raise TypeError("Angle.setDegrees() only takes 0 or 1 degrees parameter")
        else:
            if len(degrees) == 0:
                pass
            else:
                if not isinstance(degrees[0], (int, float)):
                    raise TypeError("ValueError: Angle.setDegrees() only takes Integer or Float degrees input")
                else:
                    self.degrees = degrees[0]
                    self.__formatAngle()            
                
    def setDegreesAndMinutes(self, degrees):
        # checks separator 'd' and format degrees & minutes
        count_d = 0
        for s in degrees:
            if s == 'd':
                count_d += 1
        if count_d == 0:
            raise TypeError("Angle.setDegrees() missing separator 'd' ")
        elif count_d > 1:
            raise TypeError("Angle.setDegrees() only takes 1 separator 'd' ")
        else:
            dm = degrees.split("d")
            try: 
                float(dm[0])
            except:
                raise TypeError("ValueError: Angle.setDegreesAndMinutes() only takes Integer or Float 'Degrees' input")
            try: 
                float(dm[1])
            except:
                raise TypeError("ValueError: Angle.setDegreesAndMinutes() only takes Integer or Float 'Minutes' input")
            else:
                self.degrees = float(dm[0])
                self.minutes = float(dm[1])
                self.__formatAngle()
    
    def add(self, angle):
        self.degrees += angle.degrees
        self.minutes += angle.minutes
        self.__formatAngle()
    
    def subtract(self, angle):
        self.degrees -= angle.degrees
        self.minutes -= angle.minutes
        self.__formatAngle()
    
    def compare(self, angle):
        if not isinstance(angle, Angle):
            raise TypeError("ValueError: Angle.compare() only takes Angle type 'angle' input")
        else:
            if self.degrees < angle.degrees:
                return -1
            elif self.degrees == angle.degrees:
                if self.minutes < angle.minutes:
                    return -1
                elif self.minutes == angle.minutes:
                    return 0
                else:
                    return 1
            else: 
                return 1           
    
    def getString(self):
        return str(self.degrees)+"d"+str(self.minutes)
    
    def getDegrees(self):
        pass
    
    def __formatAngle(self):
    # this method is for formating the degrees value: 0~360d, 0~60m
    # to be improved
        if self.minutes > 60:
            self.minutes -= 60
            self.degrees += 1
        elif self.minutes < 0:
            self.minutes += 60
            self.minutes -= 1    
        if self.degrees > 360:
            self.degrees -= 360
        elif self.degrees < 0:
            self.degrees += 360

      
a = Angle()
a.setDegrees(60)
b = Angle()
b.setDegreesAndMinutes("60d0")
print a.compare(b)
a.subtract(b)
print a.getString()