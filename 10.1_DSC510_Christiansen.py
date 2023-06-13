# DSC 510
# Week 10
# Programming Assignment Week 10
# Author: Madison Christiansen
# 11/02/2022
# Description: Telling Chuck Noris joke.

import requests


def main():
    print("Welcome to the Joke Generator")
    print(get_answer())


def get_answer():
    while True:
        joke_1 = input("Would you like to hear a joke? Enter yes or no:").lower().strip()
        if joke_1 == 'no':
            print("No joke for you, come back if you need a laugh!")  # no joke received
            break
        if joke_1 == 'yes':
            request_joke()
        if not joke_1 == 'yes' 'no':
            print("You did not enter a correct response.")
            get_answer()


def request_joke():
    url = "https://api.chucknorris.io/jokes/random"  # url for api
    API_response = requests.request("GET", url)  # pulling the api
    pull_joke = API_response.json()  # formatting the api text into json
    joke = pull_joke['value']  # pulling the 'value' (joke) from the api
    print("Your Chuck Noris joke:", joke)  # returning the 'value'


if __name__ == "__main__":
    main()

#   Change#:1
#   Change(s) Made: added main, welcome message, and the input
#   Date of Change: 11/04/2022
#   Author: Madison Christiansen
#   Change Approved by: Catie Williams
#   Date Moved to Production: 11/06/2022
#   Change#:2
#   Change(s) Made: added the request joke and pulled the 'value' from the given api
#   Date of Change: 11/04/2022
#   Author: Madison Christiansen
#   Change Approved by: Catie Williams
#   Date Moved to Production: 11/06/2022
#   Change#:3
#   Change(s) Made: pasted the correct url, was getting the same joke
#   Date of Change: 11/04/2022
#   Author: Madison Christiansen
#   Change Approved by: Catie Williams
#   Date Moved to Production: 11/06/2022
#   Change#:4
#   Change(s) Made: changed the joke_1 to a while true loop and got rid of the joke_2 to get continuous jokes
#   Date of Change: 11/04/2022
#   Author: Madison Christiansen
#   Change Approved by: Catie Williams
#   Date Moved to Production: 11/06/2022
