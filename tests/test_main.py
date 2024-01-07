import rsv

# ! Runtime Vars
sampledata = [
    ['Name', 'ID', 'Description', 'Data'],
    ['Romanin', '0', '', None, None]
]

# ! Tests
def test_load_dump():
    with open('test.rsv', 'wb') as file:
        rsv.dump(sampledata, file)
    
    with open('test.rsv', 'rb') as file:
        rows = rsv.load(file)
    
    for rindex, row in enumerate(rows):
        for vindex, value in enumerate(row):
            assert value == sampledata[rindex][vindex]

def test_load_split():
    with open('test.rsv', 'wb') as file:
        rsv.dump(sampledata, file)
    
    with open('test.rsv', 'rb') as file:
        rows = rsv.load_split(file)
    
    for rindex, row in enumerate(rows):
        for vindex, value in enumerate(row):
            assert value == sampledata[rindex][vindex]
