import pprint
import sys
# sys.path.append('..')
# pprint(sys.path)
from services.connections import cursor_command
import datetime


# Model: Employee
class Employee:
    def __init__(self, f_name, l_name, telegram_id, company='', specialty='', email='', phone=''):
        self.__employee_id = 0
        self.f_name = f_name
        self.l_name = l_name
        self.company = company
        self.specialty = specialty
        self.email = email
        self.phone = phone
        self.telegram_id = telegram_id
        self.__empl_info = []
        self.__sql_command = ''
        self.__sql_param = ()

    def get_empl_id(self):
        try:
            int(self.__employee_id)
            if self.__employee_id == 0:
                print(f"[INFO] employee_id = {self.__employee_id}. I dont have the employee information")
                return None
            return self.__employee_id
        except Exception as _ex:
            print(f"[INFO] employee_id = {self.__employee_id}; \nException:", _ex)

    def init_empl_id(self):
        self.__employee_id = 0

    def add_employee(self):
        try:
            self.__sql_command = """INSERT INTO employee (
                                            f_name,
                                            l_name,
                                            company,
                                            specialty,
                                            email,
                                            phone,
                                            telegram_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            self.__sql_param = (self.f_name, self.l_name, self.company, self.specialty, self.email, self.phone,
                                self.telegram_id)

            res = cursor_command('add', self.__sql_command, self.__sql_param)
            if res is False:
                print(f'[INFO:] Employee {self.f_name} {self.l_name} with telegram_id: {self.telegram_id} do not added')
                return False
            else:
                print(f'[INFO:] Employee {self.f_name} {self.l_name} with telegram_id: {self.telegram_id} was added')
                return True
        except Exception as _ex:
            print(f'[ERROR]: {_ex}')

    def delete_employee(self):
        if self.__employee_id != 0:
            self.__sql_command = """DELETE FROM employee WHERE employee_id = %s"""
            self.__sql_param = (self.__employee_id,)

            cursor_command('del', self.__sql_command, self.__sql_param)
        else:
            print('[INFO] We have no user with employee_id = 0')

    def get_info_of_employee(self):
        try:
            print('111111')
            self.__sql_command = """SELECT * FROM employee WHERE f_name = %s AND l_name = %s AND telegram_id = %s"""
            self.__sql_param = (self.f_name, self.l_name, self.telegram_id)

            self.__empl_info = cursor_command('get', self.__sql_command, self.__sql_param)

            self.__employee_id = self.__empl_info[0][0]
            return self.__empl_info
        except Exception as _ex:
            print(f'[ERROR]: sourse: models/get_info_of_employee;\n {_ex} ')
            return None


# Model: Work table
class W_table:
    def __init__(self, fk_employee_id: int, w_day: datetime.date, w_city: str, name_project: str, discr_work: str,
                 notes: str, start_shift: datetime.time, end_shift: datetime.time, shift_time: datetime.time):
        self.__w_table_id = 0
        self.fk_employee_id = fk_employee_id
        self.w_day = w_day                              # Data of the working day
        self.w_city = w_city                            # city where the job was
        self.name_project = name_project                # Name of the project
        self.descr_work = discr_work                    # Description of the project
        self.notes = notes                              # Notes
        self.start_shift = start_shift                  # Start time of the shift
        self.end_shift = end_shift                      # Finish time of the shift
        self.shift_time = shift_time                    # Working Shift time
        self.sel_w_day_from = datetime.date.today()
        self.sel_w_day_to = datetime.date.today()
        self.del_w_day_from = datetime.date.today()
        self.del_w_day_to = datetime.date.today()
        self.w_table_info = []
        self.__sql_command = ''
        self.__sql_param = ()

    def add_w_table(self):
        self.__sql_command = """INSERT INTO w_table (
                                fk_employee_id,
                                w_day,
                                w_city,
                                name_project,
                                discr_work,
                                notes,
                                start_shift,
                                end_shift,
                                shift_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        self.__sql_param = (
            self.fk_employee_id, self.w_day, self.w_city, self.name_project, self.descr_work, self.notes,
            self.start_shift[0], self.end_shift[0], self.shift_time[0])

        cursor_command('add', self.__sql_command, self.__sql_param)

    def delete_w_table(self):
        self.__sql_command = """ DELETE FROM w_table WHERE
                                    fk_employee_id = %s AND w_day >= %s AND w_day <= %s"""
        self.__sql_param = (self.fk_employee_id, self.del_w_day_from, self.del_w_day_to)
        cursor_command('del', self.__sql_command, self.__sql_param)

    def get_info_of_the_w_days(self):
        self.__sql_command = """ SELECT * FROM w_table WHERE
                                    fk_employee_id = %s AND w_day >= %s AND w_day <= %s"""

        self.__sql_param = (self.fk_employee_id, self.sel_w_day_from, self.sel_w_day_to)

        self.w_table_info = cursor_command('get', self.__sql_command, self.__sql_param)
        return self.w_table_info

# if __name__ == '__main__':
#     test_empl = Employee(f_name='Dmitry', l_name='Stepanov')
#     test_empl.get_info_of_employee()
