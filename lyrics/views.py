import re
from collections import Counter
from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse


lyrics = """You went to school to learn girl
			Things you never, never knew before
			Like "I" before "E" except after "C"
			And why 2 plus 2 makes 4
			Now, now, now
			I'm gonna teach you
			Teach you, teach you
			All about love girl
			All about love
			Sit yourself down, take a seat
			All you gotta do is repeat after me
			 
			A B C
			It's easy as, 1 2 3
			As simple as, do re mi
			A B C, 1 2 3
			Baby, you and me girl
			A B C
			It's easy as, 1 2 3
			As simple as, do re mi
			A B C, 1 2 3
			Baby, you and me girl
			 
			Come on and love me just a little bit
			Come on and love me just a little bit
			I'm gonna teach you how to sing it out
			Come on, come on, come on
			Let me tell you what it's all about
			Reading, writing, arithmatic
			Are the branches of the learning tree
			But without the roots of love everyday girl
			Your education ain't complete
			Tea-Tea-Teacher's gonna show you
			(She's gonna show you)
			How to get an "A" (na-na-na-naaaaaa)
			How to spell "me", "you", add the two
			Listen to me, baby
			That's all you got to do
			 
			Oh, A B C
			It's easy as, 1 2 3
			As simple as, do re mi
			A B C, 1 2 3
			Baby, you and me girl
			A B C it's easy,
			It's like counting up to 3
			Sing a simple melody
			That's how easy love can be
			That's how easy love can be
			Sing a simple melody
			1 2 3 baby
			You and me
			 
			Sit down girl,
			I think I love ya'
			No, get up girl
			Show me what you can do
			Shake it, shake it baby, come on now
			Shake it, shake it baby, oooh, oooh
			Shake it, shake it baby, yeah
			1 2 3 baby, oooh oooh
			A B C baby, ah, ah
			Do re mi baby, wow
			That's how easy love can be
			A B C it's easy
			It's like counting up to 3
			Sing a simple melody
			That's how easy love can be
			I'm gonna teach you
			How to sing it out
			Come-a, come-a, come-a
			Let me show you what's it's all about
			A B C it's easy
			It's like counting up to 3
			Sing a simple melody
			That's how easy love can be
			 
			I'm gonna teach you
			How to sing it out
			Sing it out, sing it out
			Sing it, sing it
			A B C it's easy
			It's like counting up to 3
			Sing a simple melody
			That's how easy love can be
			"""

def homepage(request):

	all_words = re.findall(r'\w{2,}', lyrics) # filtering words 
	# print all_words
	
	lower_words = []
	for word in all_words:
		lower_words.append(word.lower())
	
	print Counter(lower_words)
	top5words = list(Counter(lower_words).most_common(5))
	low5words = list(Counter(lower_words).most_common()[:-5-1:-1])

	print top5words
	print low5words

	context = {
		'top5words': top5words,
		'low5words': low5words
	}

	context_instance = RequestContext(request)
	return render_to_response('index.html', context, context_instance)



