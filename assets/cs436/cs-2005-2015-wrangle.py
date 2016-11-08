
import csv
import json

crs_data = []

with open('cs-2005-2015.csv', 'rb') as csvfile:

	data = list(csv.reader(csvfile, delimiter=','))
	hdr = [str(i).lower() for i in data[0]]
	
	for row in range(1, len(data)):
		crs_data.append(data[row])

fd = open('cs-2005-2015.json', 'w')
db = json.dumps(crs_data)
fd.write(db)
fd.close()

fd = open('cs-2005-2015.json', 'r')
db = json.loads(fd.read())
fd.close()

for i in db:
	print i


# $.getJSON( "ajax/test.json", function( data ) {
#   var items = [];
#   $.each( data, function( key, val ) {
#     items.push( "<li id='" + key + "'>" + val + "</li>" );
#   });
 
#   $( "<ul/>", {
#     "class": "my-new-list",
#     html: items.join( "" )
#   }).appendTo( "body" );
# });