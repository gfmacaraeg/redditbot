from django.shortcuts import render
import praw

def index(request):
	image_url = []
	image_data = {}
	print praw
	reddit = praw.Reddit(client_id='DBJ-wTtdIbMWfA',
                     client_secret="Yn8cgRnAbg1btB_n1VYNwx6z09k", password='codingdojo007',
                     user_agent='Student testing /u/cdojobot', username='cdojobot')
	print reddit
	for submission in reddit.subreddit('pics').top('month', limit=100):
    		# print(dir(submission))
    		print submission.preview, submission.url
    		if "jpg" in submission.url:
    			image_url.append({'url':submission.url, 'title':submission.title})


    		# if submission.url[-4:] == "gifv":
    		# 	image_url.append(submission.url[:-1])
    		# else:
    		# 	image_url.append(submission.url)
    	print image_url	
    	context = {
    	'images': image_url
    	}
	# print "This is the type of result subreddit", type(subreddit)
	return render(request,'hello_world_app/index.html', context)