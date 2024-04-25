# email-ping
Sends emails via a remote SMTP server at set intervals.

When using gmail to pull email from a POP3 account, it only checks at random intervals determined
by how many messages it grabs during each check. If you don't receive a lot of email this can lead
to gmail not polling your POP3 account very often, which isn't great when you need to receive email
in a timely manner like 2FA codes.

To trick gmail into checking your POP3 account more often you just need to make sure it always finds
a message to download, which is what this program will do. Then you just need to setup a rule in gmail
to filter on the email subject and send direct to trash, and now you have responsive POP3 through gmail.

# Build
docker build . -t email-ping:latest

# Config
Edit config.json with your settings. The message body needs to include two {} tokens for string replacement later.

# Run
docker-compose up -d email-ping
