//Jethro Carter Watson
//CS 1410
//ASSN 6

public class GregorianDate extends Date {
    //default constructor
    GregorianDate() {
        //initialize date
        m_day = 1;
        m_month = 1;
        m_year = 1970;
        //get time since 01/01/1970
        float current = System.currentTimeMillis();
        //account for timezone
        current += java.util.TimeZone.getDefault().getRawOffset();
        //convert current to day
        current /= (1000 * 3600 * 24);
        //change current to int
        int currentInt = (int) current;
        //add days to time
        addDays(currentInt);
    }

    //overloaded constructor
    GregorianDate(int year, int month, int day) {
        //initialize date to year, month, day provided
        m_day = day;
        m_month = month;
        m_year = year;
    }

    //public add days instance method
    public void addDays(int days) {
        //loop over number of days to add
        for (int i = 0; i < days; i++) {
            //add one to object day
            m_day++;
            //if object day is now larger than the number of days in object month
            if (m_day > getNumberOfDaysInMonth(m_year, m_month)) {
                //set object day to 1
                m_day = 1;
                //add one to object month
                m_month++;
                //if month is now 13
                if (m_month == 13) {
                    //set object month to 1
                    m_month = 1;
                    //add one to object year
                    m_year++;
                }
            }
        }
    }

    //public sub days instance method
    public void subtractDays(int days) {
        //loop over number of days to subtract
        for (int i = 0; i < days; i++) {
            //add one to object day
            m_day--;
            //if object day is now zero
            if (m_day == 0) {
                //subtract one from object month
                m_month--;
                //if month is now 0
                if (m_month == 0) {
                    //set object month to 12
                    m_month = 12;
                    //subtract one from object year
                    m_year--;
                }
                //set object day to last day of new month
                m_day = getNumberOfDaysInMonth(m_year, m_month);
            }
        }
    }

    //public is leap year
    public boolean isLeapYear() {
        //return the value of the private method
        return isLeapYear(m_year);
    }

    //private methods
    public boolean isLeapYear(int year) {
        //every four years is a leap year
        if (year % 4 == 0) {
            //except every 100
            if (year % 100 == 0) {
                //unless its every 400
                if (year % 400 == 0) {
                    return true;
                }
            } else {
                return true;
            }
        }
        return false;
    }
}
