//Jethro Carter Watson
//CS 1410
//ASSN 5

public class JulianDate {
    //declare private variables
    private int m_day = 1;
    private int m_month = 1;
    private int m_year = 1;

    //default constructor
    JulianDate() {
        //variables are initialized as part of class
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

    //public print short date
    public void printShortDate() {
        System.out.print(m_month + "/" + m_day + "/" + m_year);
    }

    //public print long date
    public void printLongDate() {
        System.out.print(getMonthName() + " " + m_day + ", " + m_year);
    }

    //get methods
    public String getMonthName() {
        //return month name as a string
        //break statements aren't needed as return statements are used
        switch (m_month) {
            case 1:
                return "January";
            case 2:
                return "February";
            case 3:
                return "March";
            case 4:
                return "April";
            case 5:
                return "May";
            case 6:
                return "June";
            case 7:
                return "July";
            case 8:
                return "August";
            case 9:
                return "September";
            case 10:
                return "October";
            case 11:
                return "November";
            case 12:
                return "December";
            default:
                return "invalid month";
        }
    }

    public int getMonth() {
        return m_month;
    }

    public int getYear() {
        return m_year;
    }

    public int getDayOfMonth() {
        return m_day;
    }

    //private methods
    private boolean isLeapYear(int year) {
        //every four years is a leap year
        if (year % 4 == 0) {
            return true;
        } else {
            return false;
        }
    }

    private int getNumberOfDaysInMonth(int year, int month) {
        switch (month) {
            //jan, mar, jul, aug, oct, dec
            case 1:
            case 3:
            case 5:
            case 7:
            case 8:
            case 10:
            case 12:
                return 31;
            //apr, jun, sep, nov
            case 4:
            case 6:
            case 9:
            case 11:
                return 30;
            //feb
            case 2:
                //check for leap year
                if (isLeapYear(year)) {
                    return 29;
                } else {
                    return 28;
                }
                //intelliJ didn't like me not having a default
            default:
                return 0;
        }
    }

    private int getNumberOfDaysInYear(int year) {
        if (isLeapYear(year)) {
            //if leap year return 366
            return 365 + 1;
        } else {
            //else return 365
            return 365;
        }
    }

    private String getMonthName(int month) {
        //return month name as a string
        //break statements aren't needed as return statements are used
        switch (month) {
            case 1:
                return "January";
            case 2:
                return "February";
            case 3:
                return "March";
            case 4:
                return "April";
            case 5:
                return "May";
            case 6:
                return "June";
            case 7:
                return "July";
            case 8:
                return "August";
            case 9:
                return "September";
            case 10:
                return "October";
            case 11:
                return "November";
            case 12:
                return "December";
            //intelliJ really has something against not having a default
            default:
                return "Invalid month";
        }
    }
}
