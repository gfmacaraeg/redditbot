from django.shortcuts import render, redirect, HttpResponse
import praw
from .models import *


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
	gif = 0
	png = 0
	jpeg = 0
	filetypes = []
	arr = ['gifv', '.jpg', 'leon', 'ifer', 'cher', '.png', '.gif', 'dowl', 'bird', '0a65', 'llar', 'tler', '647a', 'trel', 'hale', '1e4t', '125b', 'webm', '77c5', 'lina', 'tmSL', 'T3Vc', '90d3', 'cb96', 'JW2g', 'ryZV', '8785', 'iEnE', 'JcD5', 'xod', 'e0de', 'klab', 'ond', '431b', 'WyX0', '6798', '4639', '1902', '325c', 'mKmB', '4543', '42c8', '6e55', '2659', 'zEG', '735c', 'NJwr', 'a644', '5710', 'd240', 'W2Bq', 'ehog', 'apso', '026d', 'Pc35', 'ered', '9f59', 'AcF5', '0ccc', 'j66p', 'y2Wf', 'b3a2', 'e30a', 'ytJO', 'a2ef', 'kOd3', '5592', 'rgrp', '9cb4', '3b98', 'tter', 'PnsN', 'IV4', 'Mfw5', 'Atgh', '233a', 'n3zw', 'QLLi', '9531', '6GMW', '3a55', 'a120', 'd095', '8f35', 'b83b', 'dErT', 'yena', '2fce', 'ana']
	reddit = praw.Reddit(client_id='DBJ-wTtdIbMWfA',
                     client_secret="Yn8cgRnAbg1btB_n1VYNwx6z09k", password='codingdojo007',
                     user_agent='Student testing /u/cdojobot', username='cdojobot')
	request.session['reddit'] = 0
	# print reddit
	for submission in reddit.subreddit('pics').top('all', limit=500):
    		# print(dir(submission))
    		if "jpg" in submission.url:
    			image_url.append({'url':submission.url, 'title':submission.title})
    			jpeg += 1
    		elif "gif"	 in submission.url:
    			gif += 1
    		elif "png" in submission.url:
    			png += 1	
    		if submission.url[-4:] not in filetypes:
    			filetypes.append(submission.url[-4:])
    		# print submission.id

    		# if submission.url[-4:] == "gifv":
    		# 	image_url.append(submission.url[:-1])
    		# else:
    		# 	image_url.append(submission.url)
    	print "jpg", jpeg
    	print 'png', png
    	print 'gif', png	
    	# print filetypes
    	context = {
    	'images': image_url
    	}
	# print "This is the type of result subreddit", type(subreddit)
	return render(request,'hello_world_app/index.html', context)