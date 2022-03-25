import datetime
import sys


class bcolors:
    '''
    Module with colors
    '''
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Note:
    '''
    Class of Note with all needed information
    '''
    def __init__(self, mem, date, tag):
        '''
        The main function
        '''
        self.mem = mem
        self.date = date
        self.tag = tag
        self.all_info = [mem, date, tag]
        self.all_tog = [mem, date] + tag

    def match(self, to_find):
        '''
        The function finds matches in all info
        '''
        if to_find in self.all_tog:
            return True
        else:
            return False


class Notebook():
    '''
    Class of Notebook with all needed functions of program
    '''
    def __init__(self):
        '''
        Main function
        '''
        self.notes = list()

    def create_note(self, mem, date, tag):
        '''
        The function creates new note
        '''
        self.notes.append(Note(mem, date, tag))

    def show_notes(self):
        '''
        The function returns all notes in Notebook
        '''
        return self.notes

    def search(self, filter):
        '''
        The function search in all info some filter
        '''
        results = list()
        counter_1 = 1
        for one_note in self.notes:
            if one_note.match(filter):
                results.append((counter_1, one_note))
            counter_1 += 1
        return results

    def modify_memo(self, note_id, memo):
        '''
        The function enable user to modify memo in the note
        '''
        self.notes[note_id - 1].mem = memo
        self.notes[note_id - 1].date = datetime.date.today()
        self.notes[note_id - 1].all_tog = [memo, self.notes[note_id - 1].date] + \
        self.notes[note_id - 1].tag

    def modify_tags(self, note_id, tag):
        '''
        The function enable user to modify tag in the note
        '''
        self.notes[note_id - 1].tag = tag
        self.notes[note_id - 1].date = datetime.date.today()
        self.notes[note_id - 1].all_tog = [self.notes[note_id - 1].mem,
                                          self.notes[note_id - 1].date] + tag


class Menu():
    '''
    Class Menu includes static methods and interaction with user
    '''
    @staticmethod
    def try_if_okay(notebook):
        '''
        The function checks if input of user was int and if it is less than len of notes
        '''
        line = ' - '
        flag_ok = True
        while flag_ok:
            try:
                note_num = int(input(bcolors.OKCYAN + bcolors.BOLD +
                            '\nPlease enter number of the note \
to modify(starts from 1): ' + bcolors.ENDC + bcolors.HEADER + '\n>>> ' +
                            bcolors.ENDC))
                if len(notebook.show_notes()) >= int(note_num) and\
                    int(note_num) > 0:
                        flag_ok = False
                else:
                    print(line * 17 + bcolors.HEADER + bcolors.BOLD +
                        '\nYou entered something wrong :(' + bcolors.ENDC)
            except ValueError:
                print(line * 17 + bcolors.HEADER + bcolors.BOLD +
                    '\nYou entered something wrong :(' + bcolors.ENDC)
                continue
        flag_ok = True
        return note_num

    @staticmethod
    def try_if_enough(notebook):
        '''
        The function checks if notebook have some notes or it is empty
        '''
        if len(notebook.show_notes()) == 0:
            print(bcolors.OKCYAN + bcolors.BOLD +
                "\nSorry, you don't have any notes :(\nFirst you have \
to create it!\n" + bcolors.ENDC)
            notebook_1 = notebook
            Menu().menu(notebook_1)
        else:
            return True

    def menu(self, notebook):
        '''
        The function have all interaction with user
        '''
        line = ' - '
        command_user = input(line * 17 + bcolors.BOLD + bcolors.HEADER +
                    '\nYou can see all possible options, please enter one\n' +
                     bcolors.ENDC + line * 17 + '\n' + bcolors.OKCYAN +
                     '+\tcreate_note\n+\tshow_notes' +
                     '\n+\tsearch\n+\tmodify_tags\n+\tmodify_memo\n+\tstop\n' +
                     bcolors.ENDC + line * 17 + bcolors.HEADER +
                     '\n>>> ' + bcolors.ENDC)

        if command_user == 'create_note':
            mem = input(line * 17 + bcolors.OKCYAN + bcolors.BOLD +
                    '\nPlease enter a name of the memo:' +
                    bcolors.ENDC + bcolors.HEADER + ' \n>>> ' + bcolors.ENDC)
            tag = [input(bcolors.OKCYAN + bcolors.BOLD +
                'Please enter one tag:' + bcolors.ENDC + bcolors.HEADER +
                ' \n>>> ' + bcolors.ENDC)]
            flag = True
            while flag:
                tag_1 = input(bcolors.OKCYAN + 'Do you want ' + bcolors.HEADER +
                        bcolors.BOLD + '(1)to add one more tag' +
                        bcolors.OKCYAN + ' or ' + bcolors.HEADER +
                        bcolors.BOLD + '(2)to continue?' + bcolors.OKCYAN +
                        bcolors.BOLD + '\nPlease enter 1 or 2: ' +
                        bcolors.ENDC + bcolors.HEADER + ' \n>>> ' +
                        bcolors.ENDC)
                if tag_1 == '1':
                    tag_to_add = input(bcolors.OKCYAN + bcolors.BOLD +
                    'Please enter one tag:' + bcolors.ENDC + bcolors.HEADER +
                    ' \n>>> ' + bcolors.ENDC)
                    tag.append(tag_to_add)
                elif tag_1 == '2':
                    flag = False
                else:
                    print(bcolors.HEADER + bcolors.BOLD +
                    '\nYou entered something wrong :(\n' + bcolors.ENDC)
            date = str(datetime.date.today())
            notebook.create_note(mem, date, tag)
            flag = True

        elif command_user == 'show_notes':
            if Menu().try_if_enough(notebook):
                flazhok = True
                while flazhok:
                    option = input(bcolors.HEADER + 'Do you want to see ' +
                            bcolors.OKCYAN + bcolors.BOLD + '(1)all notes' +
                            bcolors.HEADER + ' or ' + bcolors.OKCYAN +
                            '(2)particular one' + bcolors.HEADER + ' or ' +
                            bcolors.OKCYAN + '(3)just number of notes' +
                            bcolors.HEADER + '?\n' + bcolors.ENDC +
                            line * 17 + bcolors.HEADER + bcolors.BOLD +
                            '\nPlease enter 1, 2 or 3: ' + bcolors.ENDC)
                    if option == '1':
                        all_notes = notebook.show_notes()
                        counter = 1
                        print(line * 17)
                        for elem in all_notes:
                            print(bcolors.OKCYAN + '\n-\t' + '№ ' +
                            str(counter) + ' Name memo: ' + str(elem.mem) +
                            ' Date: ' + str(elem.date) +
                            ' Tags: ' + ', '.join(elem.tag) + bcolors.ENDC)
                            counter += 1
                        flazhok = False
                    elif option == '2':
                        note_id = Menu().try_if_okay(notebook)
                        elem = notebook.show_notes()[note_id - 1]
                        print(line * 17 + bcolors.OKCYAN + '\n-\t' + '№ ' +
                        str(note_id) + ' Name memo: ' + str(elem.mem) +
                        ' Date: ' + str(elem.date) + ' Tags: ' +
                        ', '.join(elem.tag) + bcolors.ENDC)
                        flazhok = False
                    elif option == '3':
                        print(line * 17 + bcolors.OKCYAN +
                            '\n\nNotebook consists of ' +
                             str(len(notebook.show_notes())) +
                             ' notes\n' + bcolors.ENDC)
                        flazhok = False
                    else:
                        print(line * 17 + bcolors.BOLD + bcolors.OKCYAN +
                              "\n\nSorry you entered something wrong :(\nPlease \
try again!\n" + bcolors.ENDC)
                flazhok = True
            else:
                notebook_1 = notebook
                Menu().menu(notebook_1)

        elif command_user == 'search':
            if Menu().try_if_enough(notebook):
                to_search = input(line * 17 + bcolors.HEADER +
                            '\nPlease enter ' + bcolors.OKCYAN + bcolors.BOLD +
                            'memo, date(like this 2022-03-25) or tag' +
                            bcolors.ENDC + bcolors.HEADER +
                            ' you would like to search:\n' + bcolors.HEADER +
                            '>>> ' + bcolors.ENDC)
                list_with_res = notebook.search(to_search)
                if len(list_with_res) == 0:
                    print(bcolors.OKCYAN + bcolors.BOLD +
                        "\n\nSorry, we haven't found any matches :(\n\n" +
                         bcolors.ENDC)
                else:
                    for elem in list_with_res:
                        print(bcolors.OKCYAN + '\n-\t' + '№ ' + str(elem[0]) +
                            ' Name memo: ' + str(elem[1].mem) + ' Date: ' +
                             str(elem[1].date) + ' Tags: ' +
                             ', '.join(elem[1].tag) + bcolors.ENDC)
            else:
                notebook_1 = notebook
                Menu().menu(notebook_1)

        elif command_user == 'modify_tags':
            if Menu().try_if_enough(notebook):
                note_num = Menu().try_if_okay(notebook)
                flag_4 = True
                tags_to_mod = [input(bcolors.OKCYAN + bcolors.BOLD +
                                'Please enter one tag:' + bcolors.ENDC +
                                bcolors.HEADER + ' \n>>> ' + bcolors.ENDC)]
                while flag_4:
                    tag_1 = input(bcolors.OKCYAN + '\nDo you want ' +
                            bcolors.HEADER + bcolors.BOLD +
                              '(1)to add one more tag' + bcolors.OKCYAN +
                              ' or ' + bcolors.HEADER + bcolors.BOLD +
                              '(2)to continue?' + bcolors.OKCYAN +
                              bcolors.BOLD + '\nPlease enter 1 or 2: ' +
                              bcolors.ENDC + bcolors.HEADER + ' \n>>> ' +
                              bcolors.ENDC)
                    if tag_1 == '1':
                        tag_to_add = input(bcolors.OKCYAN + bcolors.BOLD +
                                    'Please enter one tag:' + bcolors.ENDC +
                                     bcolors.HEADER + ' \n>>> ' + bcolors.ENDC)
                        tags_to_mod.append(tag_to_add)
                    elif tag_1 == '2':
                        flag_4 = False
                    else:
                        print(line * 17 + bcolors.BOLD + bcolors.OKCYAN +
                            "\n\nSorry you entered something wrong \
:(\nPlease try again!\n" + bcolors.ENDC)
                flag_4 = True
                notebook.modify_tags(note_num, tags_to_mod)
            else:
                notebook_1 = notebook
                Menu().menu(notebook_1)

        elif command_user == 'modify_memo':
            if Menu().try_if_enough(notebook):
                note_num_mem = Menu().try_if_okay(notebook)
                memo_to_mod = input(bcolors.OKCYAN + bcolors.BOLD +
                                'Please enter one memo:' + bcolors.ENDC +
                                 bcolors.HEADER + ' \n>>> ' + bcolors.ENDC)
                notebook.modify_memo(note_num_mem, memo_to_mod)
            else:
                notebook_1 = notebook
                Menu().menu(notebook_1)

        elif command_user == 'stop':
            print(line * 17 + bcolors.OKCYAN + '\nThank you for good \
time together :)\n' + bcolors.ENDC + line * 17)
            sys.exit()

        else:
            print(line * 17 + bcolors.BOLD + bcolors.HEADER + "\nSorry, we \
don't have such a command :(\nTry again!" + bcolors.ENDC)
            notebook_1 = notebook
            Menu().menu(notebook_1)


def main():
    '''
    Main function to start program
    '''
    notebook = Notebook()
    flag = True
    while flag:
        Menu().menu(notebook)
main()
