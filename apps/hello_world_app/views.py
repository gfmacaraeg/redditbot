from django.shortcuts import render, redirect, HttpResponse
import praw



def bot_login():
	if 'reddit' not in request.session:
		reddit = praw.Reddit(client_id='DBJ-wTtdIbMWfA',
	                     client_secret="Yn8cgRnAbg1btB_n1VYNwx6z09k", password='codingdojo007',
	                     user_agent='Student testing /u/cdojobot', username='cdojobot')
		request.session['reddit'] = reddit
	else:
		reddit = request.session['reddit']	
	return reddit


def index(request):
	image_url = []
	filetypes = []
	
	
	reddit = praw.Reddit(client_id='DBJ-wTtdIbMWfA',
                     client_secret="Yn8cgRnAbg1btB_n1VYNwx6z09k", password='codingdojo007',
                     user_agent='Student testing /u/cdojobot', username='cdojobot')
	request.session['reddit'] = 0
	# print reddit
	for submission in reddit.subreddit('aww').top('all', limit=20):
    		# print(dir(submission))
    		if "jpg" in submission.url:
    			image_url.append({'url':submission.url, 'title':submission.title})
    		if submission.url[-4:] not in filetypes:
    			filetypes.append(submission.url[-4:])
    		print submission.id_from_url, " ", submission.id

    		# if submission.url[-4:] == "gifv":
    		# 	image_url.append(submission.url[:-1])
    		# else:
    		# 	image_url.append(submission.url)
    	print filetypes
    	context = {
    	'images': image_url
    	}
	# print "This is the type of result subreddit", type(subreddit)
	return render(request,'hello_world_app/index.html', context)