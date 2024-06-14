from functions import print_users, create_user, read_users, update_user, delete_user
from functions import print_payment_methods, create_payment_method, read_payment_methods, update_payment_method, \
    delete_payment_method


def main():
#in this part, I called the functions one by one to both execute the crud operations and print the tables
    print_users()
    print_payment_methods()

if __name__ == "__main__":
    main()
