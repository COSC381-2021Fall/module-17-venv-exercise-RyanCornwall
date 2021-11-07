import emoji
import wikipedia
from howdoi import howdoi
print(emoji.emojize('Python is :thumbs_up:'))

print()

page = wikipedia.page("Java")
print(page.summary)

print()

query = "create a file in java"
parser = howdoi.get_parser()
args = vars(parser.parse_args(query.split(' ')))
output = howdoi.howdoi(args)
print(output)