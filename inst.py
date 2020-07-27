#imports
#instapy version ==0.6.8
from instapy import InstaPy

session = InstaPy(username="anonymousking09", password="anirudh0901")
session.login()

#sessionsettings

session.set_do_comment(True, percentage=100)
session.set_comments(["Nice", "Amazing", "Super"])
session.set_do_follow(enabled=True, percentage=100)
session.set_user_interact(amount=1, randomize=True, percentage=100)

#some changes at the xpath_compile.py file replace xpath["like_image"]

# Remove:
# xpath["like_image"] = {
#     "like": "//section/span/button[*[local-name()='svg']/@aria-label='Like']",
#     "unlike": "//section/span/button[*[local-name()='svg']/@aria-label='Unlike']",
# }

# Replace with:
#
# xpath["like_image"] = {
#     "like": "//section/span/button/div[*[local-name()='svg']/@aria-label='Like']",
#     "unlike": "//section/span/button/div[*[local-name()='svg']/@aria-label='Unlike']",
# }




#important to keep the like_by_tags at action at last

#activities
session.like_by_tags(["dance"],amount=10, interact=True)
session.set_dont_like(["naked", "ass", "nsfw"])

session.end()