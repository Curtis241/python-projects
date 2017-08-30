import addressbook_pb2
from google.protobuf import json_format

person = addressbook_pb2.Person()
person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"
phone = person.phones.add()
phone.number = "555-4321"
phone.type = addressbook_pb2.Person.HOME

print person.__str__()

json_text = '{"phones": [{"type": "HOME","number": "555-1343"}],"email": "pdoe@example.com","name": "Pete Doe","id": 12234}'


print "initialized: " + str(person.IsInitialized())
print json_format.MessageToJson(person)

json_format.Parse(json_text,person)

print person.__str__()