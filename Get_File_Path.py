
def get_file_path():
    # Getting user input
    print("Enter the folder number [Network_Failure-1,Recharge_Issue-2,Service_Failure-3] :- ")
    folder_number = input()
    print("Enter voice clip number :- ")
    file_number = input()

    if int(folder_number) == 1:
        folder_name = 'Network_Failure'
        if int(file_number)<10:
            file_name = 'Network_Failure_0{}'.format(file_number)
        else:
            file_name = 'Network_Failure_{}'.format(file_number)
        return folder_name,file_name

    elif int(file_number) == 2:
        folder_name = 'Recharge_Issue'
        if int(file_number)<10:
            file_name = 'Recharge_Issue_0{}'.format(file_number)
        else:
            file_name = 'Recharge_Issue_{}'.format(file_number)
        return folder_name,file_name

    elif int(file_number) == 3:
        folder_name = 'Service_Failure'
        file_name = 'Recording ({})'.format(file_number)
        return folder_name,file_name

    else:
        print("Inputs are wrong")

    