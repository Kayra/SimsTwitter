from twitter import *
import simplejson as json
import time
import random
from apscheduler.scheduler import Scheduler

sched = Scheduler()
sched.configure(standalone=True)


twitter = Twitter(
            auth=OAuth('41864427-rQTnd0gZZb1w1J1zGsLyNGxdP6Jq7Mm3HGKumB8Ll', '5zIesDuQuQbEdx88E2nrZtuiTIDMpSV80SzGKHjEalQ',
                      'sTYfrPfIZP1OFfTqz0m0Q', 'lCMKOz1iJXlmTEuYnx2dAYuucbi9VceuRAxomCJl5vY')
           )

messages = ["Your energy use has just spiked. You'd better be careful.", 
	         "Do you canoe?", 
	         "You have been chosen. They will come soon.", 
	         "You're a Winter and should decorate accordingly if you want to live most harmoniously in your house.", 
	         "The number 3 is very important in your life right now.", 
	         "Your psychic advisor suggests that you work on improving relationships with those closest to you; you'll need them in the next lunar review.", 
	         "Your psychic advisor has had strong vibrations coming from your Sixth House. Stay away from any building activities during the next week.", 
	         "Your psychic advisor suggests that you keep your secrets well this month. There may be untrustworthy individuals in your environment.", 
	         "The drop off has been made. You've been warned.", 
	         "Your psychic advisor suggests that you plan your meetings very carefully this month as you may have some unexpected news.", 
	         "The number 6 will be very important for you in the next 24 hours.", 
	         "The end is near. Make preparations.", 
	         "The flashing light was just a test. You'll have plenty of warning next time.", 
	         "They're coming soon. Maybe you should think twice about opening the door.", 
	         "They're fixing your phone line. Don't pick up the phone the next time it rings."]

def postTweet(message):
    log = open('log', 'a')
    log.write("\nMessage being tweeted: %s \n" % message)
    print "Message being tweeted: %s" % message
    twitter.statuses.update(status=message)
    log.close()

sched.add_cron_job(lambda: postTweet(random.choice(messages)), day_of_week="0-6/6", hour='2-6/3')

sched.start()

#Get a random message
# random.randint(0, len(messages))

#postTweet(messages[9])

#TODO:
#Delete message after 5 minutes