import addressbook_pb2
person = addressbook_pb2.Person()


person_dict = {'phones': [{'type': 2, 'number': u'469-2370'}], 'email': u'copeterson07@gmail.com', 'name': u'Curtis Peterson', 'id': 7777}

def import_dict(person, person_dict):
    key_value_list = []

    for descriptor in person.DESCRIPTOR.fields:
        value = person_dict.get(descriptor.name)
        print "Dictionary value: {0}".format(value)
        key_value_list.append("{0}={1}".format(descriptor.name, str(value)))

    return key_value_list

result = import_dict(person, person_dict)




def dump_object(obj):
    for descriptor in obj.DESCRIPTOR.fields:
        value = getattr(obj, descriptor.name)
        if descriptor.type == descriptor.TYPE_MESSAGE:
            if descriptor.label == descriptor.LABEL_REPEATED:
                map(dump_object, value)
            else:
                dump_object(value)
        elif descriptor.type == descriptor.TYPE_ENUM:
            enum_name = descriptor.enum_type.values[value].name
            print "%s: %s" % (descriptor.full_name, enum_name)
        else:
            print "%s: %s" % (descriptor.full_name, value)

