Feature: vh

    Scenario: Invoke vh
        When I run the command: vh --help
        Then I see the line in standard output: Set image values to VALUE if values are above THRESHOLD

    Scenario: Threshold an image
        When I run the command: vh -n 0.5 -v 2. $HEIMDALI_DATA_DIR/cossin_z5_y5_x5_c2_r4.<ext> cossin_z5_y5_x5_c2_r4_vh_0_5.<ext>
        Then images cossin_z5_y5_x5_c2_r4_vh_0_5.<ext> and $HEIMDALI_DATA_DIR/cossin_z5_y5_x5_c2_r4_vh_0_5.<ext> are equal
    Examples:
      | ext |
      | h5  |
      | inr |

    Scenario: Read from standard input and write to standard output
        When I run the command: cat $HEIMDALI_DATA_DIR/cossin_z5_y5_x5_c2_r4.h5 | vh -n 0.5 -v 2 > cossin_z5_y5_x5_c2_r4_vh_0_5_sdtin.h5
        Then images cossin_z5_y5_x5_c2_r4_vh_0_5_sdtin.h5 and $HEIMDALI_DATA_DIR/cossin_z5_y5_x5_c2_r4_vh_0_5.h5 are equal
