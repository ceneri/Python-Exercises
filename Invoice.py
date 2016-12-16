#Cesar Neri
#December 16, 2016

#Exercise 11-1 From Murach's Python programming Book



#!/usr/bin/env python3

from datetime import datetime
from datetime import date
from datetime import timedelta


#Gets a valid date from the user
def get_invoice_date():
    #Initialize todays datetime object
    today = date.today()
    #todays_date = date(today.year, today.month, today.day)

    #get valid invoice datetime obj
    while True:
        date_str = input("Enter the Invoice date (MM/DD/YYYY): ")
        try:
            invoice_datetime = datetime.strptime(date_str, "%m/%d/%Y")
            invoice_date = date(invoice_datetime.year, invoice_datetime.month, invoice_datetime.day)
        except ValueError:
            print("Invalid date format. Please try again.")
            continue

        if invoice_date > today:
            print("Invoice date must be today or earlier. Please try again.")
        else:
            return invoice_date

def main():

    # display a title
    print("The Invoice program")
    print()

    choice = "y"
    while choice == "y":
    
        # get user entry
        invoice_date = get_invoice_date()

        #get todays date
        today = date.today()

        #get date 30 days apart
        due_date = invoice_date + timedelta(days=30)

        #print data
        date_format = "%B %d, %Y"
        print()
        print("Invoice Date: " + invoice_date.strftime(date_format))
        print("Due Date: \t" + due_date.strftime(date_format))
        print("Current Date: " + today.strftime(date_format))

        # determine discount percent
        print()
        if today < due_date:
            print("Invoice is " + str((today - due_date).days) + " day(s) away.")
        elif today > due_date:
            print("Invoice is " + str((due_date - today).days * -1) + " day(s) overdue.")
        else:
            print("Invoice is due today!")

        print()
        choice = input("Continue? (y/n): ")    
        print()
    
    print("Bye")

if __name__ == "__main__":
    main()
