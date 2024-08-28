# RAHUL KOONANTAVIDA
# ILLUMIO TECHNICAL ASSESSMENT
# August 28, 2024

# STEP 1 : populate tagMap given mapping information from lookup.txt
# assumption : first row of lookup.txt specifies field names (dstport, protocol, tag)
# given that tags are determined by the combination of dstport and protocol ->
tagMap = {} # create hashmap with key : (dstport, protocol) , value : tag

with open("data/lookup.txt", mode='r') as lookupData:
    fields = lookupData.readline().rstrip().split(",")
    tagMap[(fields[0], fields[1])] = fields[2] # first row - > field names
    # remaining rows -> lookup table data
    # iterate through remaining rows and populate tagMap
    # .lower() to ensure matches are case insensitive
    row = lookupData.readline().lower().rstrip()
    while row:
        # split row inside while loop, rather than prior to loop entry
        # to ensure while loop properly acknowledges EOF
        row = row.split(",")
        tagMap[(row[0], row[1])] = row[2]
        row = lookupData.readline().lower().rstrip()

# STEP 1.5 : Assigned Internet Protocol Numbers
# assumption : INCLUDED iana.txt FILE IS USED TO POPULATE protocolDectoKey
# in order to parse logs.txt and compare log fields with tagMap - >
# we need to create a mapping with
protocolDectoKey = {} # key : protocol decimal (i.e. 6) , value : protocol keyword (i.e. tcp)

with open("data/iana.txt", mode='r') as protocolData:
    fields = protocolData.readline().rstrip().split(",")
    protocolDectoKey[fields[0]] = fields[1] # first row - > field names
    # remaining rows - > protocol data specifications
    # iterate through remaining lines and populate protocolDectoKey
    row = protocolData.readline().rstrip()
    while row:
        row = row.split(",")
        protocolDectoKey[row[0]] = row[1].lower() # .lower() to ensure matches are case insensitive
        row = protocolData.readline().rstrip()

# STEP 2 : parse logs.txt and populate output dictionaries
# assumption : logs are default, version 2 only
tagCounts = {} # tagCounts - > key : tag , value : {count}
portProtocolCounts = {} # portProtocolCounts - > key : (port , protocol) , value : {count}

with open("data/logs.txt", mode='r') as logs:
    # assumption: all rows contain log data; first row does NOT contain field names
    row = logs.readline().lower().rstrip()
    while row:
        row = row.split(" ")
        # check for missing or skipped data by checking row[13] (log-status)
        # if true - > IGNORE LINE
        if row[13] == "nodata" or row[13] == "skipdata":
            row = logs.readline().lower().rstrip()
            continue
        # given that data is not missing or skipped,
        # relevant fields : row[6] (port) & row[7] (protocol)
        port = row[6]
        protocol = protocolDectoKey[row[7]] # update protocol decimal value to protocol keyword
        try: # case 1 : (port, protocol) pair is present in tagMap
            tag = tagMap[(port, protocol)]
            tagCounts[tag] = 1 + tagCounts.get(tag, 0)
            # also, increment corresponding (port, protocol) count due to successful match
            portProtocolCounts[(port, protocol)] = 1 + portProtocolCounts.get((port, protocol), 0)
        except: # case 2 : (port, protocol) pair is NOT present in tagMap
            # therefore, we do not update portProtocolCounts, as there was NOT a successful match
            tagCounts['untagged'] = 1 + tagCounts.get('untagged', 0)
        row = logs.readline().lower().rstrip()

# STEP 3 : write to output file
with open("output.txt", mode='w') as output:
    output.write("Tag Counts:\n")
    output.write("Tag,Count\n")

    for k, v in tagCounts.items():
        output.write(f'{k},{v}\n')

    output.write("\n")
    
    output.write("Port/Protocol Combination Counts:\n")
    output.write("Port,Protocol,Count\n")

    for k, v in portProtocolCounts.items():
        output.write(f'{k[0]},{k[1]},{v}\n')