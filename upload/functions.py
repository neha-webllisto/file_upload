def file_upload(f):
	with open('static/upload/'+f.name,'wb+') as destination:
		for i in f.chunks():
			destination.write(i)
