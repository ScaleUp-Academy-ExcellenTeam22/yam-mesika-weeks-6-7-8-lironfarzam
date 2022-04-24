class Message:
    """A Message class. Manages the content of messages.

    Args:
        message_id (int) : id of the message.
        message_body (str) : content of the message.
        sender (str) : who send the message.
        recipient (str) : who recipient the message.
        read (bool) : bool to mark if the message is read.
    """

    def __init__(self, message_id: int, message_body: str, sender: str, recipient: str, read: bool = False):
        self.id = message_id
        self.body = message_body
        self.sender = sender
        self.recipient = recipient
        self.read = read

    def __str__(self):
        return f"message id : {self.id}\n" \
               f"sender :{self.sender}\n" \
               f"content: {self.body}\n" \
               f"recipient :{self.recipient}\n"

    def __len__(self):
        """ Return message's content length. """
        return len(self.body)

    def mark_as_read(self):
        """ mark the message as read. """
        self.read = True

    def mark_as_unread(self):
        """ mark the message as unread. """
        self.read = False

    def is_the_message_read(self):
        """ return if the message as read. True or False. """
        return self.read


class PostOffice:
    """A Post Office class. Allows users to message each other.

    Args:
        usernames (list): Users for which we should create PO Boxes.

    Attributes:
        message_id (int): Incremental id of the last message sent.
        boxes (dict): Users' inboxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

        Args:
            sender (str): The message sender's username.
            recipient (str): The message recipient's username.
            message_body (str): The body of the message.
            urgent (bool, optional): The urgency of the message.
                                    Urgent messages appear first.

        Returns:
            int: The message ID, auto incremented number.

        Raises:
            KeyError: If the recipient does not exist.

        Examples:
            After creating a PO box and sending a letter,
            the recipient should have 1 message in the
            inbox.

            po_box = PostOffice(['a', 'b'])
            message_id = po_box.send_message('a', 'b', 'Hello!')
            len(po_box.boxes['b'])
            1
            message_id
            1
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = Message(message_id = self.message_id,
                                  message_body=message_body,
                                  sender=sender,
                                  recipient=recipient)
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, usernames: str, num_of_messages_to_read: int = None):
        """
        Return the first "num_of_messages_to_read" messages in the user's inbox.
        If no "num_of_messages_to_read" have been forwarded, return all messages in the user's inbox.
        The messages will be marked as read and will not be returned to the user on the next call.
        :param usernames: Username you want to read messages
        :param num_of_messages_to_read: (int) The maximum number of messages the user wants to read
        :return: list_of_messages_to_return List of "num_of_messages_to_read" which have not yet been read
        """

        list_of_messages_to_return = []
        if not num_of_messages_to_read or num_of_messages_to_read > len(self.boxes[usernames]):
            num_of_messages_to_read = len(self.boxes[usernames])

        # It could have been written shorter but it came at the expense of understanding the code
        for message in self.boxes[usernames][:num_of_messages_to_read]:
            if not message.is_the_message_read():
                list_of_messages_to_return.append(message)
                message.mark_as_read()

        return list_of_messages_to_return

    def search_inbox(self, usernames: str, string: str) -> list:
        """ Return all the messages inside user_name's box that include at their body the string.
        :param usernames: Wanted usernames box to search in.
        :param string: String to search for.
        :return: List of the messages that including the string at their body.
        :raises KeyError: If user name doesn't exist.
        """

        return [[message for message in self.boxes[usernames] if string in message.body]]


if __name__ == '__main__':

    msg = Message(message_id=1,
                  message_body="hello 0",
                  sender="aaa",
                  recipient="bbb")
    print(msg)

    users = ('aaa', 'bbb', 'ccc')
    post_office = PostOffice(users)
    message_id = post_office.send_message(
        sender='aaa',
        recipient='bbb',
        message_body='Hello,1',
    )
    message_id = post_office.send_message(
        sender='aaa',
        recipient='bbb',
        message_body='Hello,2',
    )
    message_id = post_office.send_message(
        sender='bbb',
        recipient='ccc',
        message_body='Hello,3',
    )
    message_id = post_office.send_message(
        sender='ccc',
        recipient='aaa',
        message_body='Hello,4',
    )
    print(f"sent message number {message_id}.")

    print("--aaa msg--:")
    for msg in post_office.boxes['aaa']:
        print(msg)

    print("--bbb msg--:")
    for msg in post_office.boxes['bbb']:
        print(msg)

    print("--ccc msg--:")
    for msg in post_office.boxes['ccc']:
        print(msg)

    print("--read_inbox('aaa', 1)--:")
    for msg in post_office.read_inbox('aaa', 1):
        print(msg)

    print("--read_inbox('bbb', 1)--:")
    for msg in post_office.read_inbox('bbb', 1):
        print(msg)

    print("--read_inbox('bbb', 2)--:")
    for msg in post_office.read_inbox('bbb', 2):
        print(msg)

