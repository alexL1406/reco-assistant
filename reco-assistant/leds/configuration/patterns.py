from leds.configuration.colors import Colors


class Patterns:
    DEFAULT_IDLE_PATTERN = [
        {0: Colors.GREEN, 1: Colors.ORANGE, 2: Colors.GREEN, 3: Colors.ORANGE, 4: Colors.GREEN, 5: Colors.ORANGE,
         6: Colors.GREEN, 7: Colors.ORANGE, 8: Colors.GREEN, 9: Colors.ORANGE, 10: Colors.GREEN, 11: Colors.ORANGE}
    ]

    DETECTION_PATTERN = [
        {0: Colors.GREEN, 1: Colors.ORANGE, 2: Colors.GREEN, 3: Colors.ORANGE, 4: Colors.GREEN, 5: Colors.ORANGE,
         6: Colors.GREEN, 7: Colors.ORANGE, 8: Colors.GREEN, 9: Colors.ORANGE, 10: Colors.GREEN, 11: Colors.ORANGE},
        
        {0: Colors.ORANGE, 1: Colors.GREEN, 2: Colors.ORANGE, 3: Colors.GREEN, 4: Colors.ORANGE, 5: Colors.GREEN,
         6: Colors.ORANGE, 7: Colors.GREEN, 8: Colors.ORANGE, 9: Colors.GREEN, 10: Colors.ORANGE, 11: Colors.GREEN}
    ]
    
    RECORDING_PATTERN = [
        {0: Colors.PURPLE, 1: Colors.OFF, 2: Colors.PURPLE, 3: Colors.OFF, 4: Colors.PURPLE, 5: Colors.OFF,
         6: Colors.PURPLE, 7: Colors.OFF, 8: Colors.PURPLE, 9: Colors.OFF, 10: Colors.PURPLE, 11: Colors.OFF},

        {0: Colors.OFF, 1: Colors.OFF, 2: Colors.OFF, 3: Colors.OFF, 4: Colors.OFF, 5: Colors.OFF,
         6: Colors.OFF, 7: Colors.OFF, 8: Colors.OFF, 9: Colors.OFF, 10: Colors.OFF, 11: Colors.OFF}
    ]

    PROCESSING_PATTERN = [
        {0: Colors.PURPLE, 1: Colors.PURPLE, 2: Colors.PURPLE, 3: Colors.PURPLE, 4: Colors.OFF, 5: Colors.OFF,
         6: Colors.OFF, 7: Colors.OFF, 8: Colors.OFF, 9: Colors.OFF, 10: Colors.OFF, 11: Colors.OFF},

        {0: Colors.OFF, 1: Colors.OFF, 2: Colors.PURPLE, 3: Colors.PURPLE, 4: Colors.PURPLE, 5: Colors.PURPLE,
         6: Colors.OFF, 7: Colors.OFF, 8: Colors.OFF, 9: Colors.OFF, 10: Colors.OFF, 11: Colors.OFF},

        {0: Colors.OFF, 1: Colors.OFF, 2: Colors.OFF, 3: Colors.OFF, 4: Colors.PURPLE, 5: Colors.PURPLE,
         6: Colors.PURPLE, 7: Colors.PURPLE, 8: Colors.OFF, 9: Colors.OFF, 10: Colors.OFF, 11: Colors.OFF},

        {0: Colors.OFF, 1: Colors.OFF, 2: Colors.OFF, 3: Colors.OFF, 4: Colors.OFF, 5: Colors.OFF,
         6: Colors.PURPLE, 7: Colors.PURPLE, 8: Colors.PURPLE, 9: Colors.PURPLE, 10: Colors.OFF, 11: Colors.OFF},

        {0: Colors.OFF, 1: Colors.OFF, 2: Colors.OFF, 3: Colors.OFF, 4: Colors.OFF, 5: Colors.OFF,
         6: Colors.OFF, 7: Colors.OFF, 8: Colors.PURPLE, 9: Colors.PURPLE, 10: Colors.PURPLE, 11: Colors.PURPLE},

        {0: Colors.PURPLE, 1: Colors.PURPLE, 2: Colors.OFF, 3: Colors.OFF, 4: Colors.OFF, 5: Colors.OFF,
         6: Colors.OFF, 7: Colors.OFF, 8: Colors.OFF, 9: Colors.OFF, 10: Colors.PURPLE, 11: Colors.PURPLE}
    ]

    ANSWER_FOUND_PATTERN = [
        {0: Colors.GREEN, 1: Colors.GREEN, 2: Colors.GREEN, 3: Colors.GREEN, 4: Colors.GREEN, 5: Colors.GREEN,
         6: Colors.GREEN, 7: Colors.GREEN, 8: Colors.GREEN, 9: Colors.GREEN, 10: Colors.GREEN, 11: Colors.GREEN}
    ]

    ANSWER_NOT_FOUND_PATTERN = [
        {0: Colors.RED, 1: Colors.RED, 2: Colors.RED, 3: Colors.RED, 4: Colors.RED, 5: Colors.RED,
         6: Colors.RED, 7: Colors.RED, 8: Colors.RED, 9: Colors.RED, 10: Colors.RED, 11: Colors.RED}
    ]
