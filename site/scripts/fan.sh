#!/bin/bash
irsend SEND_ONCE aircon KEY_POWER
wait 0.1
irsend SEND_ONCE aircon KEY_MODE
wait 0.1
irsend SEND_ONCE aircon KEY_F
