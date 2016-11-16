import hashlib
import imaplib
import email
import time


def grab_attached(em):
    attachments=[]
    for part in em.walk():
        if part.get_content_maintype() == 'multipart': continue
        if part.get('Content-Disposition') is None: continue
        attachments.append(part.get_filename())
    return attachments




class DEinbox:
    def __init__(self,e_mail,password):
        self.e_mail=e_mail
        self.password=password
        self.unread=[]
        self.read=['TODO']
        print('initialized variables')
        try:
            obj = imaplib.IMAP4_SSL('imap.gmail.com', '993')
            obj.login(e_mail,password)
            print('logged in')
            obj.select()
            unread_em=obj.search(None, 'Unseen')[1][0].decode('utf-8').split(' ')
            print('got unread emails')
            for em in unread_em:
                em1=email.message_from_string( obj.fetch(em, '(RFC822)')[1][0][1])
                if em1.is_multipart() is False:
                    self.unread.append(emale(em1['From'],em1['Date'][:-6],em1['Subject'],em1.get_payload()))
                else:
                    self.unread.append(emale(em1['From'], em1['Date'][:-6], em1['Subject'], em1.get_payload()[0],
                                             grab_attached(em1)))
                print('parsed an email')
                obj.store(em, '-FLAGS', '\\Seen')
        except:
            print('Trouble Loading Unread Emails')


    def num_unread(self):
        return len(self.unread)

   # @staticmethod
   # def place_unread():





class emale:
    def __init__(self,from_add,Date,subject,body,attachments = []):
        self.from_add = from_add
        self.body = body
        self.attachments = attachments










