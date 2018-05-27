import webbrowser, clipboard, arrow, appex


tag = input('Enter a tag: ')
webbrowser.open('editorial://open/swift_notes.md')
text = appex.get_text()
utc = arrow.utcnow()
local = utc.to('US/Central')
date = local.format('MM-DD-YY HH:mm:ss')
clipboard.set('\n\n' + date + '\n' + 'Tags: ' + tag + '\n' + text)




	
