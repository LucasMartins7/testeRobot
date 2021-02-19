import requests
import csv


def return_locations(token, country):
	head = {'Authorization': 'Bearer '+token }
	locations = requests.get('https://api.clashroyale.com/v1/locations', headers=head)
	res = locations.json()

	for l in res['items']:
		if l['name'] == country: 
			print(l['id'])
			return str(l['id'])


def return_clans(token, clanName, locationId, checkTag):
	tag = ''
	head = {'Authorization': 'Bearer '+token }
	retornoClans = requests.get('https://api.clashroyale.com/v1/clans?name='+requests.utils.quote(clanName)+'&locationId='+locationId, headers=head)
	clans = retornoClans.json()
	for clan in clans['items']:
		if clan['tag'].startswith(checkTag):
			print("Nome do clan encontrado '" +clan['name'] + "' com a tag '"+ str(clan['tag']+"'"))
			tag = str(clan['tag'])
	return tag


def write_members(token, clanTag, pathFile):
	head = {'Authorization': 'Bearer '+token }
	retornoMembers = requests.get('https://api.clashroyale.com/v1/clans/'+requests.utils.quote(clanTag)+'/members', headers=head)
	members = retornoMembers.json()
	with open(pathFile, mode='w',newline='',encoding="utf-8") as employee_file:
		employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		for member in members['items']:
			#print(str(member['name']))
			employee_writer.writerow([str(member['name']),str(member['expLevel']),str(member['trophies']),str(member['role'])])
			#print(str(member['name'])+" "+str(member['expLevel'])+" "+str(member['trophies'])+" "+str(member['role']))


#locationId = return_locations(auth_token)
#clanTag = return_clans(auth_token,'The resistance', locationId, checkTag)
#write_members(auth_token, clanTag, pathFile)



