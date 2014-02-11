import hashlib
import binascii
import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types
from evernote.api.client import NoteStore

from evernote.api.client import EvernoteClient

# Real applications authenticate with Evernote using OAuth, but for the
# purpose of exploring the API, you can get a developer token that allows
# you to access your own Evernote account. To get a developer token, visit
# https://sandbox.evernote.com/api/DeveloperToken.action
auth_token = "S=s1:U=8deab:E=14b758aef46:C=1441dd9c348:P=1cd:A=en-devtoken:V=2:H=0105be733cb2cd6262ed58a41e0a9838"


# Initial development is performed on our sandbox server. To use the production
# service, change sandbox=False and replace your
# developer token above with a token from
# https://www.evernote.com/api/DeveloperToken.action
client = EvernoteClient(token=auth_token, sandbox=True)

user_store = client.get_user_store()

version_ok = user_store.checkVersion(
    "Evernote EDAMTest (Python)",
    UserStoreConstants.EDAM_VERSION_MAJOR,
    UserStoreConstants.EDAM_VERSION_MINOR
)
print "Is my Evernote API version up to date? ", str(version_ok)
print ""
if not version_ok:
    exit(1)

noteStore = client.get_note_store()
# notebooks = noteStore.listNotebooks()
# for n in notebooks:
#     print n.name

filter = NoteStore.NoteFilter()

spec = NoteStore.NotesMetadataResultSpec()
spec.includeTitle = True
noteList = noteStore.findNotes(auth_token, filter, 0, 100)
notes = noteList.notes

for note in notes:
    print note.title
# print
# print "Creating a new note in the default notebook"
# print

# To create a new note, simply create a new Note object and fill in
# attributes such as the note's title.
# note = Types.Note()
# note.title = "Test note from EDAMTest.py"

# To include an attachment such as an image in a note, first create a Resource
# for the attachment. At a minimum, the Resource contains the binary attachment
# data, an MD5 hash of the binary data, and the attachment MIME type.
# It can also include attributes such as filename and location.
# image = open('enlogo.png', 'rb').read()
# md5 = hashlib.md5()
# md5.update(image)
# hash = md5.digest()
#
# data = Types.Data()
# data.size = len(image)
# data.bodyHash = hash
# data.body = image
#
# resource = Types.Resource()
# resource.mime = 'image/png'
# resource.data = data
#
# # Now, add the new Resource to the note's list of resources
# note.resources = [resource]
#
# # To display the Resource as part of the note's content, include an <en-media>
# # tag in the note's ENML content. The en-media tag identifies the corresponding
# # Resource using the MD5 hash.
# hash_hex = binascii.hexlify(hash)
#
# # The content of an Evernote note is represented using Evernote Markup Language
# # (ENML). The full ENML specification can be found in the Evernote API Overview
# # at http://dev.evernote.com/documentation/cloud/chapters/ENML.php
# note.content = '<?xml version="1.0" encoding="UTF-8"?>'
# note.content += '<!DOCTYPE en-note SYSTEM ' \
#     '"http://xml.evernote.com/pub/enml2.dtd">'
# note.content += '<en-note>Here is the Evernote logo:<br/>'
# note.content += '<en-media type="image/png" hash="' + hash_hex + '"/>'
# note.content += '</en-note>'
#
# # Finally, send the new note to Evernote using the createNote method
# # The new Note object that is returned will contain server-generated
# # attributes such as the new note's unique GUID.
# created_note = note_store.createNote(note)
#
# print "Successfully created a new note with GUID: ", created_note.guid