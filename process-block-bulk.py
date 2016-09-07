#!/usr/bin/python
bulk = open('/home/sbathe/Downloads/bulk/03-09-2007-TO-16-09-2015_bulk.csv','r').readlines()
block = open('/home/sbathe/Downloads/bulk/03-09-2007-TO-18-09-2015_block.csv','r').readlines()

#investors = [ "Ramdev", "Raamdeo", "Jhunhunwala", "Rare Enterprises", "Sajay Bakshi", "ValueQuest", "Nirmal Jain", "Indiainfoline", "India infoline", "Kenneth Andrade", "Damani", "Dharamshi", "ValueQuest", "Brightstar", "Nirmal Bang", "Porinju Veliyath", "Nilesh Shah", "Ekansh Mittal", "Mittal Consulting", "Vijay Kedia", "Daljeet Kohli", "Dolly", "rajiv khanna", "Nalanda", "Indianivesh", "india nivesh" ]

investors = [ "Ramdev", "Raamdeo", "Jhunhunwala", "Rare Enterprises", "Sajay Bakshi", "ValueQuest", "Damani", "Dharamshi", "ValueQuest", "Brightstar", "Veliyath", "Nalanda", "Indianivesh", "india nivesh" ]

bulkblock = bulk + block

op = ''
for i in investors:
    for line in bulkblock:
        if i.lower() in line.lower():
            op = op + line

open('/home/sbathe/Downloads/bulk/03-09-2007-TO-18-09-2015_flags.csv','w').write(op)
