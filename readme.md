# On Demand Spelling Alphabet Generator

##What is it?

An HTML/jQuery based web app which takes a word and generates a spelling alphabet. An example would be to use this when on the phone with a customer service representative who can't understand just a simple pronunciation of your name. With this app you enter your name, and it will return a random spelling alphabet like:

>"Dowd" -->
>
>>D as in Dog
>>
>>O as in Open
>>
>>W as in Where
>>
>>D as in Days

## How does it do it?

The Spelling generator uses a [Bootstrap UI](http://getbootstrap.com) with a grid system for responsiveness. Using Ajax and [jQuery](http://jquery.com) the app queries an [AWS API-connected Lambda](https://aws.amazon.com/lambda/) function (Python) which queries the [Wordnik Developer API](http://developer.wordnik.com/) to get words to match each letter of the word.

## Roadmap
+ Options
    + Use the same word for duplicate letters
    + Vary the language/types of words retrieved
    + Increase the corpus count for more common words
+ Progress animation
+ Google Material Design
+ Use the Wordnik Python SDK -- (In Progress- branch: sdk-integration)
+ ~~Chrome App~~
    + [Chrome Web App](https://chrome.google.com/webstore/detail/random-spelling-alphabet/ffcbkafemmbdfhgkdojkfdpmbiikcofi)
+ Passport Authentication
+ Persist session to save history/commonly searched words
+ ~~Google Analytics/tracking~~
+ Testing

## Thanks to
+ [Chrome Developers Tutorial: Create Your First App](https://developer.chrome.com/apps/first_app)
+ [ReadWrite: How To Build An API In 10 Minutes](http://readwrite.com/2015/11/16/how-to-build-an-api-amazon-lambda)
