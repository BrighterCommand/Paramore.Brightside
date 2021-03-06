""""
File             : messaging_factory.py
Author           : ian
Created          : 20-04-2017

Last Modified By : ian
Last Modified On : 20-04-2017
***********************************************************************
The MIT License (MIT)
Copyright © 2016 Ian Cooper <ian_hammond_cooper@yahoo.co.uk>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
***********************************************************************
"""

from uuid import uuid4
from brightside.messaging import BrightsideMessage, BrightsideMessageBody, BrightsideMessageHeader, BrightsideMessageType


def create_null_message():
    return BrightsideMessage(BrightsideMessageHeader(uuid4(), "", BrightsideMessageType.MT_NONE), BrightsideMessageBody(""))


def create_quit_message():
    body = BrightsideMessageBody(body="")
    header = BrightsideMessageHeader(uuid4(), topic="", message_type=BrightsideMessageType.MT_QUIT)
    return BrightsideMessage(header, body)
