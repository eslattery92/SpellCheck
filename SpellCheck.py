import arcpy
import enchant
from collections import Counter
import difflib

arcpy.env.workspace = "C:/Schools/Schools.gdb"

fc = "C:/Schools/Schools.gdb/NJ_Towns"

fields = [x for x in arcpy.ListFields(fc) if x.type == 'String']

included_fields = []


def find_fields():
    for field in fields:
        with arcpy.da.SearchCursor(fc, [field.name]) as cursor:
            for row in cursor:
                print row[0]
        user_q = raw_input("Do you want to include " + field.name + " in the Spell Check?")
        if user_q.title() == "Yes":
            included_fields.append(field.name)
        elif user_q.title() == "No":
            pass

    check_spelling()


used_words = []
change_words = {}


def check_spelling():
    d = enchant.Dict("en_US")
    for field in included_fields:

        with arcpy.da.SearchCursor(fc, [field]) as cursor:
            for row in cursor:
                conv_string = ''.join(row)
                split_words = conv_string.split()
                global word
                for word in split_words:

                    if word not in used_words:
                        if d.check(word):
                            used_words.append(word)
                            pass

                        else:
                            words_list = d.suggest(word)

                            print words_list
                            global change
                            change = raw_input("What word in list would you like to change "
                                               + word + " to or keep it the same?")
                            used_words.append(word)
                            change_words[word] = change
                del row
            del cursor
    change_row()


def change_row():
    for field in included_fields:
        if change.title() == 'Same':
            pass
        else:
            with arcpy.da.UpdateCursor(fc, [field]) as cursor:
                for row in cursor:
                    for k in change_words:
                        if k in row:
                            for r in row:
                                new_row = r.replace(k, change_words[k])
                                r = new_row

                                cursor.updateRow([r])
    find_similiar()


number_of_instances = []
num_of_instances = []
change_similiar = {}


def find_similiar():
    for field in included_fields:
        with arcpy.da.SearchCursor(fc, [field]) as cursor:
            for row in cursor:
                new_row = ''.join(row)
                num_of_instances.append(str(new_row))

            count_dict = Counter(num_of_instances)

            for k, v in count_dict.items():
                if v == 1:

                    results = difflib.get_close_matches(k, num_of_instances)

                    for result in results[1::]:
                        if result in num_of_instances:
                            statement = "Do you want to change " + k + " to " + result + "?"

                            answer = raw_input(statement)
                            if answer == 'yes':
                                change_similiar[k] = result
        del cursor

        with arcpy.da.UpdateCursor(fc, [field]) as second_cursor:
            for second_row in second_cursor:
                for key in change_similiar:
                    if key in second_row:
                        for r in second_row:
                            new_row = r.replace(key, change_similiar[key])
                            r = new_row
                            second_cursor.updateRow([r])


find_fields()


