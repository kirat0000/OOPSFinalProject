'''
Scenario: Alberta Rural Hospitals (ARH) is a new healthcare provider in Alberta. To complement the
existing large-scale hospitals located in urban settings, ARH is building a network of smaller
scale mini-hospitals which target underserved rural populations. ARH has hired your company
to create a management system which is customized to meet their unique operational needs.
Your group will work on Phase 1 of the project.

#Date: Sunday, April 26, 2023
#Completed by Group 6: Puneet Rani, Jaskirat Singh and Harshit Khurana
'''

#Class Doctor

class Doctor:
    # init () to initialize the Doctor object properties
    #Attributes: doctor id, name, specialty, schedule, qualification, room number
    def __init__(self, doctor_id, name, specialty, schedule, qualification, room_number=None):
        self.__doctor_id = doctor_id
        self.__name = name
        self.__specialty = specialty
        self.__schedule = schedule
        self.__qualification = qualification
        self.__room_number = room_number
    #The getter function to return the value of the property
    def get_doctor_id(self):
        return self.__doctor_id
    
    #The setter function to set the property to a new value
    def set_doctor_id(self, doctor_id):
        self.__doctor_id = doctor_id
        
    #The getter function to return the value of the property
    def get_name(self):
        return self.__name
    
    #The setter function to set the property to a new value
    def set_name(self, name):
        self.__name = name
        
    #The getter function to return the value of the property
    def get_specialty(self):
        return self.__specialty
    
    #The setter function to set the property to a new value
    def set_specialty(self, specialty):
        self.__specialty = specialty
        
    #The getter function to return the value of the property
    def get_schedule(self):
        return self.__schedule
    
    #The setter function to set the property to a new value
    def set_schedule(self, schedule):
        self.__schedule = schedule
        
    #The getter function to return the value of the property
    def get_qualification(self):
        return self.__qualification
    
    #The setter function to set the property to a new value
    def set_qualification(self, qualification):
        self.__qualification = qualification
        
    #The getter function to return the value of the property
    def get_room_number(self):
        return self.__room_number
    
    #The setter function to set the property to a new value
    def set_room_number(self, room_number):
        self.__room_number = room_number
        
    #To format the file layout
    def format_file_layout(self):
        return f"{self.__doctor_id}_{self.__name}_{self.__specialty}_{self.__schedule}_{self.__qualification}_{self.__room_number}"
    
    #Returns a string representation of a Doctor object
    def __str__(self):
        return f"Doctor ID: {self.__doctor_id:<5}, Name: {self.__name:<20}, Specialty: {self.__specialty:<20}, Schedule: {self.__schedule:<20}, Qualification: {self.__qualification:<20}, Room Number: {self.__room_number:>9}"


#Class Patient


class Patient:
    #init () to initialize the Patient object properties
    #attributes: patient id, name, diagnosis, gender, age
    def __init__(self, patient_id=None, name=None, diagnosis=None, gender=None, age=None):
        self.__patient_id = patient_id
        self.__name = name
        self.__diagnosis = diagnosis
        self.__gender = gender
        self.__age = age
    #The getter function to return the value of the property
    def get_patient_id(self):
        return self.__patient_id

    def set_patient_id(self, patient_id):
        self.__patient_id = patient_id
        
    #The getter function to return the value of the property    
    def get_name(self):
        return self.__name
    
    #The setter function to set the property to a new value
    def set_name(self, name):
        self.__name = name
        
    #The getter function to return the value of the property
    def get_diagnosis(self):
        return self.__diagnosis
    
    #The setter function to set the property to a new value
    def set_diagnosis(self, diagnosis):
        self.__diagnosis = diagnosis
        
    #The getter function to return the value of the property
    def get_gender(self):
        return self.__gender
    
    #The setter function to set the property to a new value
    def set_gender(self, gender):
        self.__gender = gender
        
    #The getter function to return the value of the property
    def get_age(self):
        return self.__age
    
    #The setter function to set the property to a new value
    def set_age(self, age):
        self.__age = age
        
    #To format the file layout
    def format_file_layout(self):
        return f"{self.__patient_id}_{self.__name}_{self.__diagnosis}_{self.__gender}_{self.__age}"
    
    #Returns a string representation of a Doctor object
    def __str__(self):
        return f"Patient ID: {self.__patient_id:<3}, Name: {self.__name:<20}, Diagnosis: {self.__diagnosis:<20}, Gender: {self.__gender:<11}, Age: {self.__age:>3}"

    
 # DOCTOR RELATED FUNCTION
 
def doctor_menu():
    print("\nARH Management System")
    print("    Doctor's Menu\n")
    print("1 - List of Doctors")
    print("2 - Search for Doctor by ID")
    print("3 - Search for Doctor by Name/Partial Name")
    print("4 - Add new Doctor")
    print("5 - Edit Doctor Info")
    print("0 - Return to Main Menu")
    return int(input("Enter option: ")) 

'''
manage_dr(): Under this function
•	Creates an empty list for Doctor objects
•	Reads doctors file
•	Manages all the doctor menu options
•	Writes doctors file
'''

def manage_dr():
    # read list of doctors from file
    doctors = read_doctors_file()
    # initialize option with non-zero value
    option = 1
    while option !='0':
        # display menu and get user option
        option = doctor_menu()
        if option == 1:
            display_list_of_drs(doctors)
        elif option == 2:
            find_dr_by_id(doctors)
        elif option == 3:
            match_dr_by_name(doctors)
        elif option == 4:
            add_dr_to_list(doctors)
        elif option == 5:
            edit_dr_info(doctors)
    # write updated list of doctors back to file
    write_drs_list_to_file(doctors)    
   
'''
read_doctors_file(): This function
•	Reads data from file “doctors.txt”
•	Creates Doctor objects for each doctor record
•	Appends object to doctor list
'''

def read_doctors_file():
    doctors = []
    with open("doctors.txt", "r") as file:
        for line in file:
            data = line.strip().split("_")
            doctor = Doctor(doctor_id=data[0], name=data[1], specialty=data[2], schedule=data[3],
                            qualification=data[4], room_number=data[5])
            doctors.append(doctor)
    return doctors

'''find_dr_by_id(): This function
•	Receives the doctor ID to locate
•	Searches the list of Doctor objects for a specified doctor with specified ID
•	If found, prints and returns Doctor object
•	Otherwise returns -1.
'''
         
def find_dr_by_id(doctors):
    doctor_id = input("Enter the Doctor ID: ")
    doctors_data= read_doctors_file()
    for doctor in doctors_data:
        if doctor.get_doctor_id() == doctor_id:
            print(doctor)
            return doctor
    print("Doctor with ID", doctor_id, "not found.")
    return -1
        
'''
match_dr_by_name(): This function:
•	Asks the user to enter the name/partial name to match
•	Searches the list of Doctor objects for a name that contains the name requested
•	Displays each Doctor objects that match criteria
•	If no match, prints not found message.

'''
def match_dr_by_name(doctors):
    name = input("Enter the Doctor Name or Partial Name: ")
    match_found = 0
    for doctor in doctors:
        if name.lower() in doctor.get_name().lower():
            print(doctor)
            match_found = 1
    if match_found == 0:
        print("No doctors found with name containing", name)
        
'''
display_list_of_drs(): This function
Displays all the Doctors’ information(attributes) in doctors list in the format specified in the Sample run
'''
def display_list_of_drs(doctor_ist):
    print(f"{'ID' : <5}{'Name' : <20}{'Specialist': <20}{'Schedule' : <15}{'Qualification' : <20}{'Room Nbr' :>8}")
    doctors_data = read_doctors_file()
    for doctor in doctors_data:
        print(doctor.__str__())               

'''
write_drs_list_to_file(): This function:	
Writes “doctors.txt” file from the list of Doctor objects, maintaining correct formatting
'''                
def write_drs_list_to_file(doc_obj_list):
    doc_file = open("doctors.txt", "w")
    doc_file.writelines([str.format_file_layout() + "\n" for str in doc_obj_list])
    doc_file.close()        

'''
add_dr_to_list(): This function	
•	Asks the user to enter a doctor id
•	Checks to see if that doctor ID exists in list of Doctor objects
•	If it does exist, prints error message
•	Otherwise, Asks the user to enter the rest of the doctor information (attributes), creates a new Doctor object (with user-entered doctor information) and adds it to the doctors list
'''
def add_dr_to_list(doctors):
    doctor_id = input("Enter Doctor ID: ")
    for doctor in doctors:
        if doctor.get_doctor_id() == doctor_id:
            print("Doctor with ID", doctor_id, "already exists - cannot add")
            return -1
    name = input("Enter Doctor Name: ")
    specialty = input("Enter Doctor Specialty: ")
    schedule = input("Enter Doctor Schedule: ")
    qualification = input("Enter Doctor Qualification: ")
    room_number = input("Enter Doctor Room Number: ")
    doctor = Doctor(doctor_id=doctor_id, name=name, specialty=specialty, schedule=schedule,
                    qualification=qualification, room_number=room_number)
    doctors.append(doctor)
    print("Doctor with id ",doctor_id," added successfully.")
    
'''
edit_dr_info(): This function:
•	Asks the user for the doctor ID to edit
•	Checks to see if that doctor ID exists in list of Doctor objects
•	If it does not exist, prints an error message
•	Otherwise, prompts for new values and updates the Doctor object with new values
•	Displays doctor list
'''

def edit_dr_info(doctors):
    doctor_id = input("Enter Doctor ID to edit: ")
    doctor_found = '0'
    for doctor in doctors:
        if doctor.get_doctor_id() == doctor_id:
            doctor_found = '1'
            print(f"{'ID' : <5}{'Name' : <20}{'Specialist': <20}{'Schedule' : <15}{'Qualification' : <20}{'Room Nbr' : >8}")
            print(doctor.__str__())

            
            doctor.name = input("Enter New Name: ")
            doctor.speciality = input("Enter New Speciality in: ")
            doctor.schedule = input("Enter New Schedule: ")
            doctor.qualification = input("Enter New Qualification: ")
            doctor.room_number = input("Enter New Room Number: ")
            
            write_drs_list_to_file(doctor)
            
            print(f"Doctor with ID {doctor.doctor_id} successfully modified.")
            print("Doctor info updated successfully.")
            break
    
    if doctor_found=='0':
        print("Doctor with ID", doctor_id, "not found.")
        print(display_list_of_drs(doctors))
                   
        
        
        
# PATIENT RELATED FUNCTION        

def patient_menu():
    print("\nARH Management System")
    print("    Patient's Menu\n")
    print("1 - List of Patients")
    print("2 - Search for Patient by ID")
    print("3 - Search for Patient by Name/Partial Name")
    print("4 - Add new Patient")
    print("5 - Edit Patient Info")
    print("0 - Return to Main Menu")
    return int(input("Enter option: "))

'''
read_patients_file()	•	Reads data from file “patients.txt”
•	Creates Patient objects for each patient record
•	Appends object to patients list
'''

def read_patients_file():
    patients = []
    with open("patients.txt", "r") as f:
        for line in f:
            data = line.strip().split("_")
            patient = Patient(patient_id=data[0], name=data[1], diagnosis=data[2], gender=data[3], age=data[4])
            patients.append(patient)
    return patients

'''
write_patients_list_to_file(): This function	
Writes “patients.txt” file from the 
list of Patient objects, maintaining correct formatting'''
def write_patients_list_to_file(patients):
    with open("patients.txt", "w") as f:
        for patient in patients:
            f.write(patient.format_file_layout() + "\n")

'''
display_list_of_patients(): This function
Displays all the Patients’ information(attributes)
in patients list in the format specified in the Sample run
'''
def display_list_of_patients(patients):
    for patient in patients:
        print(patient)

'''
find_patient_by_id(): This function	
•	Receives the Patient ID to locate
•	Searches the list of Patient objects for a patient with specified ID
•	If found, prints and returns Patient object
•	Otherwise returns -1.
'''
def find_patient_by_id(patients):
    patient_id = input("Enter the Patient ID: ")
    for patient in patients:
        if patient.get_patient_id() == patient_id:
            print(patient)
            return patient
    print("Patient with ID", patient_id, "not found.")
    return -1

def match_patient_by_name(patients):
    name = input("Enter the Patient Name or Partial Name: ")
    match_found = False
    for patient in patients:
        if name.lower() in patient.get_name().lower():
            print(patient)
            match_found = True
    if not match_found:
        print("No patients found with name containing", name)
'''
add_patient_to_list(): This function	
Asks the user to enter a patient ID
'''
def add_patient_to_list(patients):
    patient_id = input("Enter Patient ID: ")
    for patient in patients:
        if patient.get_patient_id() == patient_id:
            print("Patient with ID", patient_id, "already exists.")
            return -1
    name = input("Enter Patient Name: ")
    diagnosis = input("Enter Patient Diagnosis: ")
    gender = input("Enter Patient Gender: ")
    age = input("Enter Patient Age: ")
    patient = Patient(patient_id=patient_id, name=name, diagnosis=diagnosis, gender=gender, age=age)
    patients.append(patient)
    print("Patient added successfully.")

'''
edit_patient_info(): This function	
•	Asks the user for the Patient ID to edit
•	Checks to see if that Patient ID exists in list of Patient objects
•	If it does not exist, prints an error message
•	Otherwise, prompts for new values and updates the Patient object with new values
•	Displays patient list
'''
def edit_patient_info(patients):
    patient_id = input("Enter Patient ID to edit: ")
    for patient in patients:
        if patient.get_patient_id() == patient_id:
            name = input("Enter new Name (leave blank to keep current value '" + patient.get_name() + "'): ")
            if name:
                patient.set_name(name)
            diagnosis = input("Enter new Diagnosis (leave blank to keep current value '" + patient.get_diagnosis() + "'): ")
            if diagnosis:
                patient.set_diagnosis(diagnosis)
            gender = input("Enter new Gender (leave blank to keep current value '" + patient.get_gender() + "'): ")
            if gender:
                patient.set_gender(gender)
            age = input("Enter new Age (leave blank to keep current value '" + patient.get_age() + "'): ")
            if age:
                patient.set_age(age)
            print("Patient info updated successfully.")
            return
    print("Patient with ID", patient_id, "not found.")
    
    

'''
Menu Functions:
menu():This function
•	Receives a menu name and menu dictionary
•	Displays specified menu,
•	Accepts menu selection from user until valid selection is entered
•	Returns user’s valid selection
'''

def main_menu():
    print("\nARH Management System")
    print("    Main Menu\n")
    print("1 - Doctor's Menu")
    print("2 - Patient's Menu")
    print("0 - Exit")
    return int(input("Enter option: "))




# The main function that control the flow of the program and work according to the question 

# Main function that controls the flow of the program
def main():
    # Read the doctors and patients data from files
    doctors = read_doctors_file()
    patients = read_patients_file()

    # Initialize the option variable to -1
    option = -1

    # Run the main menu until the user chooses to exit (option 0)
    while option != 0:
        # Display the main menu and get the user's choice
        option = main_menu()

        # If the user chooses the doctor menu
        if option == 1:
            # Initialize the doctor_option variable to -1
            doctor_option = -1

            # Run the doctor menu until the user chooses to go back (option 0)
            while doctor_option != 0:
                # Display the doctor menu and get the user's choice
                doctor_option = doctor_menu()

                # If the user chooses to display the list of doctors
                if doctor_option == 1:
                    display_list_of_drs(doctors)

                # If the user chooses to search for a doctor by ID
                elif doctor_option == 2:
                    find_dr_by_id(doctors)

                # If the user chooses to search for a doctor by name
                elif doctor_option == 3:
                    match_dr_by_name(doctors)

                # If the user chooses to add a new doctor to the list
                elif doctor_option == 4:
                    add_dr_to_list(doctors)

                # If the user chooses to edit a doctor's information
                elif doctor_option == 5:
                    edit_dr_info(doctors)

                # If the user chooses an invalid option
                elif doctor_option != 0:
                    print("Invalid option. Please try again.")

        # If the user chooses the patient menu
        elif option == 2:
            # Initialize the patient_option variable to -1
            patient_option = -1

            # Run the patient menu until the user chooses to go back (option 0)
            while patient_option != 0:
                # Display the patient menu and get the user's choice
                patient_option = patient_menu()

                # If the user chooses to display the list of patients
                if patient_option == 1:
                    display_list_of_patients(patients)

                # If the user chooses to search for a patient by ID
                elif patient_option == 2:
                    find_patient_by_id(patients)

                # If the user chooses to search for a patient by name
                elif patient_option == 3:
                    match_patient_by_name(patients)

                # If the user chooses to add a new patient to the list
                elif patient_option == 4:
                    add_patient_to_list(patients)

                # If the user chooses to edit a patient's information
                elif patient_option == 5:
                    edit_patient_info(patients)

                # If the user chooses an invalid option
                elif patient_option != 0:
                    print("Invalid option. Please try again.")

        # If the user chooses an invalid option
        elif option != 0:
            print("Invalid option. Please try again.")

    # Display a message indicating the program is exiting
    print("Exiting the system...")

# main statement to run the whole program  
if __name__ == '__main__':
    main()
