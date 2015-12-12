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
+ Option to use the same word for duplicate letters
+ Option to vary the language/types of words retrieved
+ Progress animation
+ Google Material Design
+ Use the Wordnik Python SDK -- (In Progress- branch: sdk-integration)
+ Chrome App -- (In progress- branch: chrome-app credit to [Chrome Developers](Create Your First App)
++ [Chrome Web App](https://chrome.google.com/webstore/detail/random-spelling-alphabet/ffcbkafemmbdfhgkdojkfdpmbiikcofi)
+ Passport Authentication

## Thanks to
+ [Chrome Developers Tutorial: Create Your First App](Create Your First App)
