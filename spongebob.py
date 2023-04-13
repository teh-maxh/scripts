#!/usr/bin/env python3

message = input().lower()
messageBytes = bytearray()
messageBytes.extend(message.encode())
messageBytes[1::2] = messageBytes[1::2].upper()
print('\n' + messageBytes.decode())