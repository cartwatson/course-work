//Jethro Carter Watson
//CS 1410
//ASSN 6

public class Date {

    //private variables
    protected int m_year;
    protected int m_month;
    protected int m_day;

    //public add days
    public void addDays(int days) {
        //virtual by default
        //function will be overridden by definition in GregorianDate or JulianDate
    }

    //public subtract days
    public void subtractDays(int days) {
        //virtual by default
        //function will be overridden by definition in GregorianDate or JulianDate
    }

    //public boolean isLeapYear no parameter
    public boolean isLeapYear() {
        //virtual by default
        //function will be overridden by definition in GregorianDate or JulianDate
        return isLeapYear(m_year);
    }

    //protected boolean isLeapYear with parameter
    protected boolean isLeapYear(int year) {
        //virtual by default
        //function will be overridden by definition in GregorianDate or JulianDate
        return true;
    }

    //public print short date
    public void printShortDate() {
        System.out.print(m_month + "/" + m_day + "/" + m_year);
    }

    //public print long date
    public void printLongDate() {
        System.out.print(getMonthName() + " " + m_day + ", " + m_year);
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

    protected int getNumberOfDaysInYear(int year) {
        if (isLeapYear(year)) {
            //if leap year return 366
            return 365 + 1;
        } else {
            //else return 365
            return 365;
        }
    }

    protected int getNumberOfDaysInMonth(int year, int month) {
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

    protected String getMonthName(int month) {
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
