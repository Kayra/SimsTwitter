from twitter import *
import simplejson as json

twitter = Twitter(
            auth=OAuth('41864427-rQTnd0gZZb1w1J1zGsLyNGxdP6Jq7Mm3HGKumB8Ll', '5zIesDuQuQbEdx88E2nrZtuiTIDMpSV80SzGKHjEalQ',
                      'sTYfrPfIZP1OFfTqz0m0Q', 'lCMKOz1iJXlmTEuYnx2dAYuucbi9VceuRAxomCJl5vY')
           )

def postTweet(message):
    log = open('log', 'a')
    log.write("\nMessage being tweeted: %s" % message)
    print "Message being tweeted: %s" % message
    twitter.statuses.update(status=message)
    log.close()

postTweet("Test tweet gurl")