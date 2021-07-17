
from GymManager import GymManager
from Customer import Customer
from Package import Package


gymManager = GymManager()
print("\n")
print("   *****Simple Gym Management System*****")
print("Hello Admin, please select a choice from the menu")


def menu():
    print("1. Add Customer")
    print("2. Add Package")
    print("3. Show all packages")
    print("4. Show all customers")
    print("5. Find customer by name")
    print("6. Add Subscription")
    print("7. Add Payment")
    print("8. Show this menu again")
    print("\nEnter You Choice: ")

menu()

while(True):
    input1 = int(input())
    if input1 == 1:
        name = input("Enter customer's name - ")
        phoneNo = input("Enter customer's phone no. - ")
        joinDate = input("Enter joining date - ")
        customer = Customer(name, phoneNo, joinDate)
        gymManager.addCustomer(customer)

    elif input1 == 2:
        type = input("Enter package type - ")
        facilities = input("Enter facilities - ")
        cost = input("Enter package cost - ")
        package = Package(type, facilities, cost)
        gymManager.addPackage(package)

    elif input1 == 3:
        print("PackageID\tType\tFacilities\tCost")
        for pkgId in gymManager.packages.keys():
            package = gymManager.packages[pkgId]
            packageId = pkgId
            type = package.getType()
            facilities = package.getFacilities()
            cost = package.getCost()
            print (str(packageId) + "\t" + type + "\t" + facilities + "\t" + str(cost))

    elif input1 == 4:
        print("CustomerID\tName\tPhone\tJoining Date")
        for cusId in gymManager.customers.keys():
            customer = gymManager.customers[cusId]
            customerId = cusId
            name = customer.getName()
            phoneNo = customer.getPhoneNo()
            joinDate = customer.getJoiningDate()
            print(str(customerId) + "\t" + name + "\t" + phoneNo + "\t" + joinDate)

    elif input1 == 5:
        name = input("Enter customer name - ")
        customerId = -1
        for cusId in gymManager.customers.keys():
            customer = gymManager.customers[cusId]
            if customer.getName() == name:
                print(customer)
                customerId = cusId
                break;
        if customerId == -1:
            print("Customer with name - {0} not found".format(name))
        else:
            packageDict = gymManager.subscriptions.get(customerId)
            print("Customer found", gymManager.customers[customerId])
            if packageDict != {}:
                print("Subscribed to",)
                for pkgId in packageDict.keys():
                    print(gymManager.packages[pkgId], "for {0} months".format(gymManager.subscriptions[customerId][packageId]))
            else:
                print("No subscription found for this customer")

    elif input1 == 6:
        name = input("Enter customer name - ")
        customerId = -1
        for cusId in gymManager.customers.keys():
            customer = gymManager.customers[cusId]
            if customer.getName() == name:
                print(customer)
                customerId = cusId
                break;
        if customerId == -1:
            print("Customer with name - {0} not found.".format(name))
            print("Try adding a new customer.")
        else:
            print("Customer found", gymManager.customers[customerId])
            if gymManager.packages.keys():
                for pkgId in gymManager.packages.keys():
                    print (pkgId, gymManager.packages[pkgId])
                packageId = int(input("Select a package: "))
                if packageId > max(gymManager.packages.keys()):
                    print ("Please select a valid package.")
                else:
                    months = int(input("Enter no. of months"))
                    gymManager.addSubscription(gymManager.customers[customerId], gymManager.packages[packageId], months)
                    print("Subscription added.")
            else:
                print("No package exists. Try adding a package first.")

    elif input1 == 7:
        name = input("Enter customer name - ")
        customerId = -1
        for cusId in gymManager.customers.keys():
            customer = gymManager.customers[cusId]
            if customer.getName() == name:
                print(customer)
                customerId = cusId
                break;
        if customerId == -1:
            print("Customer with name - {0} not found.".format(name))
            print("Try adding a new customer.")
        else:
            print("Customer found", gymManager.customers[customerId])
            if gymManager.packages.keys():
                for pkgId in gymManager.packages.keys():
                    print(pkgId, gymManager.packages[pkgId])
                packageId = int(input("Select a package"))
                if packageId > max(gymManager.packages.keys()):
                    print("Please select a valid package.")
                else:
                    if gymManager.subscriptions[customerId][packageId] > 0:
                        customer = gymManager.customers[customerId]
                        package = gymManager.packages[packageId]
                        gymManager.addPayment(customer, package, package.getCost())
                        print( "Payment added. Subscription expires in {0} months.".format(gymManager.subscriptions[customerId][packageId]))
    elif input1 == 8:
        menu()
    elif input1 == 9:
        gymManager.save()
        exit(0)
    else:
        print("Please enter a valid number")
    menu()
 
