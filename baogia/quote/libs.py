import uuid 

# Generate unique uid
def generate_uid(tp):
    if(tp=="Volume"):
        return "V"+ uuid.uuid4().hex[:6].upper()+"P"
    else:
        return "P"+ uuid.uuid4().hex[:6].upper()+"V"