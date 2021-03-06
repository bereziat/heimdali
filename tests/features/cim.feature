Feature: cim

    Scenario: Invoke cim
        When I run the command: cim --help
        Then I see the line in standard output: Inputs ASCII value into image

    Scenario: Create a image interactively
        When I run the interactive command: cim <output>

        Then I see in the interactive command standard output: Enter sx, sy, sv, sz
        When I input to the interactive command: 3 4 2 5

        Then I see in the interactive command standard output: Enter pixel type \(0: fixed point, 1: floating point\)
        When I input to the interactive command: <pixel_type>

        Then I see in the interactive command standard output: Enter byte size
        When I input to the interactive command: <byte_size>

        Then I see in the interactive command standard output: Enter pixel values
        When I input the interactive command with the content of the file: $HEIMDALI_DATA_DIR/zero_to_one.txt

        Then I see in the interactive command standard output: <output>
        Then images <output> and $HEIMDALI_DATA_DIR/<output> are equal

    Examples:
      | output             | pixel_type | byte_size |
      | zero_to_one_r4.h5  | 1          | 4         |
      | zero_to_one_r4.inr | 1          | 4         |
      | zero_to_one_f2.h5  | 0          | 2         |
      | zero_to_one_f2.inr | 0          | 2         |
