# Find bad inputs and minimize test cases

Here's some (updated) code I used back in undergrad to find bugs
in an assignment we had to write an encoder / decoder for a popular
compression format.

Requires Python 3.

Tests that an input that can be passed through both encoder and
decoder phases without corruption (ie. it's an identity function).
Generates random inputs from a command-line supplied alphabet.

Use like so:

    ./random_input.py ./example/bad_encoder.sh ./example/bad_decoder.sh 'ABC' > bad_input
    ./bisect_input.py ./example/bad_encoder.sh ./example/bad_decoder.sh bad_input > bad_input_min

This is all wrapped up into a bash script:

    ./find_and_minimize.sh ./example/bad_encoder.sh ./example/bad_decoder.sh 'ABC'
    cat bad_input ; echo
    cat bad_input_min ; echo

YMMV

Licensed under GPL v3.
