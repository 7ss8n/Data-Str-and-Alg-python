class Date:
    #Create an object instance for the specified Gregorian date
    def __init__( self, month, day, year ):
        self._julianDay = 0
        assert self._isValidGregorian( month, day, year ), \
               'Invalid gregorian Date.'
        tmp = 0
        if month < 3 :
            tmp = -1
        self._julianDay = day - 32075 + \
                          (1461 * ( year + 4800 + tmp ) // 4) + \
                          (367 * ( month - 2 - tmp * 12) //12) - \
                          (3 * (( year + 4900 + tmp) // 100 ) // 4)
    def month ( self ):
        return (self._toGregorian())[0]

    def monthName( self ):
        dict = {1: 'January', 2: 'February', 3: 'March', \
                4: 'April', 5: 'May', 6: 'June', \
                7: 'July', 8: 'August', 9: 'Spetember', \
                10: 'October', 11: 'November', 12: 'December'}
        return dict[ self.month()]
        
    def day( self ):
        return (self._toGregorian())[1]
    
    def year( self ):
        return (self._toGregorian())[2]

    def isLeapYear( self ):
        return ((self.year() % 4 == 0 and self.year() % 100 != 0) \
               or self.year() % 400 == 0)

    def dayOfWeek( self ):
        month, day, year = self._toGregorian()
        if month < 3 :
            month = month + 12
            year = year - 1
        return ((13 * month + 3) // 5 + day + \
                year + year // 4 - year // 100 + year // 400) % 7

    def dayOfYear( self ):
        firstDay = Date(1, 1, self.year())
        return self.numDays(firstDay) + 1
    
    def dayOfWeekName( self ):
        d = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3 : 'Thursday', \
             4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
        return d[self.dayOfWeek()]
    
    def isWeekday( self ):
        return self.dayOfWeek() != 6
    
    def isEquinox( self ):
        return (self.day() == 20 and self.month() == 3) or \
               (self.day() == 22 and self.month() == 9)
    def isSolstice( self ):
        return (self.day() == 21 and self.month() == 6) or \
               (self.day() == 22 and self.month() == 12)

    
    def __str__( self ):
        month, day, year = self._toGregorian()
        return '%02d/%02d/%04d' % (month, day, year)

    def __eq__( self, otherDate):
        return self._julianDay == otherDate._julianDay

    def __lt__( self, otherDate):
        return self._julianDay < otherDate._julianDay

    def __le__( self, otherDate):
        return self._julianDay <= otherDate._julianDay

    def numDays( self, otherDate ):
        return abs(self._julianDay - otherDate._julianDay)

    def _toGregorian( self ):
        A = self._julianDay + 68569
        B = 4 * A // 146097
        A = A - (146097 * B + 3) // 4
        year = 4000 * (A + 1) // 1461001
        A = A - (1461 * year // 4) + 31
        month = 80 * A // 2447
        day = A - (2447 * month // 80)
        A = month // 11
        month = month + 2 - (12 * A)
        year = 100 * (B - 49) + year + A
        return month, day, year

    def advanceBy( self, days ):
        assert self._julianDay - days >= -365, \
               'You can not advance to a data before Nov 24, 4714'
        A = self._julianDay - days + 68569
        B = 4 * A // 146097
        A = A - (146097 * B + 3) // 4
        year = 4000 * (A + 1) // 1461001
        A = A - (1461 * year // 4) + 31
        month = 80 * A // 2447
        day = A - (2447 * month // 80)
        A = month // 11
        month = month + 2 - (12 * A)
        year = 100 * (B - 49) + year + A
        return month, day, year

    def asGreogrian( self, divchar = '/'):
        month, day, year = self._toGregorian()
        return '%02d%s%02d%s%04d' % (month, divchar, day, divchar, year)

         
    def _isValidGregorian( self, month, day, year ):
        return min([month in range(12), day in range(31), year >= -4713])
