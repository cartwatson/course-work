//Jethro Carter Watson
//CS 1410
//ASSN 6

public class JulianDate extends Date {
    //default constructor
    JulianDate() {
        //initialize variables
        m_day = 1;
        m_month = 1;
        m_year = 1;
        //get time since 01/01/1970
        long current = System.currentTimeMillis();
        //account for timezone
        current += java.util.TimeZone.getDefault().getRawOffset();
        //convert current to day
        current /= (1000 * 3600 * 24);
        //change current to int
        int currentInt = (int) current;
        //add days to time + number of days from 1/1/1 to 1/1/1970
        addDays(currentInt + 719164);
    }

    //overloaded constructor
    JulianDate(int year, int month, int day) {
        m_year = year;
        m_month = month;
        m_day = day;
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

    //get methods


    //private methods
    public boolean isLeapYear(int year) {
        //every four years is a leap year
        if (year % 4 == 0) {
            return true;
        } else {
            return false;
        }
    }
}
